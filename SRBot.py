import discord
from discord.ext import commands

token = 'NzMyNzQ5MTkzNjU5MDIzNDQw.Xw5IAw.aREda8sIid9nQ221FX9nvr8Y-Jg'

client = commands.Bot(command_prefix='.')

@client.event
async def on_ready():
    print('Bot is ready')


# @client.event
# async def on_member_join(member):
#     print(f'{member} has joined')


# @client.event
# async def on_member_remove(member):
#     print(f'{member} has left')


@client.command()
async def ping(ctx):
    await ctx.send('pong!')


@client.command()
async def clear(ctx, ammount=5):
    await ctx.channel.purge(limit=ammount)


@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used')


@client.command()
async def sr(ctx, *, tickers):
    tickers = tickers.split()
    await ctx.send(f' you passed {len(tickers)} ticker/s, {tickers}')


client.run(token)