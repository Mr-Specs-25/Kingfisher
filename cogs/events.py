import discord

from discord.ext import commands

#========================================================================================================================
#========================================================================================================================

class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

    green = discord.Color.from_rgb(50, 250, 180)

#========================================================================================================================
#========================================================================================================================

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
