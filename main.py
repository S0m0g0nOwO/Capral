import discord
from discord.ext import commands
from discord.utils import get
import os
import keep_alive
import requests
import aiohttp
from pymongo import MongoClient
import youtube_dl
import pyttsx3

client = commands.Bot(command_prefix="к!", intents = discord.Intents.all())
client.remove_command("help")

@client.event
async def on_ready():
    guilds = await client.fetch_guilds(limit = None).flatten()
    await client.change_presence(status = discord.Status.idle, activity= discord.Activity(name=f'за {len(guilds)} серверами.', type= discord.ActivityType.watching))

@client.event
async def on_guild_join(guild):
    guilds = await client.fetch_guilds(limit = None).flatten()
    await client.change_presence(status = discord.Status.idle, activity= discord.Activity(name=f'за {len(guilds)} серверами.', type= discord.ActivityType.watching))

@client.command()
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        engine = pyttsx3.init()
        engine.say('Привет, человечушки. Как жизнь на земле!?')
        engine.runAndWait()
 
@client.command()
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
    else:
        voice = await channel.connect()
 
@client.command()
async def play(ctx, url : str):
    song_there = os.path.isfile('song.mp3')
 
    try:
        if song_there:
            os.remove('song.mp3')
            print('[log] Старый файл удален')
    except PermissionError:
        print('[log] Не удалось удалить файл')
 
    await ctx.send('Пожалуйста ожидайте')
 
    voice = get(client.voice_clients, guild = ctx.guild)
 
    ydl_opts = {
        'format' : 'bestaudio/best',
        'postprocessors' : [{
            'key' : 'FFmpegExtractAudio',
            'preferredcodec' : 'mp3',
            'preferredquality' : '192'
        }],
    }
 
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('[log] Загружаю музыку...')
        ydl.download([url])
 
    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'[log] Переименовываю файл: {file}')
            os.rename(file, 'song.mp3')
 
    voice.play(discord.FFmpegPCMAudio('song.mp3'), after = lambda e: print(f'[log] {name}, музыка закончила свое проигрывание'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07
 
    song_name = name.rsplit('-', 2)
    await ctx.send(f'Сейчас проигрывает музыка: {song_name[0]}')

@client.command()
async def load(ctx, extension):
	if ctx.author.id == 745654846220271637:
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("Вы не разработчик бота...")


@client.command()
async def unload(ctx, extension):
	if ctx.author.id == 745654846220271637:
		client.unload_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("Вы не разработчик бота...")


@client.command()
async def reload(ctx, extension):
	if ctx.author.id == 745654846220271637:
		client.unload_extension(f"cogs.{extension}")
		client.load_extension(f"cogs.{extension}")
		await ctx.send("Cogs is loaded...")
	else:
		await ctx.send("Вы не разработчик бота...")


for filename in os.listdir("./cogs"):
	if filename.endswith(".py"):
		client.load_extension(f"cogs.{filename[:-3]}")

# Start the server
keep_alive.keep_alive()

# Finally, login the bot
client.run(os.environ.get('TOKEN'), bot=True, reconnect=True)
