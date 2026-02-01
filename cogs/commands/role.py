import discord
from discord.ext import commands

import utils.commands.role
from configs.guilds import SPARKHACKS_GUILD_IDS


class RoleCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    role = discord.SlashCommandGroup(
        name="role",
        description="",
        guild_ids=SPARKHACKS_GUILD_IDS,
        default_member_permissions=discord.Permissions(administrator=True),
    )

    @role.command(
        name="sync",
        description="Sync the roles",
    )
    async def sync(self, ctx: discord.ApplicationContext):
        await ctx.defer(ephemeral=True)
        await utils.commands.role.sync(ctx.guild, ctx.guild.members)
        await ctx.respond("Roles are synced!", ephemeral=True)


def setup(bot: commands.Bot):
    bot.add_cog(RoleCommands(bot))
