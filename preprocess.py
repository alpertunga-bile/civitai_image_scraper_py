import regex as re


def fix_commas(value: str) -> str:
    multiwhitespaces_regex = re.compile(r"\s+")
    nonpromptcommas_regex = re.compile(r"(,\s){2,}")

    modified_value = multiwhitespaces_regex.sub(" ", value)
    modified_value = nonpromptcommas_regex.sub(", ", modified_value)

    return modified_value
