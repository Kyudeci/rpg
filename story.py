import pygame
import sounds
import sys
import random as rdm
import rpg
import monster as mon
import eventFlags as ef
import numpy as np
from options import *
import choice as ch

from all_items.inventory import Inventory
import all_items.item_ as IC
affirm=['yes','YES','Yes','y','Y','1']
deny=['no','NO','No','n','N','2']
Red="\033[0;31m"
Green="\033[0;32m"
Cyan="\033[0;36m"
On_White="\033[47m"
CEND = '\033[0m'
Yellow="\033[0;33m"
Blue="\033[0;34m"
Purple="\033[0;35m"
Meikahs=rpg.Player.playerList[0].name
def start():
    mon.enemy()
    print('\n???: Are you perhaps LOST?')
    introScene()
    pygame.time.wait(1000)
    playerName=rpg.create_player()
    CharacterText(ch.meikahsJoke)
    playerName=nameChange(playerName)
    pygame.time.wait(1800)
    print(Meikahs+": Oh! That reminds me, I have something for you.")
    Inventory.inventory[0].get_item(1)
    # rpg.Player.playerList[1].dev_check_inventory()
    pygame.time.wait(1800)
    rpg.give_stats(1)
    pygame.time.wait(2000)
    print('\n'+Meikahs+": Yes, these are your",Red,"Specific but",Cyan,"Telling",Yellow,"Attributes of",Green,"Tactical",Purple,"Strength",CEND,"or STATS for short!")
    input(">")
    pygame.time.wait(1800)
    ForestBisca()
    
def ForestBisca():
    input("Now entering Forest Bisca.\n>")
    print("\nThe road ahead is a long and dark.\nYou trip and fall, and the forest snickers.")
    pygame.time.wait(1800)
    print("There is a single path in front of you. Go forth!")
    input(">")
    #Running sounds
    #Scripted encounter
    print("\nWalking Simulator Activated!")
    walking=True
    while walking!=False:
        tWalk=rdm.randint(1,100)
        if tWalk in range(37,50):
            print("You stumble!\n")
            break
        else:
            print("\n.")
            pygame.time.wait(500)
            continue
    enemy=mon.rank1Assign()
    defender=mon.Monster.Rank1[enemy]
    attacker=rpg.Player.playerList[1]
    combat(attacker,defender)
    print("You come to a fork in the path.")
    if rpg.Player.playerList[1].karma>=0:
        print("Instinctively, you take the path to the left!\n")
        defender=mon.Monster.Rank1[enemy]
        combat(attacker,defender)
        TownSucreNoir()
    else:
        print("Following your instincts, you take the right path!\n")
        enemy=mon.rank1Assign()
        defender=mon.Monster.Rank1[enemy]
        combat(attacker,defender)
        print("\nThe forest roars!")
        enemy=mon.rank1Assign()
        defender=mon.Monster.Rank1[enemy]
        combat(attacker,defender)
        TownSucreNoir()

def TownSucreNoir():
    player = rpg.Player.playerList[1]
    playerName = player.name
    eFlags = ef.Events().Flags
    if eFlags[0].loop==0:
        print("\nA town appears into your view.")
        player.location = "TownSucreNoir"
        print("\nWelcome to Town de SucreNoir!")
        TSNMenu(player,eFlags)
    if eFlags[0].loop==1:
        def TownSucreNoir2():
            print("\nA twisted pillar appears before you...")
            pygame.time.wait(1000)
            print("\nYou inspect it for quite some time before coming to the conclusion it is made of resin.")
            if eFlags[0].loop==2:
                print("\nA second inspection reveals an indentation that was not previously there.")
            else:
                print("You make your leave.")
                pygame.time.wait(1800)
                GeardegCrestPath()
        TownSucreNoir2()

def GeardegCrestPath():
    player = rpg.Player.playerList[1]
    playerName = player.name
    eFlags = ef.Events().Flags
    player.location = "GeardegCrestPath"
    # rpg.save(player,rpg.Player.playerList)
    print("\nA road of battle and desire: Geardeg Crest.")
    while eFlags[1].battles!=10:
        walking=True
        while walking==True:
            walking=rpg.walking()
            if walking==False:
                break
            else:
                continue
        if eFlags[1].battles<5:
            enemy=mon.rank1Assign()
            defender=mon.Monster.Rank1[enemy]
            combat(player,defender)
        else:
            enemy=mon.rank2Assign()
            defender=mon.Monster.Rank2[enemy]
            combat(player,defender)
        eFlags[1].battles+=1
    print("\nHaving survived the onslaught of foes, {0} presses forth!".format(playerName))
    input(">")
    if eFlags[1].dagger==True:
        print("Your dagger glows with a brillant but ominous light.")
    GeardegRath()

def GeardegRath():
    rpg.Player.playerList[1].location="GeardegRath"
    if ef.Events().Flags[2].intro==False:
        print("\nSoldier: Halt!")
        obey=input("Obey?\n>")
        if obey in affirm:
            rpg.Player.playerList[1].karma+=1
            ef.Events().Flags[2].intro=basicPuzzle()
        elif obey in deny:
            rpg.Player.playerList[1].karma-=1
            print("Soldier: ..... ")
        else:
            print("Eh? Battle you say.")
    else:
        print("Welcome to GeardegRath!\n || A city of tech built on the ruin of its past! || ")

def TownMenu():
    player=rpg.Player.playerList[1]
    location=rpg.Player.playerList[1].location
    eFlags=ef.Events().Flags
    pygame.time.wait(1800)
    if location=="TownSucreNoir":
        if eFlags[0].options==False:
            menu=input("""\nWhat would you like to do?
    1.Look Around\n    2.Check Stats\n    3.Save\n""")
            if menu=="1":
                print("The town looks empty...")
                eFlags[0].options=True
                return TownMenu()
            elif menu=="2":
                rpg.give_stats(1)
                return TownMenu()
            elif menu=="3":
                playerSave=input("Would you like to save?\n>")
                if playerSave in affirm:
                    rpg.save(player,rpg.Player.playerList)
                    exit=input("Would you like to quit the game?")
                    return TownMenu()
                else:
                    return TownMenu()
        else:
            menu=input("""\nWhat would you like to do?
    1.Look Around\n    2.Interact with Crest\n    3.Check Stats\n    4.Save\n""")
            if menu=="1":
                print("The town looks empty...")
                return TownMenu()
            elif menu=="2":
                print("A change occurs!")
                return 1
            elif menu=="3":
                rpg.give_stats(1)
                return TownMenu()
            elif menu=="4":
                playerSave=input("Would you like to save?\n>")
                if playerSave in affirm:
                    rpg.save(player,rpg.Player.playerList)
                    exit=input("Would you like to quit the game?")
                    return TownMenu()
                else:
                    return TownMenu()
    elif location=="GeardegRath":
        if eFlags[2].options==False:
            menu=input("""\nWhat would you like to do?
    1.Look Around\n    2.Check Stats\n    3.Save\n""")
            if menu=="1":
                print("You are awestruck by the mechanical marvels")

                return TownMenu()
def basicPuzzle():
    puzzleSol=[2,4,1,3]
    np.random.shuffle(puzzleSol)
    puzzle=[1,2,3,4]
    print("Find the correct combination!")
    print("Rules:\n1.Select the first tile you want to move.\n2.Select the tile to switch with.\n")
    while puzzle!=puzzleSol:
        for y in range(0,4):
            if puzzle[y]==puzzleSol[y]:
                print(Green,On_White,puzzle[y],CEND,end="")
            if puzzle[y]!=puzzleSol[y]:
                print(Red,On_White,puzzle[y],CEND,end="")
        print("")
        sel1=int(input())
        sel2=int(input())
        sel1=sel1-1
        sel2=sel2-1
        if sel1==sel2:
            print("No tiles moved!")
            continue
        if sel1>4 or sel2>4:
            continue
        puzzle[sel1],puzzle[sel2]=puzzle[sel2],puzzle[sel1]
    print("\nPuzzle Complete!")
    for x in range(4):
        print(Cyan,On_White,puzzle[x],CEND,end="")
    return True


locations={"TownSucreNoir":TownSucreNoir,"GeardegCrestPath":GeardegCrestPath,"GeardegRath":GeardegRath}
ef.onStartFlagSet()
mainmenu()
# basicPuzzle()
# ForestBisca()
