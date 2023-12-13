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


number = 10
os.makedirs("images", exist_ok=True)
start = time.perf_counter()
for i in range(1, number + 1):
    download_image(i)
end = time.perf_counter()
print(f"Time elapsed: {end - start}")
