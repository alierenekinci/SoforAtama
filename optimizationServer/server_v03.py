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

    gun_y = response["atama_gun"]


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



    for i in soforler:
        for j in otobusler:
            for y in gun_sayisi_y:
                for k in hatlar:
                    for l in seferler:
                        X[(i["sofor_id"], j["otobus_id"], y, k["hat_id"], l["sefer_id"])]\
                            = model.NewBoolVar('X_i%i-j%i-k%i-l%i-y%i' %
                                               (i["sofor_id"], j["otobus_id"], y, k["hat_id"], l["sefer_id"]))

    for y in gun_sayisi_y:
        for k in hatlar:
            for l in seferler:
                model.Add(sum(X[(i["sofor_id"], j["otobus_id"], y, k["hat_id"], l["sefer_id"])]
                              for i in soforler for j in otobusler) == 1)


    # Creates the solver and solve.
    solver = cp_model.CpSolver()
    solver.parameters.linearization_level = 0
    # Enumerate all solutions.
    solver.parameters.enumerate_all_solutions = True

    class DriversSolutionPrinter(cp_model.CpSolverSolutionCallback):
        """Print intermediate solutions."""

        def __init__(self, X, soforler, otobusler, hatlar, seferler, gun_y, limit):
            cp_model.CpSolverSolutionCallback.__init__(self)
            self._X = X
            self._soforler = soforler
            self._otobusler = otobusler
            self._hatlar = hatlar
            self._seferler = seferler
            self._gun_y = gun_y + 1
            self._solution_count = 0
            self._solution_limit = limit
            self._result = []

        @property
        def sonuc(self):
            return self._result

        def on_solution_callback(self):
            self._solution_count += 1
            solution = []
            print('Çözüm %i' % self._solution_count)
            for y in range(1, self._gun_y):
                print('  Gün %i' % y)
                for i in self._soforler:
                    is_working = False
                    for j in self._otobusler:
                        for k in self._hatlar:
                            for l in self._seferler:
                                if self.Value(self._X[(i["sofor_id"], j["otobus_id"], y, k["hat_id"], l["sefer_id"])]):
                                    solution.append({
                                        'sofor': i["sofor_id"],
                                        'otobus': j["otobus_id"],
                                        'hat': k["hat_id"],
                                        'sefer': l["sefer_id"],
                                        'gun': y
                                    })
                                    is_working = True
                                    print('    Şoför %i -> %i. otobüs, %i. hat, %i. sefer' % (i["sofor_id"], j["otobus_id"], k["hat_id"], l["sefer_id"]))
                    if not is_working:
                        print('    Şoför {} çalışmıyor.'.format(i["sofor_id"]))

            self._result.append(solution)
            if self._solution_count >= self._solution_limit:
                print('Stop search after %i solutions' % self._solution_limit)
                self.StopSearch()

        def solution_count(self):
            return self._solution_count

    # Display the first five solutions.
    solution_limit = 3
    solution_printer = DriversSolutionPrinter(X, soforler, otobusler, hatlar, seferler, gun_y, solution_limit)

    solver.Solve(model, solution_printer)

    # print("Optimization Result:", json.dumps(solution_printer.sonuc))

    # Statistics.
    print('\nStatistics')
    print('  - conflicts      : %i' % solver.NumConflicts())
    print('  - branches       : %i' % solver.NumBranches())
    print('  - wall time      : %f s' % solver.WallTime())
    print('  - solutions found: %i' % solution_printer.solution_count())

    response["atama_durum"] = True
    response["atama_sonuc"] = json.dumps(solution_printer.sonuc)
    updateLink = api_link + "atama/" + str(response["atama_id"])
    r = requests.put(updateLink, json=response, headers=headers)


if __name__ == '__main__':
    while True:
        responses = request_get_data(api_link, "atama/")
        for response in responses:
            if response["atama_durum"] == False:
                engine_optimize(response)
        time.sleep(5)
