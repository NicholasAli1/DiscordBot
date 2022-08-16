import discord
from discord.ext import commands
from discord import embeds
from keep_alive import keep_alive
import os
from dotenv import load_dotenv
load_dotenv()

bot = commands.Bot(command_prefix = '%')
bot.remove_command('help')

@bot.command()
async def load(ctx, extention):
  bot.load_extension(f'cogs.{extension}')

@bot.command()
async def unload(ctx, extention):
  bot.unload_extension(f'cogs.{extension}')

@bot.command()
async def reload(ctx, extention):
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')

for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    bot.load_extension(f'cogs.{filename[:-3]}')


keep_alive()
bot.run(os.getenv('TOKEN'))