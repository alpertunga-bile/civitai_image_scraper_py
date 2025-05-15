import enum
import json


class Reactions(enum.Enum):
    Like = "Like"
    Dislike = "Dislike"
    Laugh = "Laugh"
    Cry = "Cry"
    Heart = "Heart"


class MediaType(enum.Enum):
    Image = "image"
    Video = "video"
    Audio = "audio"


class BaseModels(enum.Enum):
    ODOR = "ODOR"
    SD_1_4 = "SD 1.4"
    SD_1_5 = "SD 1.5"
    SD_1_5_LCM = "SD 1.5 LCM"
    SD_1_5_Hyper = "SD 1.5 Hyper"
    SD_2_0 = "SD 2.0"
    SD_2_0_768 = "SD 2.0 768"
    SD_2_1 = "SD 2.1"
    SD_2_1_768 = "SD 2.1 768"
    SD_2_1_Unclip = "SD 2.1 Unclip"
    SDXL_0_9 = "SDXL 0.9"
    SDXL_1_0 = "SDXL 1.0"
    SD_3 = "SD 3"
    SD_3_5 = "SD 3.5"
    SD_3_5_Medium = "SD 3.5 Medium"
    SD_3_5_Large = "SD 3.5 Large"
    SD_3_5_Large_Turbo = "SD 3.5 Large Turbo"
    Pony = "Pony"
    Flux_1_S = "Flux.1 S"
    Flux_1_D = "Flux.1 D"
    AuraFlow = "AuraFlow"
    SDXL_1_0_LCM = "SDXL 1.0 LCM"
    SDXL_Distilled = "SDXL Distilled"
    SDXL_Turbo = "SDXL Turbo"
    SDXL_Lightning = "SDXL Lightning"
    SDXL_Hyper = "SDXL Hyper"
    Stable_Cascade = "Stable Cascade"
    SVD = "SVD"
    SVD_XT = "SVD XT"
    Playground_v2 = "Playground v2"
    PixArt_a = "PixArt a"
    PixArt_E = "PixArt E"
    Hunyuan_1 = "Hunyuan 1"
    Hunyuan_Video = "Hunyuan Video"
    Lumina = "Lumina"
    Kolors = "Kolors"
    Illustrious = "Illustrious"
    Mochi = "Mochi"
    LTXV = "LTXV"
    CogVideoX = "CogVideoX"
    NoobAI = "NoobAI"
    Wan_Video = "Wan Video"
    Other = "Other"


class Period(enum.Enum):
    Day = "Day"
    Week = "Week"
    Month = "Month"
    Year = "Year"
    AllTime = "AllTime"


class Sort(enum.Enum):
    MostReactions = "Most Reactions"
    MostComments = "Most Comments"
    MostCollected = "Most Collected"
    Newest = "Newest"
    Oldest = "Oldest"
    Random = "Random"


class Includes(enum.Enum):
    Tags = "tags"
    Count = "count"
    Cosmetics = "cosmetics"
    Report = "report"
    Meta = "meta"
    TagIds = "tagIds"
    ProfilePictures = "profilePictures"
    MetaSelect = "metaSelect"


class MediaInput:
    baseModels: list[str]
    period: str
    sort: str
    types: list[str]
    useIndex: bool
    browsingLevel: int
    include: list[str]
    cursor: int
    reactions: list[str]
    limit: int

    def __init__(self) -> None:
        self.baseModels = []
        self.period = Period.AllTime.value
        self.sort = Sort.MostReactions.value
        self.types = [MediaType.Image.value, MediaType.Video.value]
        self.useIndex = True
        self.browsingLevel = 1
        self.include = [Includes.Tags.value]
        self.cursor = 0
        self.reactions = [
            Reactions.Like.value,
            Reactions.Dislike.value,
            Reactions.Laugh.value,
            Reactions.Cry.value,
            Reactions.Heart.value,
        ]
        self.limit = 200

    def to_string(self) -> str:
        input_types = {
            "baseModels": self.baseModels,
            "period": self.period,
            "sort": self.sort,
            "types": self.types,
            "useIndex": self.useIndex,
            "browsingLevel": self.browsingLevel,
            "include": self.include,
            "cursor": self.cursor,
            "reactions": self.reactions,
            "limit": self.limit,
        }

        return (
            '{"json":' + json.dumps(input_types, sort_keys=True, indent=None) + "}"
        ).strip()

    def get_url(self) -> str:
        base_url = "https://civitai.com/api/trpc/image.getInfinite"
        params = self.to_string()

        return f"{base_url}?input=" + params
