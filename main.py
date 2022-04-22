import discord
import os

from discord.ext import commands
from datetime import datetime
from time import time

#=======================================================================================================================
#=======================================================================================================================

client = discord.Client()
TOKEN = os.getenv("TOKEN")

intents = discord.Intents.all()

client = commands.Bot(command_prefix = "-", intents = intents)
client.remove_command("help")
client.launch_time = datetime.utcnow()

#=======================================================================================================================
#=======================================================================================================================

#events
@client.event
async def on_ready():
    await client.change_presence(activity = discord.Game(name = "Roaming Around Kingfisher!"))
    print ('Kingfisher\'s Ready!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.MissingPermissions):
      missing_perms_embed = discord.Embed(title = f"Missing Permissions", description = f"You need **{', '.join(error.missing_perms)}** Permission to run this Command", color =  ctx.author.color, timestamp = ctx.message.created_at)
      missing_perms_embed.set_footer(text = f"Bad Argument!")
      await ctx.send(embed = missing_perms_embed, delete_after = 10.0)
    if isinstance(error, commands.CommandOnCooldown):
      cooldown_embed = discord.Embed(title = f"Command on Cooldown", description = f"You will be able to run this Command after `{round(error.retry_after)} seconds` ", color = ctx.author.color, timestamp = ctx.message.created_at)
      cooldown_embed.set_footer(text = f"Cooldown!", icon_url = client.user.avatar_url)
      await ctx.send(embed = cooldown_embed, delete_after = 10.0)

#========================================================================================================================
#========================================================================================================================

@client.command()
async def ping(ctx):
    start = time()
    message = await ctx.send(f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms```")
    end = time()
    await message.edit(content=f"```Pong! \nLATENCY: {client.latency*1000:,.0f} ms \nRESPONSE TIME: {(end-start)*1000:,.0f} ms```")


#========================================================================================================================
#========================================================================================================================

#error-handling


#========================================================================================================================
#========================================================================================================================

client.load_extension("cogs.kingfisher")
client.load_extension("cogs.events")
client.load_extension("cogs.eval")


client.run(TOKEN)

#========================================================================================================================
#========================================================================================================================

