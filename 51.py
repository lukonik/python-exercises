import requests

URL = "https://jsonplaceholder.typicode.com/todos/1"

try:
    response = requests.get(URL)
    json_data=response.json()
    response.raise_for_status()
    print(json_data)
except TimeoutError:
    print("Timeout error")
except ConnectionError:
    print("Connection error")
except Exception:
    print("SOME ERROR HAPPENED")
