name = ('lmgtfy'.upper())
version = '1.0.2'
print(
	f"""
	{name} {version}
	Copyright (c) c:/#4617
	Licensed under the GNU AGPL 3.0
	"""
)

import discord
import time
import random
from discord.ext import commands
from keep_alive import keep_alive

client = commands.Bot(command_prefix = ["c;"])

@client.event
async def on_ready():
	print("Connected to Discord at " + time.ctime())
	perms = discord.Permissions(3072)
	print("Invite link: {}".format(discord.utils.oauth_url(client.user.id, perms)))

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
	'<https://bfy.tw/PFhi>'
	]

helpVar = 0
lmgtfyVar = 0
googleVar = 0
gpuVar = 0
cpuVar = 0
licenseVar = 0
pingVar = 0


@client.listen('on_message')
async def idk(message):
	msg = message.content.lower()
	if message.author == client.user:
		return

	if msg == 'help;':
		time.sleep(1)
		embedVar = discord.Embed(title="Help", description="LMGTFY helps you get what you need in a browser, but faster and simpler.", color=0x666699)
		embedVar.add_field(name="Action 1", value="\nTakes use of the resource <https://lmgtfy.app/#gsc.tab=0>\n> `lmgtfy; *the stupid question someone asked you*`", inline=False)
		embedVar.add_field(name="Action 2", value="\nCreates a direct link to google from discord using <https://www.google.ca/?gws_rd=ssl>\n> `google; *a question you have*`", inline=False)
		embedVar.add_field(name="Action 3", value="\nProvides a link to `c:\#4617`'s GitHub\n> `lmgtfy;github`", inline=False)
		embedVar.add_field(name="Action 4", value="\nProvides a link to a detailed graph of the price to preformance of either CPUs or GPUs\n> `lmgtfy;gpu`\n> `lmgtfy;cpu`", inline=False)
		embedVar.add_field(name="Action 5", value="\nDisplayes the License as well as other additional information\n> `license;`")
		await message.channel.send(embed=embedVar)
		global helpVar
		helpVar += helpVar + 1

	if msg.startswith('lmgtfy; '):
		time.sleep(1)
		await message.channel.send(f"<https://lmgtfy.app/?q={((message.content[8:]).replace(' ', '+'))}>")
		global lmgtfyVar
		lmgtfyVar += lmgtfyVar + 1

	if msg.startswith('google; '):
		await message.channel.send(f"<https://www.google.com/search?client=opera-gx&q={((message.content[8:]).replace(' ', '+'))}&sourceid=opera&ie=UTF-8&oe=UTF-8>")
		global googleVar
		googleVar += googleVar + 1

	if msg == ('license;'):
		time.sleep(1.25)
		embed2 = discord.Embed(title=f"{name} {version}", color=0x666699)
		embed2.add_field(name="\nCopyright (c) `c:/#4617`", value = "**Licensed under the GNU AGPL 3.0**")
		await message.channel.send(embed=embed2)
		global licenseVar
		licenseVar += licenseVar + 1

	if msg == ('lmgtfy;gpu'):
		time.sleep(1.25)
		await message.channel.send('https://docs.google.com/spreadsheets/d/1fafaO0s5JgwLTRmf1QdIAT46viUXXObbgYnYzehY-DQ/edit#gid=0')
		global gpuVar
		gpuVar += gpuVar + 1

	if msg == ('lmgtfy;cpu'):
		time.sleep(1.25)
		await message.channel.send('https://docs.google.com/spreadsheets/d/1TSbLiQl8XQp0t47r7iGOMf9qpQJtw04ViP-IV-pocLU/edit#gid=0')
		global cpuVar
		cpuVar += cpuVar + 1

	if msg == ('lmgtfy;github'):
		time.sleep(1.25)
		await message.channel.send('https://github.com/there-are-higher-beings')
		global gitVar
		gitVar += gitVar + 1

	if client.user.mentioned_in(message):
		time.sleep(1)
		await message.channel.send(random.choice(ping_responses))
		global pingVar
		pingVar += pingVar + 1

	if msg == ('used;'):
		embed3 = discord.Embed(title="Use of Commands", color=0x666699)
		embed3.add_field(name='Help', value=f"Used {helpVar} times")
		embed3.add_field(name='License', value=f"Seen {licenseVar} times")
		embed3.add_field(name='Ping', value=f"Pinged {pingVar} times")
		embed3.add_field(name='LMGTFY', value=f"Used {lmgtfyVar} times")
		embed3.add_field(name='Google', value=f"Used {googleVar} times")
		embed3.add_field(name='GitHub', value=f"Used {gitVar} times")
		embed3.add_field(name='GPU', value=f"Used {gpuVar} times")
		embed3.add_field(name='CPU', value=f"Used {cpuVar} times")
		embed3.add_field(name='.', value='.')
		await message.channel.send(embed=embed3)

client.run('TOKEN')
