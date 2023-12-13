import multiprocessing
import os
import time

import requests


def download_image(idx: int) -> None:
    url = "https://pokeapi.co/api/v2/pokemon/{}"
    try:
        response = requests.get(url.format(idx))
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        print(err)
        exit(1)

    json_data = response.json()
    image_response = requests.get(
        json_data["sprites"]["other"]["official-artwork"]["front_default"]
    )
    with open(os.path.join("images", json_data["name"] + ".png"), "wb") as f:
        f.write(image_response.content)


def print_square(number):
    print(f"Square of {number} is {number ** 2}")
    time.sleep(2)


def print_cube(number):
    print(f"Cube of {number} is {number ** 3}")
    time.sleep(2)


def print_square_map(number: int) -> int:
    print(f"Square of {number} is {number ** 2}")
    time.sleep(2)
    return number**2


def print_square_with_id(number: int) -> int:
    print(f"Square of {number} is {number ** 2} with PID: {os.getpid()}")
    time.sleep(2)
    return number**2


def return_square(number: int, queue: multiprocessing.Queue) -> None:
    queue.put(number**2)


def main():
    start = time.perf_counter()

    # CPU bound task

    # basic example
    # p1 = multiprocessing.Process(target=print_square, args=(2,))
    # p2 = multiprocessing.Process(target=print_cube, args=(2,))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # map example
    # result = []
    # with multiprocessing.Pool(processes=5) as pool:
    #     # result = pool.map(print_square_map, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
    #     for res in pool.imap_unordered(
    #         print_square_map, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    #     ):
    #         result.append(res)

    # print(result)

    # pid example
    # print(f"Main process PID: {os.getpid()}")
    # p1 = multiprocessing.Process(target=print_square_with_id, args=(2,))
    # p2 = multiprocessing.Process(target=print_square_with_id, args=(2,))

    # p1.start()
    # p2.start()

    # p1.join()
    # p2.join()

    # queue example
    # queue = multiprocessing.Queue()
    # process1 = multiprocessing.Process(target=return_square, args=(2, queue))
    # process2 = multiprocessing.Process(target=return_square, args=(3, queue))

    # process1.start()
    # process2.start()

    # process1.join()
    # process2.join()

    # while not queue.empty():
    #     print(queue.get())

    # requests example

    # I/O bound task
    number = 10
    os.makedirs("images", exist_ok=True)
    start = time.perf_counter()
    with multiprocessing.Pool(processes=5) as pool:
        pool.map(download_image, range(1, number + 1))
    end = time.perf_counter()
    print(f"Time elapsed: {end - start}")


if __name__ == "__main__":
    main()
