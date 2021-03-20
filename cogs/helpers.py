import discord
from discord.ext import commands
import random
import json
import requests

rp = ['Успешно', 'Не успешно']

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        
    @commands.command()
    async def о(self, ctx):
      await ctx.send('<:py:819577942073409536>')

    
    @commands.command(aliases=['lottery', 'розыгрыш', 'конкурс'])
    async def giveaway(self, ctx, channel: discord.TextChannel=None, ids=None):
        if channel is None:
            embed = discord.Embed(title="Ошибка", description="Укажите канал сообщения `к!giveaway(розыгрыш) <channel> <id>`", color=discord.Color.red())
            await ctx.send(embed=embed)
        elif ids is None:
            embed = discord.Embed(title="Ошибка", description="Укажите айди сообщения `к!giveaway <channel> <id>`", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            try:
                try:
                    msg = await commands.get_channel(channel.id).fetch_message(int(ids))
                    users = await msg.reactions[0].users().flatten()
                    embed = discord.Embed(title="🎫 Лотерея", description=f"**Канал:** {msg.channel.mention}\n**Айди Сообщения:** {msg.id}\n**Ссылка на сообщение:** [Ссылка]({msg.jump_url})\n**Победитель:** {random.choice(users).mention}", color=discord.Color.green())
                    await ctx.send(embed = embed)
                except IndexError:
                    embed = discord.Embed(title="Ошибка", description="На указанном сообщении нету реакций!", color=discord.Color.red())
                    await ctx.send(embed=embed)
            except ValueError:
                embed = discord.Embed(title="Ошибка", description="Укажите нормальный айди сообщения", color=discord.Color.red())
                await ctx.send(embed=embed)
    
    @commands.command(aliases=['бот'])
    async def info(self, ctx):
      

            embed = discord.Embed(
                description="Префикс к!",
                color=0x00FF00
            )
            embed.set_author(
                name="Информация о боте"
            )
            embed.add_field(
                name="Владелец:",
                value="Лаки#7588",
                inline=True
            )
            embed.add_field(
                name="<:py:819577942073409536>Версия Python:",
                value="8.9.0" ,
                inline=True
            )
            embed.add_field(
                name="Префикс:",
                value="к!",
                inline=False
            )
            ret = requests.get('https://status.discordapp.com/index.json')
            rec = json.loads(ret.text)
            if rec['status']['description'] == "Все системы в рабочем состоянии":
                color = 0x00D800
            else:
                color = 0xAA00AA
            if rec["components"][0]["status"] == "operational":
                embed.add_field(name="API",value="Отлично",inline=True)
            else:
                embed.add_field(name="API",value='Не работает',inline=True)
            if rec["components"][1]["status"] == "operational":
                embed.add_field(name="Шлюз",value='Отлично',inline=True)
            else:
                embed.add_field(name="Шлюз",value='Не работает',inline=True)
            if rec["components"][2]["status"] == "operational":
                embed.add_field(name="CloudFlare",value='Отлично',inline=True)
            else:
                embed.add_field(name="CloudFlare",value='Не работает',inline=True)
            if rec["components"][3]["status"] == "operational":
                embed.add_field(name="Медиа прокси",value='Отлично',inline=True)
            else:
                embed.add_field(name="Шлюз",value='Не работает',inline=True)
            if rec["components"][3]["status"] == "operational":
                embed.add_field(name="Голосовые серверы",value='Отлично',inline=True)
            else:
                embed.add_field(name="Шлюз",value='Не работает',inline=True)
            
            embed.set_footer(text=f"CapralBot 2021")
            
            await ctx.send(embed=embed)
            

def setup(client):
    client.add_cog(help(client))
