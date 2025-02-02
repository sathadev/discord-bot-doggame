import os
import discord
from discord.ext import commands
from discord import app_commands
from dotenv import load_dotenv

from myserver import server_on  # ตรวจสอบว่าฟังก์ชันนี้ทำงานได้จริง

# โหลดตัวแปรจากไฟล์ .env
load_dotenv()

TOKEN = os.getenv("TOKEN")

# กำหนด intents ให้บอทสามารถอ่านข้อความและส่งข้อความได้
intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # จำเป็นสำหรับการอ่านข้อความ

# สร้าง instance ของบอท
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้ว! ชื่อบอท: {bot.user}")

@bot.command()
async def ชวนเล่น(ctx):
    await ctx.send("@everyone มาเล่นกัน!")

# เปิดเซิร์ฟเวอร์ (ถ้าจำเป็น)
server_on()

# รันบอท
bot.run(TOKEN)
