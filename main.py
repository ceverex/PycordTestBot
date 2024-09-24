import discord
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()
intents.message_content = True
bot = discord.Bot()
token = os.getenv('TOKEN)

@bot.event
async def on_ready():
        print(f'Bot has logged in: {bot.user}')
        await bot.change_presence(status=discord.Status.online, activity=discord.Game("testing bot"))

bot.run(token)



