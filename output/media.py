import typing
from .config import get_config_url
import request_utils
import json


class MediaOutput:
    id: int
    url: str
    media_type: str
    process: str
    prompt: str
    negativePrompt: str
    cfgScale: float
    steps: int
    sampler: str
    seed: int
    model: str
    clipSkip: int
    resources: str

    def __init__(self) -> None:
        self.id = 0
        self.url = ""
        self.media_type = ""
        self.process = ""
        self.prompt = ""
        self.negativePrompt = ""
        self.cfgScale = 0.0
        self.steps = 0
        self.sampler = ""
        self.seed = 0
        self.model = ""
        self.clipSkip = 0
        self.resources = ""

    def fill_from_inf(self, value: typing.Any) -> None:
        base_image_url = "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA"

        self.id = value["id"]
        self.media_type = value["type"]
        self.model = value["baseModel"]
        piece_url = value["url"]

        extension = "jpeg" if self.media_type == "image" else "webm"

        self.url = f"{base_image_url}/{piece_url}/{self.id}.{extension}"

    def set_if_exists(self, value: typing.Any, param: str) -> None:
        if param in value:
            self.__setattr__(param, value[param])

    def fill_from_conf(self) -> bool:
        config_url = get_config_url(self.id)

        value: typing.Any = request_utils.get_json(config_url)

        if value is None:
            return False

        value = value["result"]["data"]["json"]

        if value is None:
            return False

        self.set_if_exists(value, "process")

        if "resources" in value:
            self.resources = json.dumps(value["resources"], sort_keys=True, indent=None)

        meta = value["meta"]

        if meta is None:
            return False

        self.set_if_exists(meta, "prompt")
        self.set_if_exists(meta, "negativePrompt")
        self.set_if_exists(meta, "sampler")
        self.set_if_exists(meta, "steps")
        self.set_if_exists(meta, "steps")
        self.set_if_exists(meta, "seed")
        self.set_if_exists(meta, "clipSkip")

        return True
