import os
import discord
from dotenv import load_dotenv


load_dotenv(verbose=True)

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.all()
client = discord.Client(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print(f"We have logged in as {client.user.name}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("!"):
        await message.channel.send("안녕하세요!")


# start the bot
client.run(TOKEN)
