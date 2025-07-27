from discord.ext import commands

import logging

logger = logging.getLogger(__name__)

class Events(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logger.info(f"{self.bot.user.name} is ready and online!")
        logger.info(f"{self.bot.user.name} is connected to guilds: {[f'{guild.name}' for guild in self.bot.guilds]}")

def setup(bot: commands.Bot):
    bot.add_cog(Events(bot)) 