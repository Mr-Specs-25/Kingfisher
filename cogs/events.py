import discord

from discord.ext import commands

#========================================================================================================================
#========================================================================================================================

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

#========================================================================================================================
#========================================================================================================================

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
    LightFury = ("<a:R_LightFury:967754943882735676>")

    #kingfisher
    KC = ("https://media.discordapp.net/attachments/821196221837606923/840560249336889364/IMG_20210508_151848.jpg")
    KC_Electro = ("<a:KC_Electro:825642523128758272>")

#========================================================================================================================
#========================================================================================================================

    @commands.Cog.listener()
    async def on_message(self, message):
      if "<@816963491554131998>" in message.content:
            await message.add_reaction(self.PandaRock)
            await message.channel.reply("> *Hi, <@816963491554131998> is no more active on discord servers- you could try dming / contact through other socials-- :dove:*")
      else:
            if "<@752387831480975361>" in message.content:
                  await message.add_reaction(self.LightFury)

    @commands.Cog.listener()
    async def on_raw_message_delete(self, payload):
      message = payload.cached_message
      if(message.guild):
        if message.guild.name == "Kingfisher Gaming Hub":
          delem = discord.Embed(color = message.author.colour)
          delem.set_author(name = message.author, icon_url = message.author.avatar_url)
          delem.add_field(name = f"**Message deleted** \nChannel: #{message.channel.name}", value = f"```Content: \n\t{message.content}```")
          delem.set_footer(text = f"{message.guild} | {message.guild.id}")
          channel = self.client.get_channel(909912516044398623)
          await channel.send(embed = delem)

    @commands.Cog.listener()
    async def on_message_edit(self, before, after):
      if(after.guild):
        if after.guild.name == "Kingfisher Gaming Hub":
          if before.content != after.content:
            edem = discord.Embed(color = after.author.colour)
            edem.set_author(name = after.author, icon_url = after.author.avatar_url)
            edem.add_field(name = f"**Message edited** \nChannel: #{after.channel.name}", value = f"```Before: {before.content} \nAfter: {after.content}```")
            edem.set_footer(text = f"{after.guild} | {after.guild.id}")
            channel = self.client.get_channel(909912516044398623)
            await channel.send(embed = edem)

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
      pass
      


#========================================================================================================================
#========================================================================================================================

def setup(client):
    client.add_cog(Events(client))

#========================================================================================================================
#========================================================================================================================
