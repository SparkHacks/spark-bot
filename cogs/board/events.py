import discord
from discord.ext import commands

import logging

from cogs.board.commands import CommandHelpers
from configs.board.channels import WELCOME_CHANNEL_NAME, INTRODUCTIONS_CHANNEL_NAME
from configs.board.teams import TEAMS
from configs.guilds import BOARD_GUILD_IDS
from utils.decorators import is_in_guilds

logger = logging.getLogger(__name__)

class BoardEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    @is_in_guilds(*BOARD_GUILD_IDS)
    async def on_member_join(self, member: discord.Member):  
        await CommandHelpers.sync_user(member, TEAMS)
        await member.add_roles(discord.utils.get(member.guild.roles, name="Board"))

        welcome_channel = discord.utils.get(member.guild.channels, name=WELCOME_CHANNEL_NAME)
        introductions_channel = discord.utils.get(member.guild.channels, name=INTRODUCTIONS_CHANNEL_NAME)

        embed = discord.Embed(
            title=f"Welcome to {member.guild.name}!",
            description=(
                f"Glad to see you here, {member.mention}! "
                f"Make sure to check out {introductions_channel.mention} and introduce yourself to everyone!"
            ),
            color=discord.Color(int("#A5A8C3"[1:], 16))
        )

        if len(member.roles) == 1:
            embed.set_footer(f"{member.guild.owner.mention}, please assign appropriate roles to {member.display_name}!")

        await welcome_channel.send(embed=embed)
        
def setup(bot: commands.Bot):
    bot.add_cog(BoardEvents(bot)) 