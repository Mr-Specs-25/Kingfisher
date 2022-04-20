import discord
import datetime, time

from discord.ext import commands
from discord.ext.commands.cooldowns import BucketType

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

Online    =  ("<:RA_Online:871075685643452466>")
DND       =  ("<:RA_DoNotDisturb:871075724906332221>")
Idle      =  ("<:RA_Idle:871075755495395338>")
Offline   =  ("<:RA_Offline:871075785883140166>")

#kingfisher
KC = ("https://media.discordapp.net/attachments/821196221837606923/840560249336889364/IMG_20210508_151848.jpg")
KC_Electro = ("<a:KC_Electro:825642523128758272>")

#========================================================================================================================
#========================================================================================================================

class Info(commands.Cog):
    def __init__(self, client):
        self.client = client

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
        embed = discord.Embed(title = "**Information**", description = f"```Ping - {self.client.latency*1000:,.0f} ms \nUptime - {Uptime}```",color = green, timestamp = ctx.message.created_at)
        embed.set_footer(text = f"Requested by {ctx.author}", icon_url = ctx.author.avatar_url)
        await ctx.send(embed = embed)


#========================================================================================================================
#========================================================================================================================

def setup(client):
    client.add_cog(Info(client))

#========================================================================================================================
#========================================================================================================================
