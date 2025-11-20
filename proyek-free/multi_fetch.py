import time
import requests
from multiprocessing import Pool

URL = "https://jsonplaceholder.typicode.com/todos/1"

def fetch(_):
    r = requests.get(URL)
    return r.json()

def main():
    start = time.time()

    with Pool(10) as p:
        p.map(fetch, range(20))

    end = time.time()
    print("Multiprocessing time:", end - start)

if __name__ == "__main__":
    main()
