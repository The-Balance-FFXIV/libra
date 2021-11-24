from datetime import datetime
import discord
from discord.ext import commands
from discord_ui.cogs import slash_cog

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_cog(name="ban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx, user: discord.Member, reason: str):
        userID = (user.id)
        embed = discord.Embed(title="Member Banned", color = 0xD82626)
        embed.add_field(name="Member", value="{} ".format(user) + "(<@{}>)".format(userID), inline=True)
        embed.add_field(name="Mod", value="{}".format(ctx.author.nick), inline=True)
        embed.add_field(name="Reason", value="{}".format(reason), inline=False)
        embed.set_thumbnail(url=user.avatar_url)
        embed.timestamp = datetime.utcnow()

        log_channel_id = self.bot.config['channels']['log']
        log_channel = self.bot.get_channel(log_channel_id)

        await user.ban(reason=reason)
        await log_channel.send(embed=embed)
        await ctx.respond(embed=embed)

    @slash_cog(name="kick")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx, user: discord.Member):
        userID = (user.id)
        embed = discord.Embed(title="Member Kicked", color = 0xD82626)
        embed.add_field(name="Member", value="{} ".format(user) + "(<@{}>)".format(userID), inline=True)
        embed.add_field(name="Mod", value="{}".format(ctx.author.nick), inline=True)
        embed.set_thumbnail(url=user.avatar_url)
        embed.timestamp = datetime.utcnow()

        log_channel_id = self.bot.config['channels']['log']
        log_channel = self.bot.get_channel(log_channel_id)

        await user.kick()
        await log_channel.send(embed=embed)
        await ctx.respond(embed=embed)
    
def setup(bot):
    bot.add_cog(ModerationCog(bot))