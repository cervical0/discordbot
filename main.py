import os
import discord
import requests
import json
import random
from dotenv import load_dotenv
from replit import db
load_dotenv()
TOKEN = os.getenv('SECRET')
client = discord.Client()

sad_words = ["sad", "depressing", "upset", "stressed"]
starter_encouragements = [
  "Cheer up!"
  " It's going to be alright."
  " Don't worry, you are a great person!"
]
if "responding" not in db.keys():
  db["responding"] = True

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

prefix = '<'    
@client.event

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith(prefix + "delete"):
   await message.channel.purge(limit=10)

  msg = message.content

  if msg.startswith('<inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if db["responding"]:
    options = starter_encouragements
    if "encouragements" in db.keys():
      options = options + db["encouragements"]
  
  if any(word in msg for word in sad_words):
    await message.channel.send(random.choice(options))

  if message.author == client.user:
        return

  if message.content.startswith('<hello'):
        await message.channel.send('Hello!')

  if message.content.startswith('<desc'):
        await message.channel.send('Info Bot: the multi-purpose bot that suits many, if not all, of your server-related needs. It purges messages, and gives you information on your school. Want to apply? Do the application command and you will receive a resource for apps. Need the portal link? Type the command for so and get the invite! Created by Adeline N, student at MT, corg#3814.')
        
  if message.content.startswith('<bye'):
        await message.channel.send('goodbye.')
  
  if message.content.startswith('<application'):
        await message.channel.send('Check #staff-apps in the You category, or click this link https://docs.google.com/forms/d/1KGdhk0n-U2OKV_QemiZr83KkuKnhgmwxhdpILE2wOi8/edit.')
     
  if message.content.startswith('<help'):
        await message.channel.send('If you are looking for Project Meet VCs, scroll all the way down to #Project-Meet. If you are looking for staff application info, go to #staff-apps in the You category. If there is something else you need help with, try the prefix + the second help command.')


  if message.content.startswith('<2help'):
        await message.channel.send('If you are an MT student, any important updates will be posted in #announcement , and any other information will be posted in #gen. If there is something else you need try the prefix + the third help command.')


  if message.content.startswith('<3help'):
        await message.channel.send('If you are looking for a server invite, use this link: https://discord.gg/C6vMgqPj . If the link expires or if you need any further assistance then please contact a staff member')
  if message.content.startswith('<cmds'):

         await message.channel.send('Here is a list of commands for the bot: <help <2help <3help <application <hello <bye <bruh <inspire <delete')

  if message.content.startswith('<play'):
    await message.channel.send('Give me a number from 1-20.')



client.run(TOKEN)