import os
import discord
from discord.ext import commands
import asyncio
from pythainlp.util import eng_to_thai, thai_to_eng, isthai

from myserver import server_on

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True
intents.members = True

bot = commands.Bot(command_prefix='/', intents=intents)

@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้ว! ชื่อบอท: {bot.user}")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return  # ไม่ให้บอทตอบตัวเอง

    text = message.content.strip()
    
    # ถ้าข้อความเป็นตัวอักษรอังกฤษล้วน และแปลงแล้วเป็นไทยได้
    if text.isascii():
        fixed_message_thai = eng_to_thai(text)
        if isthai(fixed_message_thai):  # ถ้าแปลงแล้วเป็นภาษาไทยที่อ่านรู้เรื่อง
            await message.reply(f"คุณหมายถึง: `{fixed_message_thai}` หรือเปล่า? 🤔")
            return

    # ถ้าข้อความเป็นภาษาไทยล้วน และแปลงแล้วเป็นอังกฤษได้
    if isthai(text):
        fixed_message_eng = thai_to_eng(text)
        if fixed_message_eng.isascii():  # ถ้าแปลงแล้วเป็นภาษาอังกฤษที่อ่านรู้เรื่อง
            await message.reply(f"คุณหมายถึง: `{fixed_message_eng}` หรือเปล่า? 🤔")
            return

    await bot.process_commands(message)  # ให้คำสั่งอื่น ๆ ทำงานได้ปกติ

server_on()
bot.run(os.getenv('TOKEN'))
