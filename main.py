import dataset_utils
import configs
import tqdm
import json
import os.path
import os
import argparse

from logger import logger as log
from logger import set_logger

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

    dataset_utils.add_save_dataset(
        os.path.join(configs.dataset_folder, configs.dataset_filename),
        configs.dataset_columns,
        [*outputs],
        "id",
        os.path.join(configs.dataset_folder, configs.dataset_filename),
    )


if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        prog="civitai image scraper",
        usage="python main.py",
        description="Scrape CivitAI image and video generation informations",
    )
    parser.add_argument("-c", "--config", action="store", default="config.json")
    args = parser.parse_args()

    config_file = args.config

    set_logger()
    media_input = MediaInput()

    try:
        with open(config_file, "r") as file:
            config_inputs = json.loads(file.read())

        log.info(f"{config_file} is read")
    except Exception as e:
        log.error(f"{config_file} can not read: {e}")
        exit(1)

    configs.set_dataset_conf_from_json(config_inputs["dataset"])
    media_input.set_from_json(config_inputs["input"])

    os.makedirs(configs.dataset_folder, exist_ok=True)

    start_enhance(media_input)
