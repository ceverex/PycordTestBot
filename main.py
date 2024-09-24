import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
bot = discord.Bot()
token = os.getenv('TOKEN')

cogs_list = [
    'eventListener',
    'misc',
    'utilities',
    'moderation'
]

for cog in cogs_list:
    bot.load_extension(f'cogs.{cog}')

bot.run(token)



