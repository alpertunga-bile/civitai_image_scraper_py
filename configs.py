user_agents = [
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:136.0) Gecko/20100101 Firefox/136.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/134.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/133.0.0.0 Safari/537.36",
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/132.0.0.0 Safari/537.36 Edg/132.0.0.0",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/130.0.6723.170 Safari/537.36 OPR/115.0.5322.58",
    "Mozilla/5.0 (X11; Ubuntu; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.5414.145 Safari/537.36",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:135.0) Gecko/20100101 Firefox/135.0",
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/135.0.0.0 Safari/537.36",
    "Mozilla/5.0 (X11; Linux x86_64; rv:137.0) Gecko/20100101 Firefox/137.0",
]

dataset_folder = "datasets"
dataset_filename = "dataset.parquet"

dataset_columns = [
    "id",
    "url",
    "media_type",
    "process",
    "prompt",
    "negativePrompt",
    "cfgScale",
    "steps",
    "sampler",
    "seed",
    "model",
    "clipSkip",
    "resources",
    "likeCountAllTime",
    "laughtCountAllTime",
    "heartCountAllTime",
    "cryCountAllTime",
    "commentCountAllTime",
]

browsing_level_start = 0
browsing_level_end = 1


def set_dataset_conf_from_json(value) -> None:
    global dataset_folder
    global dataset_filename
    global dataset_columns
    global browsing_level_start
    global browsing_level_end

    if value is None:
        return

    if "dataset_columns" in value:
        dataset_columns = value["dataset_columns"]

    if "dataset_filename" in value:
        dataset_filename = value["dataset_filename"]

    if "dataset_folder" in value:
        dataset_folder = value["dataset_folder"]

    browsing_level_ranges = None

    if "browsingLevelRange" in value:
        browsing_level_ranges = value["browsingLevelRange"]

    if browsing_level_ranges is not None:
        browsing_level_start, browsing_level_end = browsing_level_ranges
