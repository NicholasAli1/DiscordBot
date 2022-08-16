import discord
from discord.ext import commands

class General(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  #Events
  @commands.Cog.listener()
  async def on_ready(self):
    print('Bot Is Online')

  #Commands
  @commands.command()
  async def ping(self, ctx):
    latency = bot.latency
    await ctx.send(latency)
    
  

def setup(bot):
  bot.add_cog(General(bot))