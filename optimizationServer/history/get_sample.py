import requests

API = "http://127.0.0.1:5000/api/v1/"
def requestFunc(API, tag):
    API = str(API) + str(tag)
    response = requests.get(API)
    print(response.text)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    requestFunc(API, "sofor")

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
