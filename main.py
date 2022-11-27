import discord
import asyncio
from discord import *
from discord.ext import commands
import func

intents = discord.Intents().all()
help_info = "Cписок команд, команды необходимо писать в канале #наборчикк, сообщения сами чистятся:\n $add <nickname> <@discord_name> - добавляет игрок в список, в поле никнэйм вводится игровой ник, а в поле дискорд нэйм - ник в дискорде.\n Пример:\n $add Bernathr1x <@397331097333268481>\n Команда $delete <nickname>\n Для ее работы необходим только ник игрока, который всегда можно узнать в списке.\n Пример:\n $delete Bernathr1x - удалит ранее добавленного игрока из списка"
config = {
    'token': 'MTA0NjM0MDkxMDA2NzIyMDYwMA.G2QCHf.uELRxiZSsxHUOel_ca2jt4TmPtCRyLMjdrMB4k',
    'prefix': '$',
    'txt': 'list.txt',
    'role': '🐝'
}

bot = commands.Bot(command_prefix=config['prefix'], intents = intents)

@bot.event
async def on_ready():
    global channel1
    channel1 = bot.get_channel(1033840530917965904)

@bot.command(name = 'add', description = 'Hello man', hidden = False)
@commands.has_role(config['role'])
async def add(ctx, arg1, arg2):
    line = arg1 + ' ' + arg2
    func.add_name(config['txt'], line)
    message = await ctx.reply("Done")
    await channel1.purge(limit=1)
    await channel1.send(embed = func.print_list(config['txt']))
    await asyncio.sleep(3)
    await ctx.channel.purge(limit=2)

@bot.command()
@commands.has_role(config['role'])
async def delete(ctx, arg1):
    func.delete_name(config['txt'], arg1)
    message = await ctx.reply("Done")
    await channel1.purge(limit=1)
    await channel1.send(embed = func.print_list(config['txt']))
    await asyncio.sleep(3)
    await ctx.channel.purge(limit=2)

@bot.command()
@commands.has_role(config['role'])
async def info(ctx):
    embed = discord.Embed(color = 0xff9900, title = 'Помощь', description = help_info)
    await ctx.channel.send(embed = embed)

bot.run(config['token'])