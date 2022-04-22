import discord
import datetime, time

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

#========================================================================================================================
#========================================================================================================================

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

#========================================================================================================================
#========================================================================================================================

    #colours
    blue = discord.Color.from_rgb(50, 180, 250)
    green = discord.Color.from_rgb(50, 250, 180)
    red = discord.Color.from_rgb(250, 50, 50)

#========================================================================================================================
#========================================================================================================================

    @commands.Cog.listener()
    async def on_ready(self):
        global startTime
        startTime = time.time()

    @commands.command()
    @commands.cooldown(1, 5, commands.BucketType.user)
    async def info(self, ctx):
        Uptime = str(datetime.timedelta(seconds=int(round(time.time()-startTime))))
#        MemberCount = (len([m for m in ctx.guild.members if not m.bot]))
#        BotCount = (len([m for m in ctx.guild.members if m.bot]))
        embed = discord.Embed(title = "**Information**", description = f"```Ping - {self.client.latency*1000:,.0f} ms \nUptime - {Uptime}```",color = self.green, timestamp = ctx.message.created_at)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)


#========================================================================================================================
#========================================================================================================================

def setup(client):
    client.add_cog(Info(client))

#========================================================================================================================
#========================================================================================================================
