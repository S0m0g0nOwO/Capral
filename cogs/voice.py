import discord
from discord.ext import commands
from discord.utils import get

class Voice(commands.Cog):
	def __init__(self, client):
		self.bot = client

	@commands.command(
		aliases = ['лимит-2'])
	async def limit_users_2(self, ctx):
		await ctx.send(embed = discord.Embed(
			title = 'Успешно',
			description = f'В канале {ctx.author.voice.channel} я поставил лимит участников 2',
			color = discord.Color.from_rgb(110, 196, 86))
		)
		await ctx.author.voice.channel.edit(user_limit = 2)

	@commands.command(
		aliases = ['лимит-99'])
	async def limit_users_99(self, ctx):
		await ctx.send(embed = discord.Embed(
			title = 'Успешно',
			description = f'В канале {ctx.author.voice.channel} я поставил лимит участников 99',
			color = discord.Color.from_rgb(110, 196, 86))
		)
		await ctx.author.voice.channel.edit(user_limit = 99)

def setup(client):
	client.add_cog(Voice(client))
	print('[COGS] Voice.py загружен')