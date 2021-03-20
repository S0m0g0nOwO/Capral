import discord
from discord.ext import commands
import asyncio
import random
import datetime
from discord import Embed

class moderation(commands.Cog):
	def __init__(self, client):
		self.bot = client
	
	@commands.command(
		aliases = ['anti-crush'])
	async def anti_crush(self, ctx):
		await ctx.send('Анти-краш включен')
	
	@commands.command()
	@commands.has_permissions(manage_messages = True)
	async def очистить(self, ctx, amount: int = None):
		if amount is None:
			pass
		else:
			amount1 = amount + 1

			dead = await ctx.channel.purge(limit = amount1)
			embed = discord.Embed(
				title = 'Удачно!', 
				description = f'{ctx.author.mention}, удачно удалил сообщения!\nКоличество: {len(dead)}!', 
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.channel.send(embed=embed)
			await asyncio.sleep(2)
			await ctx.channel.purge(limit = 1)

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def кик(self, ctx, member: discord.Member, *, reason = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}**, укажите пользователя!',
				color = discord.Colour.red()))
		elif reason is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}**, укажите причину!',
				color = discord.Colour.red()))
		else:
			embed = discord.Embed(
				title = 'Успешно', 
				description = f'Администратор: ``{ ctx.author.name }``\nКикнул пользователя: { member.mention },\nПричина: {reason}!', 
				color = discord.Color.from_rgb(110, 196, 86))
			await member.send(f'**{member.mention}, вы были кикнуты с сервера: {ctx.guild.name}\nАдминистратор: {ctx.author.name}\nПричина: {reason}**')
			await member.kick(reason=reason)
			await ctx.send(embed=embed)

	@commands.command()
	@commands.has_permissions(administrator = True)
	async def словмод(self, ctx, delay:int = None):
		if delay == None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.mention}** укажите время!',
				color = discord.Colour.red()))
			return
		if delay > 21600:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.mention}** нельзя ставить лимит на 21600(6ч)!',
				color = discord.Colour.red()))
			return
		await ctx.channel.edit(slowmode_delay = delay)
		await ctx.send(embed = discord.Embed(
			title = 'Успешно',
			description = f'{ctx.author.mention} поставил лимит словмод на {delay} секунд',
			color = discord.Color.from_rgb(110, 196, 86)))


	
	@commands.command()
	@commands.has_permissions(administrator = True)
	async def бан(self, ctx, *, member: discord.Member, reason = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.metion}**, укажите пользователя!',
				color = discord.Colour.red()))
		elif reason is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.mention}**, укажите причину!',
				color = discord.Colour.red()))
		else:
			embed = discord.Embed(
				title = 'Успешно', 
				description = f'Администратор: {ctx.author.mention}\n Забанил пользователя: {member.mention}\nПричина: {reason}', 
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.channel.purge( limit = 1 )
			await member.send(f'{member.mention}, вы были забанены на всегда!\nСервер: {ctx.guild.name}\nАдминистратор: {ctx.author.name}\nПричина: {reason}')
			await member.ban(reason=reason)
			await ctx.send(embed=embed)
		

	@commands.command(
		aliases = ['выдать-роль'])
	@commands.has_permissions(administrator = True)
	async def give_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите пользователя"',
				color = discord.Colour.red()))
		elif ctx.author == member:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** ты не можешь выдать роль самому себе',
				color = discord.Colour.red()))
		elif role is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите роль!',
				color = discord.Colour.red()))
		else:
			await member.add_roles(role)
			embed = discord.Embed(
				title = '**Успешно!**', 
				description = f'**Администратор {ctx.author.mention} выдал роль пользователю {member.mention}\n({role.mention})**', 
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.send(embed=embed)

	@commands.command(
		aliases = ['снять-роль'])
	@commands.has_permissions(administrator = True)
	async def remove_role(self, ctx, member: discord.Member = None, role: discord.Role = None):
		if member is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите пользователя"',
				color = discord.Colour.red()))
		elif ctx.author == member:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** самому себе выдать роль ты не сможешь!',
				color = discord.Colour.red()))
		elif role is None:
			await ctx.send(embed = discord.Embed(
				description = f':x:**{ctx.author.name}** укажите роль!',
				color = discord.Colour.red()))
		else:
			await member.remove_roles(role)
			embed = discord.Embed(
				title = '**Успешно!**', 
				description = f'**Администратор {ctx.author.mention} забрал роль у пользователю {member.mention}\n ({role.mention})**', 
				color = discord.Color.from_rgb(110, 196, 86))
			await ctx.send(embed=embed)

					

def setup(client):
	client.add_cog(moderation(client))
	print('[COGS] Moderation.py загружена!')