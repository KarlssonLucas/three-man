import random
import discord
from discord.ext import commands

client = discord.Client()
bot = commands.Bot(command_prefix='!')

players = ["Kakan", "Rille", "Balle", "Chips"]
currentPlayer = 0
treman = random.randint(0, len(players))

def next_player():
    return (currentPlayer + 1) % len(players)


def last_player():
    return (currentPlayer - 1) % len(players)


# def add_player(name):

# def remove_player(name):

# def update_treman(name):

# def get_player(name:

def get_treman():
    return players[treman]

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
        
        if "!newtreman" in message.content.lower():


        if not (partone or parttwo):
            currentPlayer = next_player()
            await message.channel.send("Nu är det " + players[currentPlayer])


    if "!update" in message.content.lower():
        players = []
        channel = client.get_channel(289451395373989918)
        members = channel.members
        for member in members:
            players.append(member.name)
        print(players)
        treman = len(players)-1


    if "!treman" in message.content.lower():
        await message.channel.send(str(get_treman()))


@bot.command()
async def on_member_join_channel(member):
    print("aa")


client.run('NzYyMTE1NDEwNTIyNDA2OTMz.X3kdSQ.PJRu4bMpsePdFAz6mGo86rcXr-M')
