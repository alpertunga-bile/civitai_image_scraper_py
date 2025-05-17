from .media import MediaOutput
import concurrent.futures
import tqdm
import request_utils


def fill_output(value) -> MediaOutput | None:
    output_elem = MediaOutput()
    ret_val = output_elem.fill(value)

    return output_elem if ret_val else None


def get_output(values: list, function) -> list[MediaOutput]:
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(values)) as executor:
        futures = [executor.submit(function, value) for value in values]

        for future in concurrent.futures.as_completed(futures):
            res = future.result()

            if res is not None:
                results.append(res)

    return results


def get_outputs(media_items) -> list[MediaOutput]:
    outputs: list[MediaOutput] = []

    with tqdm.tqdm(
        total=len(media_items), desc="Filling Items", position=3, leave=False
    ) as pbar:
        for chunk in request_utils.into_chunks(media_items, 128):
            outputs.extend(get_output(chunk, fill_output))
            pbar.update(len(chunk))

    return outputs
