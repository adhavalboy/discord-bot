import discord 
import os
import requests
import json


client = discord.Client()
def get_qoutes():
  response = requests.get("https://zenquotes.io/api/random")
  json_data=json.loads(response.text)
  quote=json_data[0]['q']
  return quote

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return 

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')
  
  if message.content.startswith('$motivate'):
    await message.channel.send(get_qoutes())

client.run(os.getenv('TOKEN'))

