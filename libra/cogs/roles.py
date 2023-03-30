from typing import Dict
import discord
from discord.ext import commands
from discord.commands import slash_command

class RoleButton(discord.ui.Button):
    r"""A discord UI button which toggles a server role for a user.

    Attributes
    ----------
    label: str
        The button's label text.
    role: :class:`discord.Role`
        The role this button should toggle.
    emoji: :class:`discord.Emoji`
        The button's emoji.
    row: int
        The row this button should be displayed in within the view.
    """

    def __init__(self, label: str, role: discord.Role, emoji: discord.Emoji, row: int):
        super().__init__(style=discord.ButtonStyle.blurple, label=label, emoji=emoji, row=row)
        self.id = id
        self.role = role

    async def callback(self, interaction: discord.Interaction):
        user = interaction.user

        if self.role in user.roles:
            await user.remove_roles(self.role)
        else:
            await user.add_roles(self.role)


class RoleSelectView(discord.ui.View):
    r"""Defines the Discord interaction view for the Role Select command.

    Attributes
    ----------
    roles: Dict[str, :class:`discord.Role`]
        A dict of server roles keyed by their name.
    emojis: Dict[str, :class:`discord.Emoji`]
        A dict of server emojis keyed by their name.
    """

    def __init__(self, roles: Dict[str, discord.Role], emojis: Dict[str, discord.Emoji]):
        super().__init__()
        # Some example buttons, we'll want to store the role name / emoji name in a DB
        self.add_item(RoleButton("Bard", roles['Bard'], emojis['bard'], 0))
        self.add_item(RoleButton("Machinist", roles['Machinist'], emojis['machinist'], 1))


class RolesCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.emojis = {}
        self.roles = {}

    @slash_command(name="roleselect", description="Opens a menu to add/remove server roles.")
    @commands.guild_only()
    async def roleselect(self, ctx: commands.Context):
        if not self.emojis:
            # Build a dict from the server's emojis if it doesn't exist yet
            for emoji in ctx.guild.emojis:
                self.emojis[emoji.name] = emoji

        if not self.roles:
            # Build a dict from the server's roles if it doesn't exist yet
            for role in await ctx.guild.fetch_roles():
                self.roles[role.name] = role

        await ctx.respond("**Choose your roles**", view=RoleSelectView(self.roles, self.emojis), ephemeral=True)
    

def setup(bot):
    bot.add_cog(RolesCog(bot))
