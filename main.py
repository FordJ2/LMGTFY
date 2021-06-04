name = ('lmgtfy'.upper())
version = '2.0.0'

import asyncio
import discord
import time
from discord.ext import commands
from e import f

intents = discord.Intents().all()
client = commands.Bot(command_prefix = ["L;"])
client.remove_command('help')

@client.event
async def on_ready():
	print("Connected to Discord at " + time.ctime())
	perms = discord.Permissions(3072)
	print("Invite link: {}".format(discord.utils.oauth_url(client.user.id, perms)))

	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="you suffer | L;help"))
	print('\n:::\n')

def read(x):
	f = open("file.txt", "r")
	for line in f:
		if line.startswith(x):
			return(int(len(line)) - 1)
	f.close()

def write(x):
	with open("file.txt", "r+") as g:
		lines = g.readlines()
		for i, line in enumerate(lines):
			if line.startswith(x):
				lines[i] = lines[i].strip() + "e\n"	
		g.seek(0)
		for line in lines:
			g.write(line)
		g.close

@client.command()
async def invite(ctx):
	perms = discord.Permissions(3072)
	await ctx.send(f'<{discord.utils.oauth_url(client.user.id, perms)}>')

@client.command()
async def lmgtfy(ctx):
	await asyncio.sleep(0.25)
	await ctx.send(f"<https://lmgtfy.app/?q={((ctx.message.content[8:]).replace(' ', '+'))}>")
	write("1")

@client.command()
async def google(ctx):
	await asyncio.sleep(0.25)
	await ctx.send(f"<https://www.google.com/search?client=opera-gx&q={((ctx.message.content[8:]).replace(' ', '+'))}&sourceid=opera&ie=UTF-8&oe=UTF-8>")
	write("2")

@client.command()
async def graph(ctx):
	await asyncio.sleep(0.25)
	await ctx.send('<https://docs.google.com/spreadsheets/d/1fafaO0s5JgwLTRmf1QdIAT46viUXXObbgYnYzehY-DQ/edit#gid=0>')
	await asyncio.sleep(0.25)
	await ctx.send('<https://docs.google.com/spreadsheets/d/1TSbLiQl8XQp0t47r7iGOMf9qpQJtw04ViP-IV-pocLU/edit#gid=0>')
	write("3")

@client.command()
async def github(ctx):
	await asyncio.sleep(0.25)
	await ctx.send('<https://github.com/wncry>')
	write("4")

@client.command()
async def used(ctx):
	em = discord.Embed(title="Use of Commands", color=0x88dff1)
	em.add_field(name='LMGTFY', value=f"Used {read('1')} times")
	em.add_field(name='Google', value=f"Used {read('2')} times")
	em.add_field(name='Graph', value=f"Used {read('3')} times")
	em.add_field(name='GitHub', value=f"Used {read('4')} times")
	em.add_field(name='Help', value=f"Used {read('5')} times")
	em.add_field(name='Ping', value=f"Pinged {read('6')} times")
	em.set_footer(text="made by .wncry")
	await ctx.send(embed=em)

@client.group(invoke_without_command=True)
async def help(ctx):
	await asyncio.sleep(0.25)
	em = discord.Embed(title="Help Information", description="View help information for <@816651441925259326>", color=0x88dff1)
	em.set_thumbnail(url='https://cdn.discordapp.com/attachments/820990482519031830/848232722635554876/lmgtfy.png')
	em.add_field(name="LMGTFY", value="\nquickly answer a dumb question someone else has\n> `L;lmgtfy *the question someone else has*`\n", inline=False)
	em.add_field(name="Google", value="\nquckly answer a question you have\n> `L;google *the question you have*`\n", inline=False)
	em.add_field(name="GitHub", value="\nprovides a link to\n.wncry's GitHub\n> `L;github`")
	em.add_field(name="Invite", value="\ninvite the bot to\nyour server\n> `L;invite`")
	em.add_field(name="Graph", value="\nshow up to date CPU\nand GPU graphs\n> `L;graph`")
	em.set_footer(text="made by .wncry")
	await ctx.send(embed=em)
	write("5")

@client.listen('on_message')
async def ping(message):
	if message.author == client.user:
		return

	if client.user.mentioned_in(message):
		write("6")

f()
client.run('ODE2NjUxNDQxOTI1MjU5MzI2.YD-D7A.Nb-D8M8Vhadnv3zMTgplzW-rNIU')
