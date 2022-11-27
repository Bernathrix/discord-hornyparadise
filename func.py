import discord
import asyncio


def find_element(list, element):
    for n in list:
        gg = n.split(' ')
        if gg[0] == element:
            nick = element + ' ' + gg[1]
            return nick
    return 'no'

def print_list(list):
    file = open(list)
    description = ''
    desc = file.readlines();
    file.close()
    for i in range(len(desc)):
        description = description + str(i+1) + '. ' + desc[i]
    list_players = discord.Embed(color = 0xff9900, title = 'Cписок Игроков', description = description)
    return list_players


def clear_list(name):
    file = open(name, 'w')
    file.write('')
    file.close()

def delete_name(name, nick):
    lines = []
    file = open(name)
    lines = file.readlines()
    file.close()
    a = find_element(lines, nick).split(' ')
    if a[0] == nick:
        lines.remove(find_element(lines, nick))
    file = open(name, 'w')
    for line in lines:
        file.write(line)
    file.close()

def add_name(name, nick):
    file = open(name, 'a')
    file.write(nick + '\n')
    file.close()

