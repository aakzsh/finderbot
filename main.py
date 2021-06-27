from jina import Document
import numpy as np
import json
# d = Document()

# d.text = 'hello world'
# print(d4)

from discord.ext import commands
import requests


bot = commands.Bot(command_prefix='$')

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def attack(ctx):
    await ctx.send('🥺\nhelllllll-lo')

@bot.command()
async def search(ctx):
    attachment_url = ctx.message.attachments[0].url
    file_request = requests.get(attachment_url)
    d4 = Document(content=ctx.message.attachments[0].url)
    
    data = {
    'api_token': '<api token here>',
    'url': d4.uri,
    'return': 'apple_music,spotify',
    }
    result = requests.post('https://api.audd.io/', data=data)
    workpwease = json.loads(result.text)
    artist = workpwease['result']['artist']
    song = workpwease['result']['title']
    link = workpwease['result']['song_link']
    await ctx.send(song + ", by " + artist + ".  Here's the link to enjoy your music(without ad ofc, coz we aint no spotify)  " +link)

# channel.send(file=discord.File('my_file.png'))

bot.run('<bot token here>')
