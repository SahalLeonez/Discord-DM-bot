import discord
import asyncio

TOKEN = 'Your Bot Token'
USER_ID = 927107287242403900

client = discord.Client()

@client.event
async def on_ready():
    user = await client.fetch_user(USER_ID)
    while True:
        await user.send("<@{USER_ID}>")
# Add what you want to send above by modifying this part: "<@{USER_ID}>"
        await asyncio.sleep(0.00001)

client.run(TOKEN)
