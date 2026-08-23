import discord

from config import board, hackathon
from util.enums import GuildType, LogsType
from util.guilds import get_guild_type


def get_logs_channel(guild: discord.Guild, logs_type: LogsType) -> discord.TextChannel:
    if get_guild_type(guild.name) == GuildType.HACKATHON:
        match logs_type:
            case LogsType.GATEWAY:
                name = hackathon.channels.GATEWAY_LOGS.name
            case LogsType.MEMBER:
                name = hackathon.channels.MEMBER_LOGS.name
            case LogsType.MOD:
                name = hackathon.channels.MOD_LOGS.name
            case LogsType.MESSAGE:
                name = hackathon.channels.MESSAGE_LOGS.name
    else:
        name = board.channels.LOGS.name

    return discord.utils.get(guild.channels, name=name)
