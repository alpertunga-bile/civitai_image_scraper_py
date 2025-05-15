import concurrent.futures
import time
import random
import requests

from typing import Any
from configs import user_agents


def into_chunks(arr, chunk_size):
    for i in range(0, len(arr), chunk_size):
        yield arr[i : i + chunk_size]


def parallel_execute(urls: list[str], function):
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(urls)) as executor:
        futures = [executor.submit(function, url) for url in urls]

        for future in concurrent.futures.as_completed(futures):
            results.append(future.result())

    return results


def get_json(url: str) -> Any | None:
    time.sleep(random.random() * 2.0)

    headers = {"User-Agent": user_agents[random.randint(0, len(user_agents) - 1)]}

    response = requests.get(url, headers=headers)

    if response.status_code != 200:
        for _ in range(3):
            time.sleep(random.random() * 2.0)

            headers = {
                "User-Agent": user_agents[random.randint(0, len(user_agents) - 1)]
            }

            response = requests.get(url, headers=headers)

            if response.status_code == 200:
                break

    if response.status_code != 200:
        return None

    return response.json()
