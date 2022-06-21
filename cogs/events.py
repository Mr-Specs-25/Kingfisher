import discord

from discord.ext import commands


class Events(commands.Cog):
    def __init__(self, client):
        self.client = client

#emotes
    PandaRock = ("<a:RA_PandaRock:909496987622195220>")
    PandaYay = ("<a:RA_PandaYay:909498835578019840>")
    PandaDance = ("<a:RA_PandaDance:909496517973385246>")
    PandaHoorayy = ("<a:RA_PandaHoorayy:909499256291864667>")
    LightFury = ("<a:R_LightFury:967754943882735676>")

#perks
    @commands.Cog.listener()
    async def on_message(self, message):
      if "<@816963491554131998>" in message.content:
            await message.add_reaction(self.PandaRock)
      else:
            if "<@752387831480975361>" in message.content:
                  await message.add_reaction(self.LightFury)

#error-handling
    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        if isinstance(error, commands.MissingPermissions):
          missing_perms_embed = discord.Embed(title = f"Missing Permissions", description = f"You need `{', '.join(error.missing_perms)}` permission to run this Command", color =  ctx.author.color, timestamp = ctx.message.created_at)
          missing_perms_embed.set_footer(text = f"Bad Argument!", icon_url = self.client.user.avatar_url) 
          await ctx.send(embed = missing_perms_embed, delete_after = 10.0)
        if isinstance(error, commands.CommandOnCooldown):
          cooldown_embed = discord.Embed(title = f"Command on Cooldown", description = f"You will be able to run this command after `{round(error.retry_after)} seconds` ", color = ctx.author.color, timestamp = ctx.message.created_at)
          cooldown_embed.set_footer(text = f"Cooldown!", icon_url = self.client.user.avatar_url)
          await ctx.send(embed = cooldown_embed, delete_after = 10.0)

#logging
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
      



def setup(client):
    client.add_cog(Events(client))


