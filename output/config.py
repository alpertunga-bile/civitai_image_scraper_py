def get_config_url(id: int) -> str:
    base_url = "https://civitai.com/api/trpc/image.getGenerationData"

    params = ('{"json":{' + f'"id": {id}' + "}}").strip()

    return f"{base_url}?input=" + params
