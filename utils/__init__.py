import os


def env_int_list(key: str) -> list[int]:
    return [int(val) for val in os.getenv(key).split(",")]
