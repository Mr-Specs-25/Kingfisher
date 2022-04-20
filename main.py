import discord
import os

from discord.ext import commands
from datetime import datetime
from time import time

from dotenv import load_dotenv

load_dotenv()

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

#colours
blue = discord.Color.from_rgb(50, 180, 250)
green = discord.Color.from_rgb(50, 250, 180)
red = discord.Color.from_rgb(250, 50, 50)

#emotes
Info       = ("<:RA_Stats:871077269387509831>")
Utility    = ("<:RA_Utility:871077840349720607>")
Moderation = ("<:RA_BanHammer:871077232020439090>")
Games      = ("<:RA_Games:871077302270820424>")
Bullet     = ("<:RA_Bullet:871077168791294012>")
X_Mark     = ("<:RA_XMark:871079164554387541>")

PandaRock = ("<a:RA_PandaRock:909496987622195220>")
PandaYay = ("<a:RA_PandaYay:909498835578019840>")
PandaDance = ("<a:RA_PandaDance:909496517973385246>")
PandaHoorayy = ("<a:RA_PandaHoorayy:909499256291864667>")

#kingfisher
KC = ("https://media.discordapp.net/attachments/821196221837606923/840560249336889364/IMG_20210508_151848.jpg")
KC_Electro = ("<a:KC_Electro:825642523128758272>")

#========================================================================================================================
#========================================================================================================================

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

#auto-responses
@client.event
async def on_message(message):
  if message.channel.id == 820311069024583711:
    if message.content.startswith("!d bump"):
      await message.add_reaction(KC_Electro)
  else:
    if message.channel.id == 894647833989357649:
      if message.content.startswith("u!use"):
        await message.channel.send("Imagine using an item that is of no use...")
    else:
      if message.content.startswith(f".gift"):
          gift = discord.Embed(title = "", description = f"**User** ➜ {message.author.mention} \n**Channel** ➜ {message.channel.mention} \n**Message** ➜ {message.content}", color = blue)
          gift.set_author(name = "Gift Command Triggered!", url = "", icon_url = "")
          gift.set_footer(text = "Kingfisher City", icon_url = KC)
          channel = client.get_channel(899724979036389426)
          await channel.send(embed = gift)

      await client.process_commands(message)

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

