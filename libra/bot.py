import asyncio
from discord.ext import commands
from discord_ui import UI
import toml

# Cogs that should run on startup
default_cogs = ['cogs.moderation']

class Libra(commands.Bot):
    def __init__(self, config):
        super().__init__(config['bot']['description'])
        self.config = config

    async def on_ready(self):
        print(f"Logged in as: {self.user.name}")


async def run():
    config = toml.load("config.toml")
    bot = Libra(config)
    ui = UI(bot)

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
