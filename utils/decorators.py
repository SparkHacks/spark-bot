from discord.ext import commands

def is_in_guilds(*guild_ids: int):
    async def predicate(ctx: commands.Context):
        return ctx.guild and ctx.guild.id in guild_ids
    
    return commands.check(predicate)