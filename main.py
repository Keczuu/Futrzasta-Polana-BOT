import discord
from discord.ext import commands
import os
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
id_kanalu = int(os.getenv('ID_KANALU'))

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'Bot is ready. Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(id_kanalu)

    if channel is not None:
        licznik_osob = sum(1 for m in member.guild.members if not m.bot)

        embed = discord.Embed(
            title=":wave: | :paw_prints: ***Futrzasta Oaza Wita!!!***",
            description=f"{member.mention} mamy nadzieję że odnajdziesz się wśród nas!\n**Pamietaj o weryfikacji!**",
            color=discord.Color.blue()
        )

        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Jestes naszym {licznik_osob} czlonkiem!")

        await channel.send(embed=embed)
    else:
        print(f"Kanal o id {id_kanalu} nie zostal znaleziony")

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(id_kanalu)

    if channel is not None:
        licznik_osob = sum(1 for m in member.guild.members if not m.bot)
        embed = discord.Embed(
            title=":wave: | **Żegnaj**",
            description=f"**{member.name}** właśnie nas opuścił\nBędziemy tęsknić",
            color=discord.Color.red()
        )
        
        embed.set_thumbnail(url=member.avatar.url)
        embed.set_footer(text=f"Pozostało {licznik_osob} użytkowników...")
        
        await channel.send(embed=embed)
    else:
        print(f"Kanal o id {id_kanalu} nie zostal znaleziony")

bot.run(token)
