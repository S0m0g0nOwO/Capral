import discord
from discord import utils
from discord.ext import commands
import random
from discord_slash import SlashCommand
from discord_slash import cog_ext

class slash(commands.Cog):
	def __init__(self, bot):
		self.bot = bot

def setup(client):
	client.add_cog(slash(client))
()