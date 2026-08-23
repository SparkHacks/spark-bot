from enum import Enum, auto


class GuildType(Enum):
    BOARD = auto()
    HACKATHON = auto()


class LogsType(Enum):
    GATEWAY = auto()
    MEMBER = auto()
    MOD = auto()
    MESSAGE = auto()
