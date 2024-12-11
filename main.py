import discord
import asyncio
from discord.ext import commands, tasks

TOKEN = "YOUR BOT TOKEN HERE"
# Put your bot token here, simple as that
USER_ID = 123456
# Remove 123456 and replace it with your target (victim) user ID
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='.', intents=intents)
# Set up for Discord Bot Intents (Which is required for this to work), do that on https://discord.com/developers/applications and click on your bot

@bot.event
async def on_ready():
    user = await bot.fetch_user(USER_ID)
    while True:
        await user.send(f"<@{USER_ID}>")
        print(f"Sent a message to {USER_ID}!") # Remove if don't like lol (Verify that the victim got the message)
# Add what you want to send above by modifying this part: "<@{USER_ID}>"
        await asyncio.sleep(0.00001)
# You can change the 0.00001 to 0.1 if you don't want to get rate limited by Discord but it will have a slower time.
bot.run(TOKEN)
