import discord
from discord.ext import commands

from cogs.commands import CommandHelpers
from configs.board.channels import CHANNELS
from configs.board.roles import ROLES
from configs.board.teams import TEAMS
from configs.guilds import BOARD_GUILD_IDS
from utils.decorators import is_in_guilds

class BoardCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="setup")
    @is_in_guilds(*BOARD_GUILD_IDS)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def setup(self, ctx: commands.Context):
        await CommandHelpers.setup(ctx, ROLES, CHANNELS)

    @commands.command(name="syncusers")
    @is_in_guilds(*BOARD_GUILD_IDS)
    @commands.guild_only()
    @commands.has_permissions(administrator=True)
    async def sync_users(self, ctx: commands.Context):
        guild: discord.Guild = ctx.guild

        for member in guild.members:
            await CommandHelpers.sync_user(member, TEAMS)
 
def setup(bot: commands.Bot):
    bot.add_cog(BoardCommands(bot)) 