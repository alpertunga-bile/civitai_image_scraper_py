import typing
import request_utils
import json


def get_config_url(id: int) -> str:
    base_url = "https://civitai.com/api/trpc/image.getGenerationData"

    params = ('{"json":{' + f'"id": {id}' + "}}").strip()

    return f"{base_url}?input=" + params


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
    likeCountAllTime: int
    laughCountAllTime: int
    heartCountAllTime: int
    cryCountAllTime: int
    commentCountAllTime: int

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
        self.likeCountAllTime = 0
        self.laughCountAllTime = 0
        self.heartCountAllTime = 0
        self.cryCountAllTime = 0
        self.commentCountAllTime = 0

    def __key(self):
        return (self.id, self.url)

    def __hash__(self):
        return hash(self.__key)

    def __eq__(self, value):
        if isinstance(value, MediaOutput):
            return self.__key() == value.__key()

        return NotImplemented

    def fill(self, value: typing.Any) -> bool:
        if value is None:
            return False

        self._fill_from_inf(value)
        return self._fill_from_conf()

    def _fill_from_inf(self, value: typing.Any) -> None:
        base_image_url = "https://image.civitai.com/xG1nkqKTMzGDvpLrqFT7WA"

        if "id" in value:
            self.id = value["id"]

        if "type" in value:
            self.media_type = value["type"]

        if "baseModel" in value:
            self.model = value["baseModel"]

        piece_url = value["url"]

        stats = value["stats"]

        if stats is not None:
            self._set_if_exists(stats, "likeCountAllTime")
            self._set_if_exists(stats, "laughCountAllTime")
            self._set_if_exists(stats, "heartCountAllTime")
            self._set_if_exists(stats, "cryCountAllTime")
            self._set_if_exists(stats, "commentCountAllTime")

        extension = "jpeg" if self.media_type == "image" else "webm"

        self.url = f"{base_image_url}/{piece_url}/{self.id}.{extension}"

    def _set_if_exists(self, value: typing.Any, param: str) -> None:
        if param in value:
            self.__setattr__(param, value[param])

    def _fill_from_conf(self) -> bool:
        config_url = get_config_url(self.id)

        value: typing.Any = request_utils.get_json(config_url)

        if value is None:
            return False

        value = value["result"]["data"]["json"]

        if value is None:
            return False

        self._set_if_exists(value, "process")

        if "resources" in value:
            self.resources = json.dumps(value["resources"], sort_keys=True, indent=None)

        meta = value["meta"]

        if meta is None:
            return False

        self._set_if_exists(meta, "prompt")
        self._set_if_exists(meta, "negativePrompt")
        self._set_if_exists(meta, "sampler")
        self._set_if_exists(meta, "steps")
        self._set_if_exists(meta, "seed")
        self._set_if_exists(meta, "cfgScale")
        self._set_if_exists(meta, "clipSkip")

        self.cfgScale = float(self.cfgScale)

        return True
