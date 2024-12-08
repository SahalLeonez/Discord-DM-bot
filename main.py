import discord
import asyncio

TOKEN = 'Your Bot Token'
# Put your bot token here, simple as that
USER_ID = 123456
# Remove 123456 and replace it with your target (victim) user ID

client = discord.Client()

@client.event
async def on_ready():
    user = await client.fetch_user(USER_ID)
    while True:
        await user.send("<@{USER_ID}>")
# Add what you want to send above by modifying this part: "<@{USER_ID}>"
        await asyncio.sleep(0.00001)
# You can change the 0.00001 to 0.1 if you don't want to get rate limited by Discord but it will have a slower time.

client.run(TOKEN)
