import discord
from discord.ext import commands

from config import hackathon
from utils.guilds import is_hackathon_guild


class HackathonEvents(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_member_join(self, member: discord.Member):
        if not is_hackathon_guild(member.guild.name):
            return

        await member.add_roles(
            discord.utils.get(
                member.guild.roles,
                name=hackathon.roles.categories.PERSONAL.name,
            ),
            discord.utils.get(
                member.guild.roles,
                name=hackathon.roles.categories.EXPERIENCE.name,
            ),
            discord.utils.get(
                member.guild.roles,
                name=hackathon.roles.categories.TEAM_STATUS.name,
            ),
        )

        embed = discord.Embed(
            title=f"Welcome to {member.guild.name}!",
            description=f"Glad to see you here, {member.mention}!",
            color=discord.Color(int("#A5A8C3"[1:], 16)),
        )

        await discord.utils.get(
            member.guild.channels,
            name=hackathon.channels.WELCOME.name,
        ).send(embed=embed)


def setup(bot: commands.Bot):
    bot.add_cog(HackathonEvents(bot))
