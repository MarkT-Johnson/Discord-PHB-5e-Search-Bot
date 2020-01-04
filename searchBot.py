import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
GUILD = os.getenv("DISCORD_GUILD")
client = discord.Client()
guild = None
bot = None


async def search(channel, message):
    await channel.send("generic search")


async def help_com(channel, message):
    await message.channel.send(f"Hello there {message.author.nick}! I am the search bot!\n"
                               f"I am here to help you find information inside the Players HandBook for D&D 5e.\n"
                               f"To use me simply type:\n"
                               f"'-s' : for a generic search\n"
                               f"'-h' : for this help message\n"
                               f"'-c' : for a class search\n"
                               f"'-r' : for a race search\n"
                               f"'-e' : for an equipment search\n")


async def class_search(channel, message):
    await channel.send("class search")


async def race_search(channel, message):
    await channel.send("race search")


async def equip_search(channel, message):
    await channel.send("equipment search")


@client.event
async def on_ready():
    global guild
    global bot
    guild = discord.utils.get(client.guilds, name=GUILD)
    bot = client.user
    print(f'{bot}')
    print(
        f'{client.user} has connected to Discord!\n'
        f'{guild.name}(id: {guild.id})'
    )

    # Greets all members that are online at the moment the bot is ready

    # online = []
    # for mem in guild.members:
    #     if (mem.status == discord.Status.online or mem.status == discord.Status.idle) and mem != bot:
    #         online.append(mem)
    # channel = client.get_channel(662892613250056192)
    # await channel.send("I am the bot.")
    # message = ""
    # for active in online:
    #     message = message + f'\nHello {active.name}'
    # await channel.send(message)

    members = '\n ~ '.join([member.name for member in guild.members])
    print(f'Guild Members:\n ~ {members}')


@client.event
async def on_message(message):
    channel = message.channel
    if channel == client.get_channel(662892613250056192) and message.author != bot:
        await channel.send("Message received")
        commands = {
            "-s": search,
            "-h": help_com,
            "-c": class_search,
            "-r": race_search,
            "-e": equip_search
        }
        command = commands.get(message.content)
        if command is not None:
            await command(channel, message)

client.run(TOKEN)
