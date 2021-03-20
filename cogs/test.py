import discord
from discord.ext import commands
import random
import emoji

rp = ['Успешно', 'Не успешно']

der = ['https://cdn.discordapp.com/attachments/772509291361206305/812755856893935686/2ee54ae4a271cd49302c8fc68329c458.jpg', 'https://cdn.discordapp.com/attachments/801412657474699277/818846408911880212/IMG-20210217-WA0057.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/818786517895741480/PicsArt_03-09-03.04.32.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/818563069734158387/PicsArt_03-08-12.46.13.png'
, 'https://cdn.discordapp.com/attachments/815915010496528394/818562925371457626/20210308_184355.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/818472701600595968/Adobe_20210307_201432.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/818472701248405534/Adobe_20210308_180137.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/816976334781153292/PicsArt_03-04-01.34.11.jpg'
, 'https://cdn.discordapp.com/attachments/815915010496528394/816780879904768040/IMG_20210304_020303.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/816763292424732722/IMG_20210226_163411_702.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/816742755728490496/PicsArt_03-04-12.41.18.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/816620033022230568/Adobe_20210303_153555.jpg'
, 'https://cdn.discordapp.com/attachments/815915010496528394/815915592941961216/PicsArt_02-18-03.16.18.jpg', 'https://cdn.discordapp.com/attachments/815915010496528394/815915592321073242/PicsArt_02-19-05.03.54.jpg']

class test(commands.Cog):
	def __init__(self, bot):
		self.bot = bot
	
	
	@commands.command()
	async def деррор(self, ctx):
	    ctx.send(random.choice(der))
	    


def setup(client):
	client.add_cog(test(client))
()