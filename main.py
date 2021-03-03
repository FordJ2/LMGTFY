name = ('lmgtfy'.upper())

print(
	f"""
	{name} 1.0.0
	Copyright (c) there-are-higher-beings
	Licensed under the GNU AGPL 3.0
	"""
)

import asyncio
import discord
import time
import random
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = [";"])

@client.event
async def on_ready():
	print("Connected to Discord at " + time.ctime())
	perms = discord.Permissions(3072)
	print("Invite link: {}".format(discord.utils.oauth_url(client.user.id, perms)))

	'''
	#Setting `Playing ` status
	(name="a game")
	# Setting `Streaming ` status
	(name="My Stream", url=my_twitch_url)
	# Setting `Listening ` status
	(type=discord.ActivityType.listening, name="a song")
	# Setting `Watching ` status
	(type=discord.ActivityType.watching, name="a movie")
	'''

	await client.change_presence(status=discord.Status.online, activity=discord.Activity(type=discord.ActivityType.watching, name="you suffer"))
	print('')
	print(':::')
	print('')

ping_responses = [
	'stop',
	'stap',
	'really?',
	'can you not?',
	'bruh wth',
	'i will kick you',
	'https://bfy.tw/PFhi'
	]

@client.listen('on_message')
async def idk(message):
	if message.author == client.user:
		return

	msg = message.content.lower()

	if msg == 'help;':
		asyncio.sleep(0.5)
		await message.channel.send('`lmgtfy; *whatever question you have been bothered with*`')

	if msg.startswith('lmgtfy; '):
		asyncio.sleep(0.5)
		await message.channel.send(f"https://lmgtfy.app/?q={((message.content[8:]).replace(' ', '+'))}")
	
	if msg.startswith('lmgtfy;'):
		asyncio.sleep(0.5)
		await message.channel.send(f"https://lmgtfy.app/?q={((message.content[7:]).replace(' ', '+'))}")

	if client.user.mentioned_in(message):
		asyncio.sleep(0.5)
		await message.channel.send(random.choice(ping_responses))

#https://lmgtfy.app/?q=xxx

keep_alive()

TOKEN = ''
client.run(TOKEN)
