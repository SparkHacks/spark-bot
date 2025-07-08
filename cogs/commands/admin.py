from discord.ext import commands

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.command(name="sync")
    @commands.is_owner()
    async def sync_commands(self, ctx: commands.Context):
        await self.bot.sync_commands()

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot)) 