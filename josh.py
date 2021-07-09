import discord
from discord.ext import commands
from secrets import * 
import random
import json

client = commands.Bot(command_prefix = "++")


@client.event
async def on_ready():
    print("Ready")

@client.command()
async def balance(ctx):
    await open_account(ctx.author)
    user = ctx.author
    users = await get_bank_data()

    wallet_amt = users[str(user.id)]["wallet"]
    bank_amt = users[str(user.id)]["bank"]

    em = discord.Embed(title = f"{ctx.author.name}'s balance",color = discord.Color.green())
    em.add_field(name = "Wallet balance", value = wallet_amt)
    em.add_field(name = "Bank balance", value = bank_amt)
    await ctx.send(embed = em)


@client.command()
async def beg(ctx):
    await open_account(ctx.author)

    users = await get_bank_data()

    user = ctx.author

    earnings = random.randrange(101)

    await ctx.send(f"Someone gave you {earnings} Tempest Tokens!")


    users[str(user.id)]["wallet"] += earnings

    with open("mainbank.json","w") as f:
        json.dump(users,f)

@client.command()
async def  withdraw(ctx,amount = None):
    await open_account(ctx.author)    
    if amount == None:
        await ctx.send("Please enter the amount")
        return
    
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[1]:
        await ctx.send("You don't have enough money")
        return
    if amount<0:
        await ctx.send("Amount must be above zero")
        return

    await update_bank(ctx.author,amount)
    await update_bank(ctx.author,-1*amount,"bank")

    await ctx.send(f"You withdrew {amount} Tempest Tokens!")

@client.command()
async def  deposit(ctx,amount = None):
    await open_account(ctx.author)    
    if amount == None:
        await ctx.send("Please enter the amount")
        return
    
    bal = await update_bank(ctx.author)

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You don't have enough money")
        return
    if amount<0:
        await ctx.send("Amount must be above zero")
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"You depsited {amount} Tempest Tokens!")

async def open_account(user):

    users = await get_bank_data()

    if str(user.id) in users:
        return False
    else:
        users[str(user.id)] = {}
        users[str(user.id)]["wallet"] = 69
        users[str(user.id)]["bank"] = 420

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    return True

async def get_bank_data():
    with open("mainbank.json","r") as f:
        users = json.load(f)
    
    return users

async def update_bank(user,change = 0,mode = "wallet"):
    users = await get_bank_data()

    users[str(user.id)][mode] += change

    with open("mainbank.json","w") as f:
        json.dump(users,f)
    
    bal =  users[str(user.id)]["wallet"], users[str(user.id)]["bank"]
    return bal



client.run(DISCORD_TOKEN)