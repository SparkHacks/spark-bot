import re
from enum import Enum, auto


class GuildType(Enum):
    BOARD = auto()
    HACKATHON = auto()
    UNKNOWN = auto()


def get_guild_type(name: str) -> GuildType:
    if re.match(r"^SparkHacks \d{4} Board$", name):
        return GuildType.BOARD
    elif re.match(r"^SparkHacks \d{4}$", name):
        return GuildType.HACKATHON
    else:
        return GuildType.UNKNOWN
