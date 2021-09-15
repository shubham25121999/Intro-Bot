import discord
from discord.ext import commands
import os
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.members = True
client = commands.Bot(command_prefix="!", intents=intents)
my_secret = os.environ['TOKEN']

@client.event
async def on_ready():
  print("We are logged in as {0.user}".format(client))

@client.command()
async def server(ctx):
    name = str(ctx.guild.name)
    description = str(ctx.guild.description)

    owner = str(ctx.guild.owner)
    id = str(ctx.guild.id)
    region = str(ctx.guild.region)
    memberCount = str(ctx.guild.member_count)

    icon = str(ctx.guild.icon_url)

    embed = discord.Embed(
        title = name + " Server Information",
        description = description,
        color = discord.Color.blue()
    )
    embed.set_thumbnail(url=icon)
    embed.add_field(name="Owner", value=owner, inline=True)
    embed.add_field(name="Server ID", value=id, inline=True)
    embed.add_field(name="Region", value=region, inline=True)
    embed.add_field(name="Member Count", value=memberCount, inline=True)
    embed.add_field(name = "GREETINGS!", value = name + " warmly welcomes you!! Hope you enjoy your stay here!!", inline = False)

    await ctx.send(embed=embed)


keep_alive()
client.run(my_secret)