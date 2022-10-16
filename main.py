import os
from dotenv import load_dotenv
from discord import Intents
from discord.ext import commands


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

intents = Intents.all()
bot = commands.Bot(command_prefix='+', intents=intents)

@bot.command('suma')
async def suma(ctx, num1, num2):
    suma = int(num1) + int(num2)
    await ctx.send(suma)

bot.run(TOKEN)  # type: ignore