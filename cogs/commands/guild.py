import logging

import discord
from discord.ext import commands

import embeds
from config import board, hackathon, permissions
from utils.dataclasses import Channel, ChannelCategory
from utils.guilds import is_board_guild, is_hackathon_guild

logger = logging.getLogger(__name__)


async def create_guild(guild: discord.Guild, roles: list, channels: list):
    for role in roles:
        await guild.create_role(
            name=role.name,
            permissions=role.permissions,
            color=role.color,
            hoist=role.hoist,
        )

    board = discord.utils.get(guild.roles, name="Board")

    for item in channels:
        overwrites = {
            guild.default_role: permissions.overwrites.DENY,
            board: permissions.overwrites.READ_WRITE,
        }
        for role, overwrite in item.overwrites.items():
            key = (
                guild.default_role
                if role.name == "@everyone"
                else discord.utils.get(guild.roles, name=role.name)
            )
            overwrites[key] = overwrite

        if isinstance(item, Channel):
            await guild.create_text_channel(
                name=item.name, overwrites=overwrites
            )
        elif isinstance(item, ChannelCategory):
            category_channel = await guild.create_category(
                name=item.name, overwrites=overwrites
            )
            for channel in item.channels:
                ch_overwrites = {**overwrites}
                for role, overwrite in channel.overwrites.items():
                    key = (
                        guild.default_role
                        if role.name == "@everyone"
                        else discord.utils.get(guild.roles, name=role.name)
                    )
                    ch_overwrites[key] = overwrite

                match channel.type:
                    case "text":
                        await guild.create_text_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=ch_overwrites,
                        )
                    case "voice":
                        await guild.create_voice_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=ch_overwrites,
                        )
                    case "forum":
                        await guild.create_forum_channel(
                            name=channel.name,
                            category=category_channel,
                            overwrites=ch_overwrites,
                        )


class GuildCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    guild = discord.SlashCommandGroup(
        name="guild",
        description="",
        default_member_permissions=discord.Permissions(administrator=True),
    )

    @guild.command(name="setup", description="Set up the server")
    async def setup(self, ctx: discord.ApplicationContext):
        await ctx.defer(ephemeral=True)

        guild: discord.Guild = ctx.guild

        if is_board_guild(guild.name):
            await create_guild(
                guild, board.roles.ROLES, board.channels.CHANNELS
            )
            welcome_channel = discord.utils.get(
                guild.channels, name=board.channels.WELCOME.name
            )

        elif is_hackathon_guild(guild.name):
            await create_guild(
                guild, hackathon.roles.ROLES, hackathon.channels.CHANNELS
            )
            welcome_channel = discord.utils.get(
                guild.channels, name=hackathon.channels.WELCOME.name
            )

            rules = discord.utils.get(
                guild.channels, name=hackathon.channels.RULES.name
            )
            await rules.send(embed=embeds.rules)

        await guild.default_role.edit(permissions=permissions.EVERYONE)
        await guild.edit(system_channel=welcome_channel)

        bots_role = discord.utils.get(guild.roles, name="Bots")
        for member in guild.members:
            if member.bot:
                await member.add_roles(bots_role)

        await ctx.respond("Server was set up!", ephemeral=True)

    @guild.command(name="wipe", description="Wipe the server")
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
