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
            m = " - Dela ut eller drick själv" + str(a + b) + " klunkar"
        elif a + b == 7:
            m = " - Seven ahead (" + str(players[next_player()]) + ")"
        elif a + b == 9:
            m = " - Nine behind (" + str(players[last_player()]) + ")"
        elif a + b == 11:
            m = " ....sista dricker"
        else:
            partone = False

        if ((a == 3) or (b == 3)) and (currentPlayer == treman):
            await message.channel.send("Välj ny treman!!! (^namn)")
        elif (a == 3) or (b == 3) or (a + b == 3):
            parttwo = True
            await message.channel.send("TREMAN!!! " + str(players[treman]) + " dricker")

        await message.channel.send(str(a) + " och " + str(b) + m)
         
        if not (partone or parttwo):
            currentPlayer = next_player()
            await message.channel.send("Nästa persons tur, " + players[currentPlayer] + " kör")


    if "!update" in message.content.lower():
        players = []
        channel = client.get_channel('channelid')
        members = channel.members
        for member in members:
            players.append(member.name)
        print(players)
        treman = len(players)-1


    if "!whotreman" in message.content.lower():
        await message.channel.send(str(get_treman()))

    if "^" in message.content.lower():
        trem = "" 
        for s in message.content:
            if s != ^:
               trem += s
        
        for p in players:
            if trem.lower() == p.lower()
                treman = players.index(p)
                

client.run('token here')
