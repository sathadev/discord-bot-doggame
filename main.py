import os
import discord
from discord.ext import commands
from discord import app_commands
import asyncio

from myserver import server_on

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # จำเป็นสำหรับการอ่านข้อความ
intents.members = True  # จำเป็นสำหรับการตรวจสอบสมาชิก

bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้ว! ชื่อบอท: {bot.user}")

# เพิ่ม Slash Command
@bot.tree.command(name="ชวนเล่น", description="ส่งข้อความชวนทุกคนมาเล่น")
async def ชวนเล่น(interaction: discord.Interaction):
    await interaction.response.send_message("@everyone มาเล่นกัน!", ephemeral=False)

# ฟังก์ชั่นใหม่สำหรับแท็กผู้ใช้
@bot.tree.command(name="ตามตัว", description="แท็กผู้ใช้จนกว่าจะเข้าห้องเสียง")
async def ตามตัว(interaction: discord.Interaction, ชื่อดิส: str):
    # ค้นหาผู้ใช้จากชื่อ
    member = discord.utils.get(interaction.guild.members, name=ชื่อดิส)
    
    if member:
        # เช็คว่าผู้ใช้เข้าห้องเสียงหรือยัง
        while member.voice is None:
            # ถ้ายังไม่เข้า
            await interaction.channel.send(f"<@{member.id}> รอเข้าเสียง! <@{member.id}> รอเข้าเสียง! <@{member.id}> รอเข้าเสียง!")  # ส่งข้อความแท็กผู้ใช้
            await asyncio.sleep(0.5)  # รอ 0.5 วินาที
        # เมื่อผู้ใช้เข้าห้องเสียงแล้ว
        await interaction.response.send_message(f"ผู้ใช้ {member.name} เข้าห้องเสียงแล้ว!", ephemeral=False)
    else:
        await interaction.response.send_message(f"ไม่พบผู้ใช้ {ชื่อดิส} ในเซิร์ฟเวอร์นี้", ephemeral=True)

server_on()

bot.run(os.getenv('TOKEN'))
