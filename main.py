import input.media
import request_utils

import typing


def get_media_items(
    media_input: input.media.MediaInput, browsing_level: int
) -> list[typing.Any]:
    urls = []

    for cursor in range(0, 50000, media_input.limit):
        media_input.browsingLevel = browsing_level
        media_input.cursor = cursor

        urls.append(media_input.get_url())

    results = request_utils.parallel_execute(urls, request_utils.get_json)
    post_items = []

    for result in results:
        if result is None:
            continue

        try:
            items = result["result"]["data"]["json"]["items"]
        except:
            continue

        post_items.extend(items)

    return post_items


if __name__ == "__main__":
    media_input = input.media.MediaInput()

    media_items = get_media_items(media_input, 0)

    print(len(media_items))
