import logging

import discord
from discord.ext import commands

import cogs.board.commands.guild
import cogs.hackathon.commands.guild
from utils.guilds import is_board_guild, is_hackathon_guild

logger = logging.getLogger(__name__)


class GuildCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    guild = discord.SlashCommandGroup(
        name="guild",
        description="",
        default_member_permissions=discord.Permissions(administrator=True),
    )

    @guild.command(
        name="setup",
        description="Set up the server",
    )
    async def setup(self, ctx: discord.ApplicationContext):
        await ctx.defer(ephemeral=True)

        guild: discord.Guild = ctx.guild

        if is_board_guild(guild.name):
            await cogs.board.commands.guild.setup(guild)
        elif is_hackathon_guild(guild.name):
            await cogs.hackathon.commands.guild.setup(guild)

        bots_role = discord.utils.get(guild.roles, name="Bots")

        for member in guild.members:
            if member.bot:
                await member.add_roles(bots_role)

        await ctx.respond("Server was set up!", ephemeral=True)

    @guild.command(
        name="wipe",
        description="Wipe the server",
    )
    async def wipe(self, ctx: discord.ApplicationContext):
        await ctx.defer(ephemeral=True)

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

        await ctx.respond("Server was wiped!", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(GuildCommands(bot))
