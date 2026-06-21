import discord
from discord.ext import commands

from static import embeds


class RoleCommands(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    role = discord.SlashCommandGroup(
        name="role",
        description="Manage member roles",
        default_member_permissions=discord.Permissions(manage_roles=True),
    )

    @role.command(name="add", description="Add a role to a member")
    async def add(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        role: discord.Role,
    ):
        await ctx.defer()

        if ctx.guild.me.top_role <= role:
            await ctx.edit(embed=embeds.ROLE_FORBIDDEN)
            return
        if ctx.author.top_role <= role:
            await ctx.edit(embed=embeds.ROLE_HIERARCHY)
            return

        await member.add_roles(role)
        await ctx.edit(embed=embeds.ROLE_ADD(member, role))

    @role.command(name="remove", description="Remove a role from a member")
    async def remove(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        role: discord.Role,
    ):
        await ctx.defer()

        if ctx.guild.me.top_role <= role:
            await ctx.edit(embed=embeds.ROLE_FORBIDDEN)
            return
        if ctx.author.top_role <= role:
            await ctx.edit(embed=embeds.ROLE_HIERARCHY)
            return

        await member.remove_roles(role)
        await ctx.edit(embed=embeds.ROLE_REMOVE(member, role))


def setup(bot: commands.Bot):
    bot.add_cog(RoleCommands(bot))
