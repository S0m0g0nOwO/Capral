from bs4 import BeautifulSoup
from discord.ext import commands, tasks
from itertools import cycle
from discord import Spotify, Embed, Role, Color
from datetime import datetime
from requests import get
import io
import aiohttp
import datetime
import discord
import json
import random
import requests
import wikipedia
import asyncio
import os
from Cybernator import Paginator as pag
from PIL import Image, ImageFont,ImageDraw
import io
from discord.utils import get
from pymongo import MongoClient

class Information(commands.Cog):
	def __init__(self, sadness):
		self.sadness = sadness

	@commands.command(
		aliases = ['комент'])
	async def add_comment(self, ctx, *, comment):
		if not ctx.message.attachments:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.mention}** укажи аватарку комментария',
				color = discord.Colour.red()
			))
		if comment is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.mention}** укажи комментарий',
				color = discord.Colour.red()
			))			
		else:
			for file in ctx.message.attachments:
				url = file.url
				async with aiohttp.ClientSession() as session:
					async with session.get(f"https://some-random-api.ml/canvas/youtube-comment?avatar={url}&comment={comment}&username={ctx.author.name}") as resp:
						if resp.status != 200:
							return await ctx.send("Не получилось скачать файл!")
						data = io.BytesIO(await resp.read())
						await ctx.send(file = discord.File(data, "comment.png"))


	@commands.command(
		aliases = ['инфо-роль'])
	async def info_role(self, ctx, role: discord.Role=None):
		date = role.created_at
		dates = date.strftime('%d.%m.%Y')
		if role is None:
			await ctx.send(embed=discord.Embed(
				title="Информация о роли",
				description="Вы не указали роль!",
				colour=discord.Color.red()))
		else:
			try:
				guild = ctx.guild
				embed = discord.Embed(
					title = 'Информация о роли {}'.format(role.name),
					color = discord.Color.from_rgb(110, 196, 86))
				embed.add_field(
					name='Роль создана',
					value='{}'.format(dates)
					)
				embed.add_field(
					name='Название роли', 
					value=role.name, 
					inline=False)
				embed.add_field(
					name='Айди роли', 
					value=role.id, 
					inline=False)
				embed.add_field(
					name="Количество пользователей с этой ролью",
					value=len(role.members),
					inline=False)
				if len(role.members) <= 30:
					embe.add_field(
						name = "Пользователи с этой ролью",
						value = ", ".join([member.mention for member in role.members]),
						inline = False)

				embed.add_field(
					name='Позиция роли', 
					value=role.position)
				await ctx.send(embed=emb)
			except:
				await ctx.send(
					embed = discord.Embed(
						title="Информация о роли",
						description="Упс, похоже что-то пошло не так",
						colour=discord.Color.red()
						)
					)	                    

	@commands.command()
	async def аватар(self, ctx, member: discord.Member = None):
		if member is None:
			embed = discord.Embed(
				title = f"Аватар пользователя {ctx.author}",
				color = discord.Color.from_rgb(110, 196, 86))
			embed.set_image(
				url=ctx.author.avatar_url)		
			await ctx.send(embed=embed)
		else:
			embed = discord.Embed(
				title = f"Аватар пользователя {member.name}",
				color = discord.Color.from_rgb(110, 196, 86))
			embed.set_image(
				url=member.avatar_url)		
			await ctx.send(embed=embed)			


	@commands.command()
	async def ping(self, ctx):
		ping = self.sadness.latency
		ping_emoji = "🟩🔳🔳🔳🔳"
		
		ping_list = [
			{"ping": 0.10000000000000000, "emoji": "🟧🟩🔳🔳🔳"},
			{"ping": 0.15000000000000000, "emoji": "🟥🟧🟩🔳🔳"},
			{"ping": 0.20000000000000000, "emoji": "🟥🟥🟧🟩🔳"},
			{"ping": 0.25000000000000000, "emoji": "🟥🟥🟥🟧🟩"},
			{"ping": 0.30000000000000000, "emoji": "🟥🟥🟥🟥🟧"},
			{"ping": 0.35000000000000000, "emoji": "🟥🟥🟥🟥🟥"}]
		
		for ping_one in ping_list:
			if ping > ping_one["ping"]:
				ping_emoji = ping_one["emoji"]
				break

		message = await ctx.send("Пожалуйста, подождите. . .")
		embed = Embed(
			title="Понг!",
			color=discord.Color.from_rgb(110,196,86)
		)		
		embed.add_field(
			name="Пинг бота",
			value=f"{ping * 1000:.0f}mc"
		)
	
		await message.edit(embed=embed)

	@commands.command()
	async def trush(self,ctx,member:discord.Member = None):
		if member == None:
			member = ctx.author
		url = str(member.avatar_url)[:-10]
		url = requests.get(url,stream = True)
		avatar = Image.open(io.BytesIO(url.content))
		trash = Image.open('trash.png')
		trash = trash.convert('RGBA')
		avatar = avatar.convert('RGBA')
		avatar = avatar.resize((500,500))
		mask = Image.new('L',(1500,1500),0)
		draw = ImageDraw.Draw(mask)
		draw.ellipse((0,0) + (1500,1500),fill = 255)
		mask = mask.resize((500,500))
		avatar.putalpha(mask)
		trash = trash.resize((1000,1000))
		trash.paste(avatar,(155,280,655,780),avatar)
		_buffer = io.BytesIO()
		trash.save(_buffer,"png")
		_buffer.seek(0)
		await ctx.send(file = discord.File(fp = _buffer,filename = f'{member.name}trash.png'))

	@commands.command(
		aliases = ['инфо-эмоджи'])
	async def emoji_info(self, ctx, emoji: discord.Emoji = None):
		if emoji is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** введите эмодзи',
				color = discord.Colour.red()))
		else:	
			embed = discord.Embed(
				description = f"[Эмодзи]({emoji.url}) сервера {emoji}",
				color = discord.Color.from_rgb(110, 196, 86))
			embed.add_field(
				name = "Имя:", 
				value = f"`{emoji.name}`")
			embed.add_field(
				name = "‎‎‎‎", 
				value = "‎‎‎‎")
			embed.add_field(
				name = "Время добавления:", 
				value = f"`{emoji.created_at}`")
			embed.add_field(
				name = "ID эмодзи:", 
				value = f"`{emoji.id}`")
			embed.add_field(
				name = "‎‎‎‎", 
				value = "‎‎‎‎")
			embed.set_thumbnail(
				url = f"{emoji.url}")
			await ctx.send(embed=embed)

	@commands.command()
	async def updates(self, ctx):
		embed = discord.Embed(
			title = '**1.0**', 
			description = '**Была отключена MongoDB(времено)!**', 
			color = discord.Color.from_rgb(110, 196, 86))
		embed1 = discord.Embed(
			title = '**2.0**', 
			description = '**Началось исправление/добавление команд !**', 
			color = discord.Color.from_rgb(110, 196, 86))
		embed2 = discord.Embed(
			title = '**3.0**', 
			description = '**Добавяются обновлённые команды модерации **', 
			color = discord.Color.from_rgb(110, 196, 86))
		embed3 = discord.Embed(
			title = '**4.0**', 
			description = '**Добавлена новая система информации**',
			color = discord.Color.from_rgb(110, 196, 86))
		embed4 = discord.Embed(
			title = '**5.0**', 
			description = '**Временное удаление NSFW команд**',
			color = discord.Color.from_rgb(110, 196, 86))
		embeds = [embed1, embed2, embed3, embed4]
		message = await ctx.send(embed = embed)
		page = pag(self.sadness, message, only = ctx.author, use_more = False, embeds = embeds)
		await page.start()

	@commands.command(
		aliases = ['сервер-инфо'])
	async def server_info(self, ctx):
		members = ctx.guild.members
		online = len(list(filter(lambda x: x.status == discord.Status.online, members)))
		offline = len(list(filter(lambda x: x.status == discord.Status.offline, members)))
		idle = len(list(filter(lambda x: x.status == discord.Status.idle, members)))
		dnd = len(list(filter(lambda x: x.status == discord.Status.dnd, members)))
		allchannels = len(ctx.guild.channels)
		allvoice = len(ctx.guild.voice_channels)
		alltext = len(ctx.guild.text_channels)
		allroles = len(ctx.guild.roles)
		embed = discord.Embed(
			title=f"{ctx.guild.name}", 
			color = discord.Color.from_rgb(110, 196, 86), 
			timestamp=ctx.message.created_at)
		embed.description=(
			f"<a:animmoder:819577802839949343> Время создания севрера: **{ctx.guild.created_at.strftime('%A, %b %#d %Y')}**\n\n"
			f" <:BugHunter:819577777744248832> Регион **{ctx.guild.region}\n\nСоздатель сервера **{ctx.guild.owner}**\n\n"
			f" <:discord_bot_dev:819577940755873882> Ботов на сервере: **{len([m for m in members if m.bot])}**\n\n"
			f" <:online:819577924293754930> Онлайн: **{online}**\n\n" f" <:offline:819577832501280800> Оффлайн: **{offline}**\n\n" f" <:idle:819578201490849832> Не активны: **{idle}**\n\n"
			f" <:DND:819578201419808850> Не беспокоить: **{dnd}**\n\n"
			f" <:BugHunterLvl2:819577803192008724> Уровень верификации: **{ctx.guild.verification_level}**\n\n"
			f" <:channels:819597349079875615> Всего каналов: **{allchannels}**\n\n"
			f" <:voice_emoji:819578290784043078> Голосовых каналов: **{allvoice}**\n\n"
			f" :keyboard: Текстовых каналов: **{alltext}**\n\n"
			f" <:ytheart:819577803145084938> Всего ролей: **{allroles}**\n\n"
			f" <:members:819597349172150332> Людей на сервере **{ctx.guild.member_count}\n\n"

		)
		embed.set_thumbnail(
			url=ctx.guild.icon_url)
		embed.set_footer(
			text=f"ID: {ctx.guild.id}")
		embed.set_footer(
			text=f"ID Пользователя: {ctx.author.id}")
		await ctx.send(embed=embed)

	@commands.command(
		aliases = ['бот-инфо'])
	async def infobot(self, ctx):
		embed = discord.Embed(
			title = '**Информация обо мне**',
			description = """
Меня зовут Capral\nЯ много функциональный и русский бот\nна платформе Discord созданный для множества серверов.\nЯ имею множество разных команд и функций. Работаю всегда\nЕсли хочешь узнать мои возможности пропиши к!хелп""",
			color = discord.Color.from_rgb(110, 196, 86))
		embed.add_field(
			name = '**Разработчик**',
			value = '<@745654846220271637>')
		embed.add_field(
			name = '**Бот написан на**',
			value = 'Python 3.8.6')
		embed.add_field(
			name = '**База данных бота**',
			value = 'MongoDB')
		embed.add_field(
			name = '**Сервер поддержки**',
			value = 'https://discord.gg/FvMM79R6XT')
		embed.set_footer(
			text = 'Все права защищены | by  Лаки#7588',)
		await ctx.send(embed=embed)

	@commands.command()
	async def профиль(self, ctx, member:discord.Member=None):
		if member is None:
			embed = Embed(
				title=f"Информация о пользователе {ctx.author.name}",
				color=discord.Color.from_rgb(110, 196, 86)
			)
			embed.set_thumbnail(
				url=ctx.author.avatar_url)
			stik = {
				"dnd":"<:DND:819578201419808850>Не беспокоить",
				"idle":"<:idle:819578201490849832>Не активен",
				"offline":"<:offline:819577832501280800> Оффлайн",
				"online":"<:online:819577924293754930> Онлайн"
			}
			embed.add_field(
				name="Статус пользователя",
				value=stik[str(ctx.author.status)],
				inline=False
				)
			embed.add_field(
				name="Имя на сервере",
				value=str(ctx.author.display_name)
				)
			embed.add_field(
				name="Даты/входа/регистрации",
				value=f"""Присоединился: {ctx.author.joined_at}
	Дата создания: {ctx.author.created_at}""",
				inline=False)
			embed.add_field(
				name="Главная роль", 
				value=f"{ctx.author.top_role.mention}")
			embed.add_field(
				name="Всего ролей",
				value=len(ctx.author.roles)
			)
			await ctx.send(embed=embed)
		else:
			embed = Embed(
				title=f"Информация о пользователе {member.name}",
				color=discord.Color.from_rgb(110, 196, 86)
			)
			embed.set_thumbnail(
				url=ctx.author.avatar_url)
			stik = {
				"dnd":"<:DND:819578201419808850>Не беспокоить",
				"idle":"<:idle:819578201490849832>Не активен",
				"offline":"<:offline:819577832501280800>Оффлайн",
				"online":"<:online:819577924293754930>Онлайн"
			}
			embed.add_field(
				name="Статус пользователя",
				value=stik[str(member.status)],
				inline=False
				)
			embed.add_field(
				name="Имя на сервере",
				value=str(member.display_name)
				)
			embed.add_field(
				name="Даты/входа/регистрации",
				value=f"""Присоединился: {member.joined_at}
	Создал аккаунт: {member.created_at}""",
				inline=False)
			embed.add_field(
				name="Главная роль", 
				value=f"{member.top_role.mention}")
			embed.add_field(
				name="Всего ролей",
				value=len(member.roles)
			)
			await ctx.send(embed=embed)					

	@commands.command()
	async def wiki(self, ctx, *, text=None):
		if text is None:
			await ctx.send(
				embed=discord.Embed(
					title="Найти в википедии",
					description="Вы не указали запрос который хотите найти",
					color=discord.Color.from_rgb(110, 196, 86)
					)
				)
		else:
			try:
				wikipedia.set_lang("ru")
				new_page = wikipedia.page(text)
				summ = wikipedia.summary(text)
				embed = Embed(
					title=new_page.title,
					description=summ,
					color=discord.Color.from_rgb(110, 196, 86)
				 )
				embed.set_author(
					name='Больше информации тут!', 
					url= new_page.url, 
					icon_url= 'https://upload.wikimedia.org/wikipedia/commons/thumb/8/80/Wikipedia-logo-v2.svg/1200px-Wikipedia-logo-v2.svg.png%27')

				await ctx.send(embed=embed)
			except:
				await ctx.send(
					embed=Embed(
						title="Найти в википедии",
						description="Мы не смогли найти ничего по вашему запросу :(",
						color=discord.Color.from_rgb(110, 196, 86)
						)
					)

	@commands.command(
		aliases=['covid-19'])
	async def covid_19(self, ctx):
		
		Corona = 'https://xn--80aesfpebagmfblc0a.xn--p1ai/#operational-data'
		headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.149 Safari/537.36'}

		full_page = requests.get(Corona, headers=headers)
		soup = BeautifulSoup(full_page.content, 'html.parser')

		convert = soup.findAll("div", {"class": "cv-countdown__item-value"})
		hz = soup.find("div",{"class":"cv-banner__description"})

		heads = []
		for i in convert:
			heads.append(i.string)

		embed = discord.Embed(
			title=f"Данные по короновирусу. {hz.string}", 
			color=discord.Color.from_rgb(110, 196, 86))
		embed.add_field(
			name="Заболело: ", 
			value=heads[1], 
			inline=False)
		embed.add_field(
			name="Выздоровело: ", 
			value=heads[3], 
			inline=False)
		embed.add_field(
			name="Умерло: ", 
			value=heads[4], 
			inline=False)
		embed.set_thumbnail(
			url='https://upload.wikimedia.org/wikipedia/commons/thumb/8/8b/Biohazard_orange.svg/1200px-Biohazard_orange.svg.png')
		await ctx.send(embed=embed)

	@commands.command(
		aliases = ['создать-роль'])
	@commands.is_owner()
	async def create_role(self, ctx, name = None, *, perm = None):
		if name is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите название роли!',
				color = discord.Colour.red()))
		elif perm is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** введите 1, если хотите чтобы люди могли писать сообщение с этой ролью, введите 2, если не хотите чтобы люди могли писать сообщение с этой ролью',
				color = discord.Colour.red()))
		else:
			role = await ctx.guild.create_role(name = name)

			if perm == "1":
				pass
			elif perm == "0":
				role.edit(send_messages = False, send_tts_messages = False)

			await ctx.send(f"Роль {name}, была удачно создана!")


			overwrite = discord.PermissionOverwrite()
			overwrite.send_messages = False
			for chat in ctx.guild.channels:
				await chat.set_permissions(role, overwrite = overwrite )

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def news(self, ctx, *, arg = None, argg = None):
		if not arg:
			await ctx.send('заголовок укажи ля')
		elif not argg:
			await ctx.send('заголовок укажи ля')
		else:	
			embed = discord.Embed(
				title = f'{arg}',
				description = f'{argg}',
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.send(embed=embed)		

def setup(sadness):
	sadness.add_cog(Information(sadness))
	print('[COGS] Information.py Загружен!')