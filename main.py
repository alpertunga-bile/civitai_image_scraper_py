import input.media
import output.media
import request_utils
import tqdm
import concurrent.futures
import dataset_utils
import configs


def fill_output(value) -> output.media.MediaOutput | None:
    output_elem = output.media.MediaOutput()

    output_elem.fill_from_inf(value)
    ret_val = output_elem.fill_from_conf()

    if ret_val is None:
        return None

    return output_elem


def get_output(values: list, function) -> list[output.media.MediaOutput]:
    results = []

    with concurrent.futures.ThreadPoolExecutor(max_workers=len(values)) as executor:
        futures = [executor.submit(function, value) for value in values]

        for future in concurrent.futures.as_completed(futures):
            res = future.result()

            if res is not None:
                results.append(res)

    return results


if __name__ == "__main__":
    media_input = input.media.MediaInput()
    media_input.start_cursor = 1000
    media_input.end_cursor = 2000

    media_items = []

    media_items.extend(input.media.get_media_items(media_input, 0))

    outputs: list[output.media.MediaOutput] = []

    with tqdm.tqdm(total=len(media_items), desc="Filling Items") as pbar:
        for chunk in request_utils.into_chunks(media_items, 128):
            outputs.extend(get_output(chunk, fill_output))
            pbar.update(len(chunk))

    dataset_utils.add_save_dataset(
        "dataset.parquet",
        configs.dataset_columns,
        outputs,
        "id",
        "dataset.parquet",
        "dataset.csv",
    )
