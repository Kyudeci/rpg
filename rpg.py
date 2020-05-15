import pickle
import random
import sys
import tkinter as tk
from math import floor

import pygame

import eventFlags as ef
import monster
import moves
import sounds
import story
from player import Player

pygame.mixer.init()


def tc_combat(attacker, defender, root, txt, atk_type):
    if atk_type == 1:
        if attacker.spd > defender.spd:
            base_dmg = random.randint(5, 8)
            Admg = floor((base_dmg + (attacker.atk * .10))
                         * (100 / (100 + defender.dfn)))
            enem_rand = random.randint(0, 1)
            Bdmg = enemy_attack(attacker, defender, root, enem_rand, txt)
            if Bdmg > 0:
                txt.insert(tk.INSERT, "You took " + str(Bdmg) + " damage!\n")
        elif defender.spd > attacker.spd:
            enem_rand = random.randint(0, 1)
            Bdmg = enemy_attack(attacker, defender, root, enem_rand, txt)
            if Bdmg > 0:
                txt.insert(tk.INSERT, "You took " + str(Bdmg) + " damage!\n")
            base_dmg = random.randint(5, 8)
            Admg = floor((base_dmg + (attacker.atk * .10))
                         * (100 / (100 + defender.dfn)))
        else:
            pass
    elif atk_type == 2:
        if attacker.spd > defender.spd:
            base_dmg = random.randint(5, 8)
            Admg = floor((base_dmg + (attacker.matk * .10))
                         * (100 / (100 + defender.mdef)))
            enem_rand = random.randint(0, 1)
            Bdmg = enemy_attack(attacker, defender, root, enem_rand, txt)
            if Bdmg > 0:
                txt.insert(tk.INSERT, "You took " + str(Bdmg) + " damage!\n")
        elif defender.spd > attacker.spd:
            enem_rand = random.randint(0, 1)
            Bdmg = enemy_attack(attacker, defender, root, enem_rand, txt)
            if Bdmg > 0:
                txt.insert(tk.INSERT, "You took " + str(Bdmg) + " damage!\n")
            base_dmg = random.randint(5, 8)
            Admg = floor((base_dmg + (attacker.matk * .10))
                         * (100 / (100 + defender.mdef)))
        else:
            pass

    return Admg, Bdmg


def enemy_attack(attacker, defender, root, atk_type, txt):
    base_dmg = moves.movePool(atk_type, defender, root, txt)
    if base_dmg <= 0:
        return base_dmg
    if atk_type == 0:
        dmg = floor((base_dmg + (defender.atk * .10))
                    * (100 / (100 + attacker.dfn)))
    elif atk_type == 1:
        dmg = floor((base_dmg + (defender.matk * .10))
                    * (100 / (100 + attacker.mdef)))
    return dmg


def walking():
    tWalk = random.randint(1, 100)
    if tWalk in range(40, 51):
        print("\nA battle!\n")
        pygame.time.wait(1800)
        return False
    else:
        print("\n.")
        pygame.time.wait(500)
        return True

Player1 = Player("Kyu", 100, 54, 24, 56, 57, 61, 1)
# Player2=Player("Varis",100,45,34,34,24,60,1)
# Player3=Player("Y",100,23,25,54,34,90)
# Monsta1=monster.Monster("WizCat",1,100,100,100,100,100,100,34,256)


def save(player, plist):
    ef.Events().Flags.clear()
    ef.onStartFlagSet()
    player = attacker
    plist = Player.playerList
    events = ef.Events().Flags
    with open('savefile.dat', 'wb') as f:
        pickle.dump([player, plist, events], f, protocol=2)
    print("\nSave complete!")


def load():
    global attacker
    ef.Events().Flags.clear()
    with open('savefile.dat', 'rb') as f:
        player, plist, events = pickle.load(f)
        for x in range(1, len(plist)):
            Player.playerList.append(plist[x])
        attacker = Player.playerList[1]
        for y in range(0, len(events)):
            ef.Events().Flags.append(events[y])
        monster.enemy()
        give_stats(1)
    return True


def is_accessible(path, mode='r'):
    """
    Check if the file or directory at `path` can
    be accessed by the program using `mode` open flags.
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True


def give_stats(num):
    print("\nName:", Player.playerList[num].name,
          "\nLevel:", Player.playerList[num].lvl)
    print("HP:", Player.playerList[num].hp,
          "\nAttack:", Player.playerList[num].atk)
    print("Defense:", Player.playerList[num].dfn,
          "\nMagic Attack:", Player.playerList[num].matk)
    print("Magic Defence:",
          Player.playerList[num].mdef, "\nSpeed:", Player.playerList[num].spd)
    print(Player.playerList[num].location)


def create_player():
    name = input("Meikahs: What is your name by chance? => ")
    if len(name) < 3 and name != 'AI':
        print("Your name is not up to my standards.")
        return create_player()
    atk = random.randint(20, 50)
    dfn = random.randint(20, 50)
    matk = random.randint(20, 50)
    mdef = random.randint(20, 50)
    spd = random.randint(20, 50)
    lvl = 1
    new_player = Player(name, 100, atk, dfn, matk, mdef, spd, lvl)
    Player.playerList.append(new_player)
    return name

def gameStart(l_check=False):
    if l_check == False:
        sounds.background_music(3)
        story.start()
    else:
        location = Player.playerList[1].location
        if location in story.locations:
            story.locations[location]()

### Testing Below ###
# gameStart()
# mainMenu()
# create_player()
# random_player()
# enemy_assign_random()
# print(defender.name)
# for x in range(1,len(Player.playerList)):
#     give_stats(x)
#     print("")
# attacker.levelUp(120)
