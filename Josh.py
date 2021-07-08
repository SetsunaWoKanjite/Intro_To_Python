import discord
from discord.ext import commands
from secrets import * 
import random

client = commands.Bot(command_prefix = "++")


@client.event
async def on_ready():
    print("Ready")

@client.command()
async def balance(ctx):
    await open_account(ctx.author)

    users = await get_bank_data


async def open_account(user):

    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["Wallet"]
    bank_amt = users[str(user.id)]["Bank"]



    em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.color.green)
    em.add_field(name = "Wallet balance", value = wallet_amt)
    em.add_field(name = "Bank balance", value = bank_amt)
    await ctx.send(embed = em)


@client.command()

    if str(user.id) in users:
        return false
    else:
        users[str(user.id)]["Wallet"] = 69
        users[str(user.id)]["Bank"] = 420

    with open("mainbank.json","w") as f:
        json.dump(user,f)
    return true



async def get_bank_data():
    with open("mainbank.json","r") as f:
        user = json.load(f)
    
    return users

client.run(DISCORD_TOKEN)