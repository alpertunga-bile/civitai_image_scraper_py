import dataset_utils
import configs
import tqdm
import json
from logger import logger as log
from logger import set_logger
import os.path
import os

from input import MediaInput, get_media_items
from output import get_outputs


def start_enhance(input: MediaInput) -> None:
    outputs = set()

    for level in tqdm.tqdm(
        range(configs.browsing_level_start, configs.browsing_level_end),
        desc="Browsing Level",
        position=1,
        leave=False,
    ):
        media_items = get_media_items(input, level)
        outputs.update(get_outputs(media_items))

    print("\n" * 2)

    dataset_utils.add_save_dataset(
        os.path.join(configs.datasets_folder, configs.datasets_filename),
        configs.dataset_columns,
        [*outputs],
        "id",
        os.path.join(configs.datasets_folder, configs.datasets_filename),
    )


if __name__ == "__main__":
    set_logger()
    media_input = MediaInput()

    with open("config.json", "r") as file:
        config_inputs = json.loads(file.read())

    log.info("config.json is read")

    configs.set_dataset_conf_from_json(config_inputs["dataset"])
    media_input.set_from_json(config_inputs["input"])

    os.makedirs(configs.datasets_folder, exist_ok=True)

    start_enhance(media_input)
