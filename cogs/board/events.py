import discord
from discord.ext import commands

from config import board
from utils.guilds import is_board_guild


class BoardEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if not is_board_guild(member.guild.name):
            return

        await member.add_roles(
            discord.utils.get(member.guild.roles, name="Board")
        )

        welcome_channel = discord.utils.get(
            member.guild.channels, name=board.channels.WELCOME.name
        )
        introductions_channel = discord.utils.get(
            member.guild.channels, name=board.channels.INTRODUCTIONS.name
        )

        embed = discord.Embed(
            title=f"Welcome to {member.guild.name}!",
            description=(
                f"Glad to see you here, {member.mention}! "
                f"Make sure to check out {introductions_channel.mention} "
                "and introduce yourself to everyone!"
            ),
            color=discord.Color(int("#A5A8C3"[1:], 16)),
        )

        if len(member.roles) == 1:
            embed.set_footer(
                text=(
                    f"{member.guild.owner.mention}, "
                    f"please assign appropriate roles to {member.display_name}!"
                )
            )

        await welcome_channel.send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(BoardEvents(bot))
