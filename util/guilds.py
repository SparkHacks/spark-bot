import re

from util.enums import GuildType


def get_guild_type(name: str) -> GuildType:
    if re.match(r"^SparkHacks \d{4} Board$", name):
        return GuildType.BOARD
    else:
        return GuildType.HACKATHON
