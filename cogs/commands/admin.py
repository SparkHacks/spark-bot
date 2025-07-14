import discord
from discord.ext import commands

import json
import logging
from dacite import from_dict
from dataclasses import dataclass

logger = logging.getLogger(__name__)

@dataclass
class Channel:
    name: str
    type: str

@dataclass
class Category:
    name: str
    channels: list[Channel]

class Admin(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    def _load_data(self, filename):
        with open(filename, "r") as f_data:
            return json.load(f_data)

    @commands.command(name="setup_board")
    @commands.has_permissions(administrator=True)
    async def setup_board(self, ctx: commands.Context):
        guild: discord.Guild = ctx.guild

        categories = [from_dict(Category, d) for d in self._load_data("configs/board/channels.json")]

        welcome_channel = await guild.create_text_channel("🎉welcome👋")
        await guild.edit(system_channel=welcome_channel)

        for category in categories:
            _category = await guild.create_category(name=category.name)

            for channel in category.channels:
                match channel.type:
                    case "text":
                        await guild.create_text_channel(name=channel.name, category=_category)
                    case "voice":
                        await guild.create_voice_channel(name=channel.name, category=_category)
                    case _:
                        logger.error(f"Unknown channel type: {channel.type}.")

    @commands.command(name="wipe")
    @commands.has_permissions(administrator=True)
    async def wipe(self, ctx: commands.Context):
        guild: discord.Guild = ctx.guild

        for channel in guild.channels:
            try:
                await channel.delete()
            except Exception as e:
                logger.error(f"Error deleting channel {channel.name}: {e}")

        for role in guild.roles:
            if role.name == "@everyone" or guild.me.top_role <= role:
                continue
            
            try:
                await role.delete()
            except Exception as e:
                logger.error(f"Error deleting role {role.name}: {e}")

def setup(bot: commands.Bot):
    bot.add_cog(Admin(bot)) 