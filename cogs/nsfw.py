import discord
from discord.ext import commands
import json
import aiohttp
import io
import requests

class nsfw(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
        
        
    @commands.command(aliases=['ноги'])
    async def feet(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/feet")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW гиф 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


    @commands.command(aliases=['хентайгиф'])
    async def hentaigif(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW гиф 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
    
    @commands.command(aliases=['сиськи'])
    async def tits(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/tits")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW картинка 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
    
    @commands.command(aliases=['трап'])
    async def trap(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/trap")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW картинка 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
    
    @commands.command(aliases=['футунари'])
    async def futanari(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/futunari")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW картинка 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
    
    @commands.command(aliases=['сперма'])
    async def cum(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/cum")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW картинка 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command(aliases=['нсфваватар'])
    async def nsfwavatar(self, ctx): # b'\xfc'
        await ctx.message.delete()
        r = requests.get("https://nekos.life/api/v2/img/nsfw_avatar")
        res = r.json()
        em = discord.Embed(description='Рандомный NSFW аватар 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)
  
    


    

    @commands.command(aliases=['анал'])
    async def anal(self, ctx): # b'\xfc'
        r = requests.get("https://nekos.life/api/v2/img/anal")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW картинка 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)


    @commands.command(aliases=['хентай'])
    async def hentai(self, ctx): # b'\xfc'
        r = requests.get("https://nekos.life/api/v2/img/hentai")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW картинка 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

    @commands.command(aliases=['йифф'])
    async def yiff(self, ctx): # b'\xfc'
        r = requests.get("https://sheri.bot/api/yiff")
        res = r.json()
        em = discord.Embed(description='Рандомная NSFW картинка 🌊')
        em.set_image(url=res['url'])
        await ctx.send(embed=em)

def setup(client):
    client.add_cog(nsfw(client))