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
