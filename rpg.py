import random
import pygame
import sounds
import monster
import moves
import sys
import pickle
import eventFlags as ef
from math import floor
import tkinter as tk
import story

from all_items.inventory import Inventory
import all_items.item_
pygame.mixer.init()
class Player(Inventory):
    def __init__(self, name, hp, atk, dfn, matk, mdef, spd, lvl):
        self.name = name
        self.image = "images/qmark.png"
        self.baseHP = 100
        self.hp = hp
        self.atk = atk
        self.dfn = dfn
        self.matk = matk
        self.mdef = mdef
        self.spd = spd
        self.lvl = lvl
        self.xp = 0
        self.lvlNext = 25
        self.karma = 0
        self.location = "ForestBisca"
        self.bag = Inventory.bag
    playerList=[]
    Inventory.__init__
    def levelUp(self,xp):
        self.xp += xp
        while self.xp >= self.lvlNext:
            self.lvl += 1
            self.xp = self.xp - self.lvlNext
            self.lvlNext = floor(self.lvlNext * 1.5)
            print("\nYou are now level", self.lvl)
            print("Exp:", self.xp)
            print("To Next Level:", self.lvlNext, "\n")
            stat_attribute=[self.atk, self.dfn, self.matk, self.mdef, self.spd]
            for x in range(len(stat_attribute)):
                stat = ["Attack:", "Defense:", "Magic Attack:", "Magic Defense:", "Speed:"]
                increase = random.randint(0, 3)
                print(stat[x], stat_attribute[x], "+", increase)
                if stat[x] == stat[0]:
                    self.atk += increase
                elif stat[x] == stat[1]:
                    self.dfn += increase
                elif stat[x] == stat[2]:
                    self.matk += increase
                elif stat[x] == stat[3]:
                    self.mdef += increase
                elif stat[x] == stat[4]:
                    self.spd += increase

def tc_combat(attacker, defender, root, txt, type):
    if type == 1:
        if attacker.spd > defender.spd:
            base_dmg = random.randint(5, 8)
            Admg = floor((base_dmg + (attacker.atk * .10)) * (100 / (100 + defender.dfn)))
            enem_rand = random.randint(0, 1)
            Bdmg = enemy_attack(attacker, defender, root, enem_rand, txt)
            if Bdmg > 0:
                txt.insert(tk.INSERT,"You took " + str(Bdmg) + " damage!\n")
        elif defender.spd > attacker.spd:
            enem_rand = random.randint(0, 1)
            Bdmg = enemy_attack(attacker, defender, root, enem_rand, txt)
            if Bdmg > 0:
                txt.insert(tk.INSERT, "You took " + str(Bdmg) + " damage!\n")
            base_dmg = random.randint(5, 8)
            Admg = floor((base_dmg + (attacker.atk * .10)) * (100 / (100 + defender.dfn)))
        else:
            pass
    elif type==2:
        if attacker.spd > defender.spd:
            base_dmg = random.randint(5,8)
            Admg = floor((base_dmg+(attacker.matk*.10))*(100/(100+defender.mdef)))
            enem_rand = random.randint(0,1)
            Bdmg = enemy_attack(attacker,defender,root,enem_rand,txt)
            if Bdmg>0:
                txt.insert(tk.INSERT,"You took "+str(Bdmg)+" damage!\n")
        elif defender.spd > attacker.spd:
            enem_rand = random.randint(0,1)
            Bdmg = enemy_attack(attacker,defender,root,enem_rand,txt)
            if Bdmg>0:
                txt.insert(tk.INSERT,"You took "+str(Bdmg)+" damage!\n")
            base_dmg = random.randint(5,8)
            Admg = floor((base_dmg+(attacker.matk*.10))*(100/(100+defender.mdef)))
        else:
            pass

    return Admg,Bdmg

def enemy_attack(attacker,defender,root,type,txt):
    base_dmg = moves.movePool(type,defender,root,txt)
    if base_dmg<=0:
        return base_dmg
    if type==0:
        dmg = floor((base_dmg+(defender.atk*.10))*(100/(100+attacker.dfn)))
    elif type==1:
        dmg = floor((base_dmg+(defender.matk*.10))*(100/(100+attacker.mdef)))
    return dmg

def walking():
    tWalk=random.randint(1,100)
    if tWalk in range(40,51):
        print("\nA battle!\n")
        pygame.time.wait(1800)
        return False
    else:
        print("\n.")
        pygame.time.wait(500)
        return True
Origin=Player("Meikahs",999,999,999,999,999,999,999)
Player.playerList.append(Origin)
Player1=Player("Kyu",100,54,24,56,57,61,1)
# Player2=Player("Varis",100,45,34,34,24,60,1)
Player2 = monster.Monster("mon_icons/Vitaro2.png","Gooblins","Gooblins",2,76,27,35,20,20,45,100)
# Player3=Player("Y",100,23,25,54,34,90)
# Monsta1=monster.Monster("WizCat",1,100,100,100,100,100,100,34,256)

def save(player,plist):
    ef.Events().Flags.clear()
    ef.onStartFlagSet()
    player=attacker
    plist=Player.playerList
    events=ef.Events().Flags
    with open('savefile.dat', 'wb') as f:
        pickle.dump([player,plist,events], f, protocol=2)
    print("\nSave complete!")

def load():
    global attacker
    ef.Events().Flags.clear()
    with open('savefile.dat', 'rb') as f:
        player,plist,events = pickle.load(f)
        for x in range(1,len(plist)):
            Player.playerList.append(plist[x])
        attacker=Player.playerList[1]
        for y in range(0,len(events)):
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
    print("\nName:",Player.playerList[num].name,"\nLevel:",Player.playerList[num].lvl)
    print("HP:",Player.playerList[num].hp,"\nAttack:",Player.playerList[num].atk)
    print("Defense:",Player.playerList[num].dfn,"\nMagic Attack:",Player.playerList[num].matk)
    print("Magic Defence:",Player.playerList[num].mdef,"\nSpeed:",Player.playerList[num].spd)
    print(Player.playerList[num].location)
def create_player():
    global attacker
    name=input("Meikahs: What is your name by chance? =>")
    if len(name)<3:
        print("Your name is too short.")
        return create_player()
    atk=random.randint(20,50)
    dfn=random.randint(20,50)
    matk=random.randint(20,50)
    mdef=random.randint(20,50)
    spd=random.randint(20,50)
    lvl=1
    new_player=Player(name,100,atk,dfn,matk,mdef,spd,lvl)
    Player.playerList.append(new_player)
    attacker=Player.playerList[1]
    return name

def enemy_assign_manual():
    global defender
    print("")
    for x in range(2,len(Player.playerList)):
        print(x-1,".",Player.playerList[x].name,sep="")
    print("")
    enemy=int(input("Choose an opponent by selecting a number: "))
    if enemy+1>=len(Player.playerList):
        return enemy_assign_manual()
    else:
        defender=Player.playerList[enemy+1]
        print("")
        print("You have chosen",defender.name)
    # print(new_player.name)
    print(" ")
    print("""Are you sure?
1.Yes       2.No """)
    print(" ")
    confirm=int(input("Do you wish to fight? "))
    if confirm==2:
        enemy_assign_manual()
    else:
        return enemy+1
def enemy_assign_random():
    global defender
    enemy=random.randint(2,len(Player.playerList)-1)
    defender=Player.playerList[enemy]
    return enemy

def gameStart(l_check=False):
    if l_check==False:
        sounds.background_music(3)
        story.start()
    else:
        location=Player.playerList[1].location
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
