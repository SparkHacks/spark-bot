import re


def is_board_guild(name: str) -> bool:
    return bool(re.match(r"^SparkHacks \d{4} Board$", name))


def is_hackathon_guild(name: str) -> bool:
    return bool(re.match(r"^SparkHacks \d{4}$", name))
