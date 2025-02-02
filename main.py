import os
import discord
from discord.ext import commands
from discord import app_commands


from myserver import server_on

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







server_on()

bot.run(os.getenv('TOKEN'))