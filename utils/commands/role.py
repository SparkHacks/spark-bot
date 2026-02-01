import discord

import configs.board.teams
import configs.hackathon.teams
from configs.guilds import BOARD_GUILD_IDS, HACKATHON_GUILD_IDS


async def sync(guild: discord.Guild, members: list[discord.Role]):
    if guild.id in BOARD_GUILD_IDS:
        teams = configs.board.teams.TEAMS
    elif guild.id in HACKATHON_GUILD_IDS:
        teams = configs.hackathon.teams.TEAMS
    else:
        return

    for member in members:
        for team in teams:
            if member.id not in team.members:
                continue

            team_role = discord.utils.get(member.guild.roles, name=team.name)
            if team_role not in member.roles:
                await member.add_roles(team_role)
