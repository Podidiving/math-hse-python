# Multithreading example
# Threads are perfect for IO bound tasks
# Threads are not suitable for CPU bound tasks
import os
import time
from concurrent.futures import ThreadPoolExecutor

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


def main():
    start = time.perf_counter()
    os.makedirs("images", exist_ok=True)
    number = 10
    with ThreadPoolExecutor(max_workers=number) as executor:
        executor.map(download_image, range(1, number + 1))
    end = time.perf_counter()
    print(f"Time elapsed: {end - start}")


if __name__ == "__main__":
    main()
