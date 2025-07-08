import discord
from discord.ext import commands

from config import DISCORD_TOKEN

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

for command in ["admin", "hacker"]:
    bot.load_extension(f"cogs.commands.{command}")
    
bot.load_extension("cogs.events")

bot.run(DISCORD_TOKEN)
