import polars as pl
import os.path
import threading


def create_dataframe_from_list(infos: list, columns: list[str]) -> pl.DataFrame:
    values: dict[str, list] = {column: [] for column in columns}

    for info in infos:
        for column in columns:
            values[column].append(getattr(info, column))

    return pl.DataFrame(values)


def get_dataframe(dataset_path: str, columns: list[str]) -> pl.DataFrame:
    pl.enable_string_cache()

    if os.path.exists(dataset_path):
        return pl.read_parquet(
            dataset_path, columns=columns, use_pyarrow=True, memory_map=True
        )

    return pl.DataFrame()


def add_postprocss_dataframe(
    df: pl.DataFrame, values: list, unique_column: str, columns: list[str]
) -> pl.DataFrame:
    created_df = create_dataframe_from_list(infos=values, columns=columns)

    if len(created_df) == 0:
        return df

    new_df = pl.concat([df, created_df], how="vertical")
    new_df = new_df.unique([unique_column], keep="last")
    new_df = new_df.shrink_to_fit()

    return new_df


def print_save_dataframe(df: pl.DataFrame, parquet_filename: str):
    df.write_parquet(parquet_filename)

    print(f"Total rows of dataframe: {len(df)}")
    print(df.head(5))


dataset_lock = threading.Lock()


def add_save_dataset(
    dataset_path: str,
    columns: list[str],
    values: list,
    unique_key: str,
    parquet_filename: str,
):
    with dataset_lock:
        df = get_dataframe(dataset_path, columns)
        df = add_postprocss_dataframe(df, values, unique_key, columns)

        print_save_dataframe(df, parquet_filename)
