import discord
from discord.ext import commands
import random
import requests
from bs4 import BeautifulSoup
import wikipedia
from googletrans import Translator
import asyncio
import datetime
import io
import aiohttp
import json
from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
from discord import Spotify


class Funny(commands.Cog):
	def __init__(self, client):
		self.bot = client
		

	@commands.command()
	async def монетка(self, ctx):
		a = random.randint(1, 2)
		a = random.randint(1, 2)
		if a == 1:
			embed = discord.Embed(
				title = '**Орёл и решка**', 
				color = discord.Color.from_rgb(110, 196, 86))
			embed.add_field(
				name = 'Что выпало:', 
				value = '*Вам выпал* __**орёл**__')
			embed.set_thumbnail(
				url = 'https://i.gifer.com/ZXv0.gif')
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(
				title = '__**Орёл и решка**__', 
				color = discord.Color.from_rgb(110, 196, 86))
			embed.add_field(
				name = 'Что выпало:', 
				value = '*Вам выпала* __**решка**__')
			embed.set_thumbnail(
				url = 'https://i.gifer.com/ZXv0.gif')
			await ctx.send(embed=embed)

	@commands.command()
	async def сапёр(self, ctx, arg = None):
		await ctx.send(embed = discord.Embed(
			title = 'Пальцы не сломай',
			description = """
||1️⃣||||1️⃣||||0️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||
||||💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||💥||||💥||||1️⃣||||
||1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||3️⃣||||2️⃣||||1️⃣||||
||1️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||💥||||1️⃣||||0️⃣||||0️⃣||||
||||💥||||2️⃣||||💥||||1️⃣||||1️⃣||||💥||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||
||1️⃣||||2️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||||
||||💥||||💥||||1️⃣||||||||2️⃣||||3️⃣||||3️⃣||||💥||||2️⃣||||1️⃣||||
||2️⃣||||2️⃣||||1️⃣||||0️⃣||||1️⃣||||💥||||2️⃣||||1️⃣||||1️⃣||||0️⃣||||
||0️⃣||||0️⃣||||0️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||0️⃣||||0️⃣||||0️⃣||||
||1️⃣||||1️⃣||||0️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||
||||💥||||1️⃣||||1️⃣||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||💥||||💥||||1️⃣||||
||1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||||1️⃣||||2️⃣||||3️⃣||||2️⃣||||1️⃣||||
||1️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||2️⃣||||💥||||1️⃣||||0️⃣||||0️⃣||||
||||💥||||2️⃣||||💥||||1️⃣||||1️⃣||||💥||||2️⃣||||2️⃣||||1️⃣||||1️⃣||||
||1️⃣||||2️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||1️⃣||||💥||||1️⃣||||""",
			color = discord.Color.from_rgb(110, 196, 86)))	

	@commands.command()
	async def шар(self, ctx):
		answers = [
			"Несомненно!",
			"Можете быть уверены!",
			"Сомневаюсь в этом...",
			"Спроси позже...",
			"Наверно, лучше форматни диск C:",
			"На такие вопросы, я лучше промолчу"
		]
		embed = discord.Embed(
			title = "Магический шар",
			description = random.choice(answers),
			color = discord.Color.from_rgb(110, 196, 85)
		)
		await ctx.send(embed=embed)
		
	@commands.command(
		aliases = ['фейк-кик'])
	async def fake_kick(self, ctx, member: discord.Member = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите пользователя!',
				color = discord.Colour.red()))
		else:	   
			embed = discord.Embed(
				title = 'Кик!', 
				description = f'Администратор: {ctx.author.mention}, кикнул: {member.mention}!', 
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.send(embed=embed)

	@commands.command(
		aliases = ['фейк-бан'])
	async def fake_ban(self, ctx, member: discord.Member = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите пользователя!',
				color = discord.Colour.red()))
		else:               
			embed = discord.Embed(
				title = 'Бан!', 
				description = f'Администратор: {ctx.author.mention}, забанил: {member.mention}!', 
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.send(embed=embed)

	@commands.command(
		aliases = ['фейк-мьют'])
	async def fake_mute(self, ctx, member: discord.Member = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите пользователя!',
				color = discord.Colour.red()))
		else:               
			embed = discord.Embed(
				title = 'Мут!', 
				description = f'Администратор: {ctx.author.mention}, выдал мут: { member.mention }!', 
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.send(embed=embed)

	
	@commands.command()
	async def кнб(self, ctx, *, arg = None):
		a = random.randint(1, 2)
		sho = random.choice([1, 2, 3])
		if arg is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите чем вы будете атаковать (камень, ножницы, бумага)',
				color = discord.Colour.red()))
		elif sho == 1:
			await ctx.send(embed = discord.Embed(
				description = f'Ты выбрал {arg}, а бот Камень',
				color = discord.Color.from_rgb(110, 196, 86)))
			if arg == 'камень':
				await ctx.send(embed = discord.Embed(
					description = 'Нечья!',
					color = discord.Color.from_rgb(110, 196, 86)))
			elif arg == 'бумага':
				await ctx.send(
					description = 'Ты выиграл!', 
					color = discord.Color.from_rgb(110, 196, 86))
			elif arg == 'ножницы':
				await ctx.send(
					description = 'Ты проиграл!', 
					color = discord.Color.from_rgb(110, 196, 86))
		elif sho == 2:
			await ctx.send(embed = discord.Embed(
				description = f'Ты выбрал {arg}, а бот Ножницы',
				color = discord.Color.from_rgb(110, 196, 86)))
			if arg == 'камень':
				await ctx.send(embed = discord.Embed(
					description = 'Нечья!',
					color = discord.Color.from_rgb(110, 196, 86)))
			elif arg == 'бумага':
				await ctx.send(
					description = 'Ты выиграл!', 
					color = discord.Color.from_rgb(110, 196, 86))
			elif arg == 'ножницы':
				await ctx.send(
					description = 'Ты проиграл!', 
					color = discord.Color.from_rgb(110, 196, 86))
		elif sho == 3:
			await ctx.send(embed = discord.Embed(
				description = f'Ты выбрал {arg}, а бот Бумагу',
				color = discord.Color.from_rgb(110, 196, 86)))
			if arg == 'бумага':
				await ctx.send(embed = discord.Embed(
					description = 'Нечья!',
					color = discord.Color.from_rgb(110, 196, 86)))
			elif arg == 'ножницы':
				await ctx.send(
					description = 'Ты выиграл!', 
					color = discord.Color.from_rgb(110, 196, 86))
			elif arg == 'камень':
				await ctx.send(
					description = 'Ты проиграл!', 
					color = discord.Color.from_rgb(110, 196, 86))               

def setup(client):
	client.add_cog(Funny(client))
	print('[COGS] Funny.py Загружен!') 