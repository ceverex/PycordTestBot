import discord
import datetime
from discord.ext import commands

class Moderation(commands.Cog):

    def __init__(self, bot):
        self.bot = bot

    @discord.slash_command(description='Submit a report against a user')
    async def report(
        self, 
        ctx
    ):
        embed = discord.Embed(
            title="Report Submitted",
            description=f'Thank you for opening a report!',
            color=discord.Colour.blurple(),
        )
        await ctx.respond(embed=embed, ephemeral=True)
    
    @discord.slash_command(description='Kick a user from the server')
    @commands.has_permissions(kick_members=True)
    async def kick(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,  # Just use type hints without discord.Option
        reason: str = None
    ):
        kickEmbed = discord.Embed(
            description=f'{member} has been kicked | Reason: {reason}',
            color=discord.Colour.blurple(),
        )

        if not ctx.author.guild_permissions.kick_members:
            await ctx.respond('You do not have the permissions to use this command.', ephemeral=True)
            return
        try:
            await member.kick(reason=reason)
            await ctx.respond(embed=kickEmbed, ephemeral=True)
        except discord.Forbidden:
            await ctx.respond(f'I do not have permission to kick this user.', ephemeral=True)
        except discord.HTTPException as e:
            await ctx.respond(f'Failed to kick {member}. Error: {e}', ephemeral=True)

    @discord.slash_command(description='Ban a user from the server')
    @commands.has_permissions(ban_members=True)
    async def ban(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        reason: str = None
    ):
        banEmbed = discord.Embed(
            description=f'{member} has been banned | Reason: {reason}',
            color=discord.Colour.blurple(),
        )

        if not ctx.author.guild_permissions.ban_members:
            await ctx.respond('You do not have the permissions to use this command.', ephemeral=True)
            return
        try:
            await member.ban(reason=reason)
            await ctx.respond(embed=banEmbed, ephemeral=True)
        except discord.Forbidden:
            await ctx.respond(f'I do not have permission to ban this user.', ephemeral=True)
        except discord.HTTPException as e:
            await ctx.respond(f'Failed to ban {member}. Error: {e}', ephemeral=True)

    @discord.slash_command(description='Put a user in timeout')
    @commands.has_permissions(moderate_members=True)
    async def timeout(
        self,
        ctx: discord.ApplicationContext,
        member: discord.Member,
        time: int,
        reason: str = None
    ):
        timeoutEmbed = discord.Embed(
            description=f'{member} has been put in timeout for {time} hour(s) | Reason: {reason}',
            color=discord.Colour.blurple(),
        )
        try:
            # Calculate the time until which the member will be timed out
            until = datetime.datetime.utcnow() + datetime.timedelta(hours=time)
            # Apply the timeout
            await member.timeout(until=until, reason=reason)
            # Send a success message
            await ctx.respond(embed=timeoutEmbed, ephemeral=True)
        except discord.Forbidden:
            await ctx.respond(f'I do not have permission to put this user in timeout.', ephemeral=True)
        except discord.HTTPException as e:
            await ctx.respond(f'Failed to timeout {member}. Error: {e}', ephemeral=True)

def setup(bot):
    bot.add_cog(Moderation(bot))
    
