import logging

import discord
from discord.ext import commands

from static import embeds
from utils.channels import get_logs_channel
from utils.enums import LogsType

logger = logging.getLogger(__name__)


class MessageEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_message_delete(self, message: discord.Message):
        if message.author.bot or not message.guild:
            return

        await get_logs_channel(message.guild, LogsType.MESSAGE).send(
            embed=embeds.events.MESSAGE_DELETED(message)
        )
        logger.info(
            f"Message by {message.author} deleted in #{message.channel.name} in {message.guild.name} server"
        )

    @commands.Cog.listener()
    async def on_message_edit(self, before: discord.Message, after: discord.Message):
        if after.author.bot or not after.guild or before.content == after.content:
            return

        await get_logs_channel(after.guild, LogsType.MESSAGE).send(
            embed=embeds.events.MESSAGE_EDITED(before, after)
        )
        logger.info(
            f"Message by {after.author} edited in #{after.channel.name} in {after.guild.name} server"
        )


def setup(bot: commands.Bot):
    bot.add_cog(MessageEvents(bot))
