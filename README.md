# Tarkov Discord Bot

This repository contains a simple Discord bot for the game Escape from Tarkov. The bot can track data from public APIs and display it in Discord.

## Features

- **Ping**: Check if the bot is responsive.
- **Server Status**: Fetch server status or other public data from Escape from Tarkov APIs.

## Setup

1. Install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

2. Create a Discord bot and obtain its token. Set the token as an environment variable:

```bash
export DISCORD_TOKEN="YOUR_DISCORD_BOT_TOKEN"
```

3. Run the bot:

```bash
python bot.py
```

The bot uses `discord.py` and `aiohttp` for asynchronous HTTP requests.
