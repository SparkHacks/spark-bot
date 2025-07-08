import discord
from discord.ext import commands

class Hacker(commands.Cog):
    def __init__(self, bot: commands.Bot): 
        self.bot = bot

    @commands.slash_command(
        description="Sends SparkHacks bot's latency"
    ) 
    async def ping(self, ctx:  discord.ApplicationContext):
        await ctx.respond(f"Pong! Latency is {self.bot.latency}")

def setup(bot: commands.Bot):
    bot.add_cog(Hacker(bot)) 