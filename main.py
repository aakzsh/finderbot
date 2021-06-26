import discord
from discord.ext import commands


bot = commands.Bot(command_prefix='$')
from discord.ext.commands import Bot

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def frooti(ctx):
    await ctx.send('go brr')

@bot.command()
async def cute(ctx):
    await ctx.send('no you ❤ :pepeOK: ')

@bot.command()
async def search(ctx):
    await ctx.send('send audio file or smth :PepeYikes:')

@bot.command()
async def attack(ctx):
    await ctx.send('🥺🥺🥺🥺🥺')





bot.run('add token here')