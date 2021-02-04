import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

intents = discord.Intents().all()
client = commands.Bot(command_prefix='$', intents=intents)


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_member_join(member):
    role = discord.utils.get(member.guild.roles, name='rookie_volunteer')
    await member.add_roles(role)


client.run(TOKEN)
