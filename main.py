import logging
import os
from pathlib import Path

import discord
from discord.ext import commands
from dotenv import load_dotenv

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)-8s | %(name)s: %(message)s",
    handlers=[logging.StreamHandler()],
)

load_dotenv()
DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")

if __name__ == "__main__":
    if not DISCORD_TOKEN:
        logging.critical("DISCORD_TOKEN not found in environment")
        exit(1)

    bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

    for cog in [
        str(path.with_suffix("")).replace("/", ".")
        for path in Path("cogs").rglob("*.py")
        if path.name != "__init__.py"
    ]:
        bot.load_extension(cog)

    bot.run(DISCORD_TOKEN)
