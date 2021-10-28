import discord
from discord.ext import commands

class Wiretapper(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.wiretap = []

        logcategory = self.bot.get_channel()

        if logcategory is None:
            pass #TODO: This needs to be updated to use the logging category or create one if not found

    @commands.command(name='startwiretap', aliases=['swt','wiretap'])
    async def startwiretap(self, ctx, user: discord.member):
        """Starts a wiretap on a user."""
        if user.id == ctx.author.id:
            await ctx.send("You can't wiretap yourself!")
        elif user.id in self.bot.wiretap:
            await ctx.send("That user is already being wiretapped!")
        else:
            self.bot.wiretap.append(user.id)
            await ctx.send(f"{user.mention} is now being wiretapped!")
    
    @commands.command(name='endwiretap', aliases=['ewt'])
    async def endwiretap(self, ctx, user: discord.member):
        """Stops a wiretap on a user."""
        if user.id == ctx.author.id:
            await ctx.send("You can't stop your own wiretap!")
        elif user.id not in self.bot.wiretap:
            await ctx.send("That user isn't being wiretapped!")
        else:
            self.bot.wiretap.remove(user.id)
            await ctx.send(f"{user.mention} is no longer being wiretapped!")
