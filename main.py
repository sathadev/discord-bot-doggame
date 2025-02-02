import os
import discord
from discord.ext import commands
from discord import app_commands

from myserver import server_on

intents = discord.Intents.default()
intents.messages = True
intents.guilds = True
intents.message_content = True  # จำเป็นสำหรับการอ่านข้อความ


bot = commands.Bot(command_prefix='/', intents=intents)


@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้ว! ชื่อบอท: {bot.user}")

# เพิ่ม Slash Command
@bot.tree.command(name="ชวนเล่น", description="ส่งข้อความชวนทุกคนมาเล่น")
async def ชวนเล่น(interaction: discord.Interaction):
    await interaction.response.send_message("@everyone มาเล่นกัน!", ephemeral=False)

server_on()

bot.run(os.getenv('TOKEN'))
