import random
import discord

client = discord.Client()

players = []
currentPlayer = ""
tremann = ""

@client.event
async def on_ready():
    print('Logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('!setplayers'):
        await message.channel.send('Nya spelarlista: ' + players)

    if message.content.startswith('!3mann'):
        message.content.
        await message.channel.send('Ny 3mann: ' + tremann)

client.run('token here')


