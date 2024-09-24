import discord
from discord.ext import commands

class Utilities(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Help command')
    async def help(self, ctx):

        embed = discord.Embed(
            title='Help Menu',
            description='',
            color=discord.Colour.blurple(),
        )

        for cog in self.bot.cogs:
            cog_commands = self.bot.get_cog(cog).get_commands()
            command_list = "\n".join([f"`/{cmd.name}` - {cmd.description}" for cmd in cog_commands])
            if command_list:
                embed.add_field(name=cog, value=command_list, inline=False)

        await ctx.respond(embed=embed)

def setup(bot):
    bot.add_cog(Utilities(bot))