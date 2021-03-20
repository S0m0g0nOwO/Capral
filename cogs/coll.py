import discord
from discord.ext import commands
import random
import emoji

rp = ['Успешно', 'Не успешно']

class help(commands.Cog):

    def __init__(self, bot):
        self.bot = bot


    @commands.command()
    async def testreact(self, ctx, letters: list=None):
        if letters:
            try:
                for letter in letters:
                    emote = emoji.emojize(':regional_indicator_' + letter.lower() + ':', use_aliases = True)
                    await ctx.channel.last_message.add_reaction(emote)
            except:
                return await ctx.send("Эмодзи не существует!")
        else:
            return await ctx.send("Укажите реакции, которые хотите добавить к последнему сообщению!")

    @commands.command(
			  name = "баг",
  			brief = "Отправка бага",
  			usage = "к!баг <Описание бага>",
		)
    async def bag_report(self, ctx, *, bag):
        channel = commands.get_channel(807913454164770816
        )
        
        await channel.send(
              f'**{ctx.author}** отправил баг: {bag}'
        )

    @commands.command(aliases=['юзер'])
    async def user_info(ctx,member:discord.Member = None):
        if member == None:
            member = ctx.author
        if member.nick == None:
            nick = member.name
        else:
            nick = member.nick

        emb = discord.Embed(title = f'**Информация о {member.name}**',description = f'''
    Никнейм на сервере: {nick}
    Айди: {member.id}

    **Аватар:** [[клик]({member.avatar_url})]
    **Тег:** {member.discriminator}
    **Всего ролей:** {len(member.roles)}
    **Гл.Роль:** {member.top_role.name}
        
    **Дата создания аккаунта:** {str(member.created_at)[:16]}
    **Дата входа на сервер:** {str(member.joined_at)[:16]}
    ''')
        emb.set_thumbnail(url=member.avatar_url)
        await ctx.send(embed = emb)

    @commands.command(
				name = "идея",
  			brief = "Отправка идеи",
  			usage = "к!идея <Описание идеи>",
		)
    async def idea(self, ctx, *, idea=None):
        if idea is None:
            embed = discord.Embed(title="Ошибка", description="Укажите идею `>idea <idea>`", color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            member = await commands.fetch_user(user_id=745654846220271637)
            embed = discord.Embed(title="Новая Идея!", description=f"**Отправитель:\n**{ctx.author}\n**Айди:**\n{ctx.author.id}\n**Идея:**\n{idea}", color=discord.Color.green())
            await member.send(embed=embed)
            embed2 = discord.Embed(title="Успешно!", description=f"Идея была успешно отправлена создатаелю\n**Содержимое:**\n{idea}", color=discord.Color.green())
            await ctx.send(embed=embed2)

def setup(client):
    client.add_cog(help(client))