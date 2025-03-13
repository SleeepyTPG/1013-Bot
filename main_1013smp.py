import discord
from discord.ext import commands

bot = commands.bot(command_prefix="?", intents=discord.Intents.all())

@bot.event
async def on_ready():
    print("Bot online")

@bot.event
async def on_down():
    print("Bot offline")

@bot.slash_command(description="Die Regeln halt")
async def rules(ctx, user:(discord.Member)):
    await ctx.respond(f"")


bot.run("MTM0NjIxMzY3MTk0ODI1OTM4OA.GsJ-ML.vT2t4kU4QHZmlLwkY-gc_SJ5d7VvRjvimarVgY")
