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
    if amount<bal[0]:
        await ctx.send("You don't have enough money")
        return
    if amount<0:
        await ctx.send("Amount must be above zero")
        return

    await update_bank(ctx.author,-1*amount)
    await update_bank(ctx.author,amount,"bank")

    await ctx.send(f"You deposited {amount} Tempest Tokens!")


@client.command()
async def send(ctx,member:discord.Member,amount = None):
    await open_account(ctx.author)    
    await open_account(member)    


    if amount == None:
        await ctx.send("Please enter the amount")
        return
    
    bal = await update_bank(ctx.author)
    if amount == "all":
        amount = bal[0]

    amount = int(amount)
    if amount>bal[0]:
        await ctx.send("You don't have enough money")
        return
    if amount<0:
        await ctx.send("Amount must be above zero")
        return

    await update_bank(ctx.author,-1*amount,"wallet")
    await update_bank(member,amount,"wallet")

    await ctx.send(f"You gave {amount} Tempest Tokens!")

@client.command()
async def rob(ctx,member:discord.Member):
    await open_account(ctx.author)    
    await open_account(member)    
    
    bal = await update_bank(member)

    if bal[0]<100:
        await ctx.send("It's not worth it!")
        return

    earnings = random.randrange(0, bal[0])

    await update_bank(ctx.author,earnings)
    await update_bank(member,-1*earnings)

    await ctx.send(f"You robbed {member} and got {earnings} Tempest Tokens!")


@client.command()
async def slots(ctx,amount = None):
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

    final = []
    for i in range(3):
        #a = random.choice(["X","0","Q","E"])
        a = random.choice(["E","E","E","E"])
        final.append(a)

    await ctx.send(str(final))
 
    if final[0] == final[1] and final[0] == final[2] and final[2] and final[1]:
        await update_bank(ctx.author,3*amount)
        await ctx.send("YOU WON THE JACKPOT!")
    elif final[0] == final[1] or final[0] == final[2] or final[2] == final[1]:
        await update_bank(ctx.author,1*amount)
        await ctx.send("You won!")
    else:
        await update_bank(ctx.author,-1*amount)
        await ctx.send("You lost!")

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