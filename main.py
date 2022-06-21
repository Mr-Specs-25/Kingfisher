import discord
import os

from discord.ext import commands
from datetime import datetime
from time import time


#setup
TOKEN = os.getenv("TOKEN")
client = discord.Client()
intents = discord.Intents.all()

client = commands.Bot(command_prefix = "-", intents = intents)
client.remove_command("help")
client.launch_time = datetime.utcnow()


#status
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "Roaming Around Kingfisher!"))
    print ('Kingfisher\'s Ready!')


#basic
@client.command()
async def ping(ctx):
    start = time()
    message = await ctx.send(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```")
    end = time()
    await message.edit(content=f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms \nRESPONSE TIME: {(end-start)*1000:,.0f} ms```")


#load-extensions
client.load_extension("cogs.kingfisher")
client.load_extension("cogs.events")
client.load_extension("cogs.eval")


client.run(TOKEN)



