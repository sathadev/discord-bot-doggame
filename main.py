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
class MyBot(commands.Bot):
    def __init__(self):
        super().__init__(
            command_prefix="!",
            intents=intents,
            application_id=os.getenv("APPLICATION_ID"),  # ใส่ Application ID ของคุณ
        )

    async def setup_hook(self):
        # ซิงค์คำสั่ง Slash Command กับ Discord
        await bot.tree.sync()

bot = MyBot()

@bot.event
async def on_ready():
    print(f"บอทออนไลน์แล้ว! ชื่อบอท: {bot.user}")

# เพิ่ม Slash Command
@bot.tree.command(name="ชวนเล่น", description="ส่งข้อความชวนทุกคนมาเล่น")
async def ชวนเล่น(interaction: discord.Interaction):
    await interaction.response.send_message("@everyone มาเล่นกัน!", ephemeral=False)

server_on()

bot.run(os.getenv('TOKEN'))
