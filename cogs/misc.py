import discord
from discord import guild_only
from discord.ext import commands

class Miscellaneous(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command()
    @guild_only()
    async def ping(self, ctx):
        embed = discord.Embed(
            title="Bot Latency",
            description=f'Latency is {self.bot.latency}',
            color=discord.Colour.blurple(),
        )
        await ctx.respond(embed=embed)
    
def setup(bot):
    bot.add_cog(Miscellaneous(bot))
