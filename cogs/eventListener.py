import discord
from discord.ext import commands

class eventListener(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print(f'Bot has logged in: {self.bot.user}')
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game("/help"))

def setup(bot):
    bot.add_cog(eventListener(bot))