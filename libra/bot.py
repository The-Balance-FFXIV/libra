import asyncio
import discord
from discord.ext import commands
import toml

# Cogs that should run on startup
default_cogs = [
    'cogs.moderation',
    'cogs.roles',
]

class Libra(commands.Bot):
    def __init__(self, config):
        super().__init__(config['bot']['description'])
        self.config = config

    async def on_ready(self):
        print(f"Logged in as: {self.user.name}")

    async def log_message(self, embed: discord.Embed):
        channel_id = self.config['channels']['log']
        channel = self.get_channel(channel_id)
        await channel.send(embed=embed)


async def run():
    config = toml.load("config.toml")
    bot = Libra(config)

    if __name__ == '__main__':
        for cog in default_cogs:
            bot.load_extension(cog)

    try:
        await bot.login(config['bot']['token'])
        await bot.connect()

    except KeyboardInterrupt:
        await bot.logout()

loop = asyncio.get_event_loop()
loop.run_until_complete(run())
