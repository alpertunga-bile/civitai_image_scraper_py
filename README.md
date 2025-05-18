# civitai_image_scraper_py

CivitAI image and video generation scraper to build datasets with selected
columns.

## Setup

- Download the project with
  `git clone https://github.com/alpertunga-bile/civitai_image_scraper.git` code
- Download the requirements with `pip install -r requirements.txt` code
- Create the config file or use the `example_config.json` file
- Start the program with `python main.py`

## Example Config

```json
{
    "dataset": {
        "dataset_columns": [
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
            "laughCountAllTime",
            "heartCountAllTime",
            "cryCountAllTime",
            "commentCountAllTime"
        ],
        "dataset_filename": "dataset.parquet",
        "dataset_folder": "datasets",
        "browsingLevelRange": [0, 1]
    },
    "input": {
        "baseModels": ["SD 1.5"],
        "period": "AllTime",
        "sort": "Most Reactions",
        "types": ["image", "video"],
        "limit": 200,
        "cursorRange": [0, 1000]
    }
}
```

## Config

### Dataset

|        Name        |      Type      | Definition                                                                                                                                     |
| :----------------: | :------------: | :--------------------------------------------------------------------------------------------------------------------------------------------- |
|  dataset_columns   |   list[str]    | Selecting which dataset columns to be included. See [this section](#dataset-columns).                                                          |
|  dataset_filename  |      str       | Dataset filename to be read from or created                                                                                                    |
|   dataset_folder   |      str       | Dataset folder to search the dataset or create the dataset into                                                                                |
| browsingLevelRange | list[int, int] | Left integer is the starting browsing level and right integer is the ending browsing level. The left has to be smaller than the right integer. |

#### Dataset Columns

- The user can select the dataset columns, but the dataset does not to be
  present if this value is updated

<ul>
    <ul>
        <li>id</li>
        <li>url</li>
        <li>media_type</li>
        <li>process</li>
        <li>prompt</li>
        <li>negativePrompt</li>
        <li>cfgScale</li>
        <li>steps</li>
        <li>sampler</li>
        <li>seed</li>
        <li>model</li>
        <li>clipSkip</li>
        <li>resources</li>
        <li>likeCountAllTime</li>
        <li>laughCountAllTime</li>
        <li>heartCountAllTime</li>
        <li>cryCountAllTime</li>
        <li>commentCountAllTime</li>
    </ul>
</ul>

### Input

|    Name     |    Type    | Definition                                                                   |
| :---------: | :--------: | :--------------------------------------------------------------------------- |
| baseModels  | list[str]  | List of images and video models to filter. See [this section](#base-models). |
|   period    |    str     | Period option selection. See [this section](#period).                        |
|    sort     |    str     | Sort option selection. See [this section](#sort).                            |
|    types    | list[str]  | Image, video post item option selection. See [this section](#media-type).    |
|    limit    |  [0, 200]  | The limit in one page                                                        |
| cursorRange | [0, 50000) | The cursor in the image page                                                 |

#### Base Models

- Select the models from the below:

<ul>
    <ul>
        <li>ODOR</li>
        <li>SD 1.4</li>
        <li>SD 1.5</li>
        <li>SD 1.5 LCM</li>
        <li>SD 1.5 Hyper</li>
        <li>SD 2.0</li>
        <li>SD 2.0 768</li>
        <li>SD 2.1</li>
        <li>SD 2.1 768</li>
        <li>SD 2.1 Unclip</li>
        <li>SDXL 0.9</li>
        <li>SDXL 1.0</li>
        <li>SD 3</li>
        <li>SD 3.5</li>
        <li>SD 3.5 Medium</li>
        <li>SD 3.5 Large</li>
        <li>Sd 3.5 Large Turbo</li>
        <li>Pony</li>
        <li>Flux.1 S</li>
        <li>Flux.1 D</li>
        <li>AuraFlow</li>
        <li>SDXL 1.0 LCM</li>
        <li>SDXL Distilled</li>
        <li>SDXL Turbo</li>
        <li>SDXL Lightning</li>
        <li>SDXL Hyper</li>
        <li>Stable Cascade</li>
        <li>SVD</li>
        <li>SVD XT</li>
        <li>Playground v2</li>
        <li>PixArt a</li>
        <li>PixArt E</li>
        <li>Hunyuan 1</li>
        <li>Hunyuan Video</li>
        <li>Lumina</li>
        <li>Kolors</li>
        <li>Illustrious</li>
        <li>Mochi</li>
        <li>LTXV</li>
        <li>CogVideoX</li>
        <li>NoobAI</li>
        <li>Wan Video</li>
        <li>Other</li>
    </ul>
</ul>

#### Period

<ul>
    <ul>
        <li>Day</li>
        <li>Week</li>
        <li>Month</li>
        <li>Year</li>
        <li>AllTime</li>
    </ul>
</ul>

#### Sort

<ul>
    <ul>
        <li>Most Reactions</li>
        <li>Most Comments</li>
        <li>Most Collected</li>
        <li>Newest</li>
        <li>Oldest</li>
        <li>Random</li>
    </ul>
</ul>

#### Media Type

<ul>
    <ul>
        <li>image</li>
        <li>video</li>
    </ul>
</ul>
