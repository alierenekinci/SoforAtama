import json
import time

import requests
from ortools.sat.python import cp_model

headers: dict[str, str] = {
    'Content-type': 'application/json',
    'Accept': 'application/json',
    'charset': 'utf-8'
}

api_link: str = "http://127.0.0.1:5000/api/v1/"


def request_get_data(api, tag):
    r = requests.get(api + tag, headers=headers)
    r.encoding = 'utf-8'
    return r.json()
def engine_optimize(response):
    start = time.time()
    # Data.
    sofor_i = 9
    otobus_j = 2
    hat_k = 2
    sefer_l = 2
    gun_y = 1

    sofor_sayisi_i = range(1, sofor_i + 1) # [1,2,3,4,5,6,7,8,9] [1,2,3,6]
    otobus_sayisi_j = range(1, otobus_j + 1)
    hat_sayisi_k = range(1, hat_k + 1)
    sefer_sayisi_l = range(1, sefer_l + 1)
    gun_sayisi_y = range(1, gun_y + 1)


    soforler = list(request_get_data(api_link, "sofor/"))
    otobusler = request_get_data(api_link, "otobus/")
    hatlar = request_get_data(api_link, "hat/")
    seferler = request_get_data(api_link, "sefer/")
    atama = request_get_data(api_link, "atama/")
    print(soforler, otobusler, hatlar, seferler, atama, sep="\n\n")


    model = cp_model.CpModel()

    # Creates shift variables.
    X = {}

    for i in sofor_sayisi_i:
        for j in otobus_sayisi_j:
            for y in gun_sayisi_y:
                for k in hat_sayisi_k:
                    for l in sefer_sayisi_l:
                        X[(i, j, y, k, l)] = model.NewBoolVar('X_i%i-j%i-k%i-l%i-y%i' % (i, j, y, k, l))

    for y in gun_sayisi_y:
        for k in hat_sayisi_k:
            for l in sefer_sayisi_l:
                model.Add(sum(X[(i, j, y, k, l)] for i in sofor_sayisi_i for j in otobus_sayisi_j) == 1)

    min_sefer_sofor = (otobus_j * gun_y * hat_k * sefer_l) // sofor_i

    if (otobus_j * gun_y * hat_k * sefer_l) % sofor_i == 0:
        max_sefer_sofor = min_sefer_sofor
    else:
        max_sefer_sofor = min_sefer_sofor + 1

    for i in sofor_sayisi_i:
        shifts_worked = []
        for j in otobus_sayisi_j:
            for y in gun_sayisi_y:
                for k in hat_sayisi_k:
                    for l in sefer_sayisi_l:
                        shifts_worked.append(X[(i, j, y, k, l)])
        model.Add(min_sefer_sofor <= sum(shifts_worked))
        model.Add(sum(shifts_worked) <= max_sefer_sofor)

    # Creates the solver and solve.
    solver = cp_model.CpSolver()
    solver.parameters.linearization_level = 0
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True

    class DriversSolutionPrinter(cp_model.CpSolverSolutionCallback):
        """Print intermediate solutions."""

        def __init__(self, X, sofor_i, otobus_j, hat_k, sefer_l, gun_y, limit):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self._X = X
            self._sofor_i = sofor_i + 1
            self._otobus_j = otobus_j + 1
            self._hat_k = hat_k + 1
            self._sefer_l = sefer_l + 1
            self._gun_y = gun_y + 1
            self._solution_count = 0
            self._solution_limit = limit
            self._result = []

        @property
        def sonuc(self):
            return self._result

        def on_solution_callback(self):
            self._solution_count += 1
            self._result = []
            print('Çözüm %i' % self._solution_count)
            for y in range(1, self._gun_y):
                print('  Gün %i' % y)
                for i in range(1, self._sofor_i):
                    is_working = False
                    for j in range(1, self._otobus_j):
                        for k in range(1, self._hat_k):
                            for l in range(1, self._sefer_l):
                                if self.Value(self._X[(i, j, y, k, l)]):
                                    self._result.append({
                                        'driver': i,
                                        'bus': j,
                                        'line': k,
                                        'trip': l,
                                        'day': y
                                    })
                                    is_working = True
                                    print('    Şoför %i -> %i. otobüs, %i. hat, %i. sefer' % (i, j, k, l))
                    if not is_working:
                        print('    Şoför {} çalışmıyor.'.format(i))
            if self._solution_count >= self._solution_limit:
                print('Stop search after %i solutions' % self._solution_limit)
                self.StopSearch()

        def solution_count(self):
            return self._solution_count

    # Display the first five solutions.
    solution_limit = 7
    solution_printer = DriversSolutionPrinter(X, sofor_i, otobus_j, hat_k, sefer_l, gun_y, solution_limit)

    solver.Solve(model, solution_printer)

    print("Optimization Result:", json.dumps(solution_printer.sonuc))

    # Statistics.
    print('\nStatistics')
    print('  - conflicts      : %i' % solver.NumConflicts())
    print('  - branches       : %i' % solver.NumBranches())
    print('  - wall time      : %f s' % solver.WallTime())
    print('  - solutions found: %i' % solution_printer.solution_count())

    response["atama_durum"] = True
    updateLink = api_link + "atama/" + str(response["atama_id"])
    r = requests.put(updateLink, json=response, headers=headers)


if __name__ == '__main__':
    while True:
        responses = request_get_data(api_link, "atama/")
        for response in responses:
            if response["atama_durum"] == False:
                engine_optimize(response)
        time.sleep(5)
