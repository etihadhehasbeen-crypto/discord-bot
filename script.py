import discord
import os
from flask import Flask
from threading import Thread

# ตั้งค่า Intents
intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!hello':
        await message.channel.send('สวัสดีครับ บอททำงานปกติแล้ว!')

# ระบบเว็บเซิร์ฟเวอร์จำลองเพื่อให้บอทออน 24 ชม. บน Render
app = Flask('')

@app.route('/')
def home():
    return "Bot is running!"

def run():
    app.run(host='0.0.0.0', port=8080)

def keep_alive():
    t = Thread(target=run)
    t.start()

if __name__ == "__main__":
    keep_alive()
    # แทนที่ 'YOUR_BOT_TOKEN' ด้วย Token ของบอทที่คุณคัดลอกมา
    client.run('YOUR_BOT_TOKEN')