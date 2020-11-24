import random
import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

players = ["Kakan", "Rille", "Balle", "Chips"]
currentPlayer = 0
treman = random.randint(0, len(players))
print(treman)


def next_player():
    return (currentPlayer + 1) % len(players)


def last_player():
    return (currentPlayer - 1) % len(players)


# def add_player(name):

# def remove_player(name):

# def update_treman(name):

# def get_player(name:

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    global currentPlayer, treman, players

    if message.author == client.user:
        return

    if "r1" in message.content.lower():
        a = random.randint(1, 6)
        await message.channel.send(a)

    if "r2" in message.content.lower():
        a = random.randint(1, 6)
        b = random.randint(1, 6)
        m = ""

        partone = True
        parttwo = False

        if a == b:
            m = " - Dela ut " + str(a + b) + " klunkar"
        elif a + b == 7:
            m = " - Seven ahead (" + str(players[next_player()]) + ")"
        elif a + b == 9:
            m = " - Nine behind (" + str(players[last_player()]) + ")"
        elif a + b == 11:
            m = " ....sista dricker"
        else:
            partone = False

        if ((a == 3) or (b == 3)) and (currentPlayer == treman):
            await message.channel.send("Välj ny treman!!! (!treman [namn])")
        elif (a == 3) or (b == 3) or (a + b == 3):
            parttwo = True
            await message.channel.send("TREMAN!!! " + str(players[treman]) + " dricker")

        await message.channel.send(str(a) + " och " + str(b) + m)

        if not (partone or parttwo):
            currentPlayer = next_player()
            await message.channel.send("Nu är det " + players[currentPlayer])

    if "among us" in message.content.lower():
        channel = client.get_channel(289451395373989918)
        members = channel.members  # finds members connected to the channel
        memids = []  # (list)
        for member in members:
            memids.append(member.name)
        print(memids)  # print info
        await message.channel.send("https://twitter.com/Majd1LoL/status/1307735771663790082")

    if "!update" in message.content.lower():
        channel = client.get_channel(289451395373989918)
        members = channel.members
        for member in members:
            players.append(member.name)
        print(players)


@bot.command()
async def on_member_join_channel(member):
    print("aa")


client.run('NzYyMTE1NDEwNTIyNDA2OTMz.X3kdSQ.5mSRu6C3OHdcy_00WDpnVmv9Tn8')
