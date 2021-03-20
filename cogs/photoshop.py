import discord
from discord.ext import commands
import json
import aiohttp
import io
import random

rp = ['Успешно', 'Не успешно']

class photo(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    


    @commands.command(
      name = "радуга",
      aliases = ["gay"],
      usage = ['радуга (для работы прикрипите ихображение)'],
      brief = "радужный эффект на фото",
    )
    async def gay_comand(self, ctx):
            for file in ctx.message.attachments:
                url = file.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/canvas/gay?avatar={url}") as resp:
                        if resp.status != 200:
                            return await ctx.send("Не получилось скачать файл!")
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file = discord.File(data, "triger.png"))


    @commands.command(aliases = ['тригеред','триггер'])
    async def triger(self, ctx):
        if not ctx.message.attachments:
            await ctx.send("Не обноружил фотографию!")
        else:
            for file in ctx.message.attachments:
                url = file.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/canvas/triggered?avatar={url}") as resp:
                        if resp.status != 200:
                            return await ctx.send("Не получилось скачать файл!")
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file = discord.File(data, "triger.png"))

    @commands.command(aliases = ['стекло'])
    async def glass(self, ctx):
        if not ctx.message.attachments:
            await ctx.send("Не обноружил фотографию!")
        else:
            for file in ctx.message.attachments:
                url = file.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/canvas/glass?avatar={url}") as resp:
                        if resp.status != 200:
                            return await ctx.send("Не получилось скачать файл!")
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file = discord.File(data, "steklo.png"))
                    
    @commands.command(aliases = ['инверт'])
    async def invert(self, ctx):
        if not ctx.message.attachments:
            await ctx.send("Не обноружил фотографию!")
        else:
            for file in ctx.message.attachments:
                url = file.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/canvas/invert?avatar={url}") as resp:
                        if resp.status != 200:
                            return await ctx.send("Не получилось скачать файл!")
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file = discord.File(data, "invert.png"))
                    
    @commands.command(aliases = ['сепия'])
    async def sepia(self, ctx):
        if not ctx.message.attachments:
            await ctx.send("Не обноружил фотографию!")
        else:
            for file in ctx.message.attachments:
                url = file.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/canvas/sepia?avatar={url}") as resp:
                        if resp.status != 200:
                            return await ctx.send("Не получилось скачать файл!")
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file = discord.File(data, "sepia.png"))

    @commands.command(aliases = ['коммент', 'ютуб'])
    async def youtube_comment(self, ctx, comment):
        if not ctx.message.attachments:
            await ctx.send("Вы не отправили аватарку комментатора!")
        else:
            for file in ctx.message.attachments:
                url = file.url
                async with aiohttp.ClientSession() as session:
                    async with session.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={url}&comment={comment}&username={ctx.author.name}") as resp:
                        if resp.status != 200:
                            return await ctx.send("Не получилось скачать файл!")
                        data = io.BytesIO(await resp.read())
                        await ctx.send(file = discord.File(data, "comment.png"))
                       


def setup(client):
    client.add_cog(photo(client))