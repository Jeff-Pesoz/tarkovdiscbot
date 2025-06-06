import os
import discord
from discord.ext import commands
import aiohttp

TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.command()
async def ping(ctx):
    """Respond with pong"""
    await ctx.send("Pong!")

@bot.command(name="status")
async def server_status(ctx):
    """Fetch Escape from Tarkov server status"""
    url = "https://status.escapefromtarkov.com/status.json"
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    status = data.get("status", "unknown")
                    await ctx.send(f"EFT Server Status: {status}")
                else:
                    await ctx.send("Failed to fetch server status")
    except Exception as e:
        await ctx.send(f"Error fetching status: {e}")

if __name__ == "__main__":
    if not TOKEN:
        raise SystemExit("DISCORD_TOKEN environment variable not set")
    bot.run(TOKEN)
