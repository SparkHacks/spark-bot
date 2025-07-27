from discord.ext import commands

from cogs.commands import Commands
from configs.board.channels import CHANNELS
from configs.board.roles import ROLES
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
        await Commands.setup(ctx, ROLES, CHANNELS)
 
def setup(bot: commands.Bot):
    bot.add_cog(BoardCommands(bot)) 