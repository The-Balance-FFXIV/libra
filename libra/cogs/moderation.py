from datetime import datetime
import discord
from discord.ext import commands
from discord.commands import slash_command

class ModerationCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @slash_command(name="ban")
    @commands.guild_only()
    @commands.has_permissions(ban_members=True)
    async def ban(self, ctx: commands.Context, user: discord.Member, reason: str):
        embed = discord.Embed(title="Member Banned", color = 0xD82626)
        embed.add_field(name="Member", value=f"<@{user.id}> ({user})", inline=True)
        embed.add_field(name="Mod", value=ctx.author.nick, inline=True)
        embed.add_field(name="Reason", value=reason, inline=False)
        embed.set_thumbnail(url=user.display_avatar)
        embed.timestamp = datetime.utcnow()

        await user.ban(reason=reason)
        await self.bot.log_message(embed=embed)
        await ctx.respond(embed=embed, ephemeral=True)

    @slash_command(name="kick", description="Kick a user.")
    @commands.guild_only()
    @commands.has_permissions(kick_members=True)
    async def kick(self, ctx: commands.Context, user: discord.Member):
        embed = discord.Embed(title="Member Kicked", color = 0xD82626)
        embed.add_field(name="Member", value=f"<@{user.id}> ({user})", inline=True)
        embed.add_field(name="Mod", value=ctx.author.nick, inline=True)
        embed.set_thumbnail(url=user.display_avatar)
        embed.timestamp = datetime.utcnow()

        await user.kick()
        await self.bot.log_message(embed=embed)
        await ctx.respond(embed=embed, ephemeral=True)
    
def setup(bot):
    bot.add_cog(ModerationCog(bot))
