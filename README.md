# Libra

A moderation bot for The Balance discord.

## Prerequisites

* `pipenv`

## Running locally

1. Clone the repo and `pipenv install`. 
2. Create a `config.toml` file using the template provided in `example.config.toml`.
3. Run `libra/bot.py` and invite the bot to your server.

## Inviting the bot to your server

Use the URL `https://discord.com/oauth2/authorize?client_id=${CLIENT_ID}&permissions=268435462&scope=applications.commands%20bot` for the right permissions and scope for inviting the bot to your server