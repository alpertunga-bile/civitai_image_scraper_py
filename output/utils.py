from .media import MediaOutput
import concurrent.futures
import tqdm


def fill_output(value) -> MediaOutput | None:
    output_elem = MediaOutput()
    ret_val = output_elem.fill(value)

    return output_elem if ret_val else None


def get_outputs(media_items) -> list[MediaOutput]:
    outputs: list[MediaOutput] = []

    with tqdm.tqdm(total=len(media_items), desc="Filling Items") as pbar:
        with concurrent.futures.ThreadPoolExecutor(max_workers=128) as executor:
            futures = [executor.submit(fill_output, item) for item in media_items]

            for future in concurrent.futures.as_completed(futures):
                res = future.result()

                if res is not None:
                    outputs.append(res)

                pbar.update(1)

    return outputs
