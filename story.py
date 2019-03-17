import pygame
import sounds
import sys
import rpg
import random as rdm
import monster as mon
affirm=['yes','YES','Yes','y','Y','1']
deny=['no','NO','No','n','N','2']
Meikahs=rpg.Player.playerList[0].name
def start():
    mon.enemy()
    intro=input('\n???: Are you perhaps LOST?\n>Yes...\n>No, not really!\n>>')
    if intro in affirm:
        print('\nWelcome! I am Meikahs, Keeper of the Lost!\n')
    elif intro in deny:
        print('\n???: Then begone from here! uwu\n')
        sys.exit()
    else:
        return start()
    pygame.time.wait(1000)
    playerName=rpg.create_player()
    joke=["Do you really want to go with that?", "I mean come on! There are better names!","Here, I'll even give the chance to change it this one time!","I'll even forget what your previous name was!"]
    print(Meikahs+":",playerName,"was it?")
    for x in range(len(joke)):
        print(Meikahs+":",joke[x])
        # pygame.time.wait(1800)
    nameChange=input('Meikahs: So will you change your name?\n>>')
    if nameChange in affirm:
        rpg.Player.playerList.pop()
        playerName=rpg.create_player()
    elif nameChange in deny:
        print(Meikahs+": I guess you're sticking with "+playerName+",then?")
    print(Meikahs+": Oh! That reminds me, I have something for you.")
    # pygame.time.wait(1800)
    rpg.give_stats(1)
    Red="\033[0;31m"
    Green="\033[0;32m"
    Yellow="\033[0;33m"
    # Blue="\033[0;34m"
    Purple="\033[0;35m"
    Cyan="\033[0;36m"
    CEND = '\033[0m'
    print('\n'+Meikahs+": Yes, these are your",Red,"Specific but",Cyan,"Telling",Yellow,"Attributes of",Green,"Tactical",Purple,"Strength",CEND,"or STATS for short!")
    clarity=input("\nDo you understand so far?\n1.Yes\n2.Also Yes\n3.What kind of options are these?\n>>")
    if clarity=="1":
        rpg.Player.playerList[1].karma+=1
        print(Meikahs+": How compliant! Let's continue!")
    elif clarity=="2":
        print(Meikahs+": You could have just chosen the first option...")
    else:
        rpg.Player.playerList[1].karma-=1
        print(Meikahs+": Silly child, you are guided by my hand. I cannot simply leave you to your own devices, now can I?")
    if clarity=="1" or clarity=="2":
        print(Meikahs+": Well now, it's time for you to get going. Ta ta!")
        ForestBisca()
    else:
        print(Meikahs+": It's time for you to LEAVE!!!")
        ForestBisca()
def ForestBisca():
    print("\nThe road ahead is a long and dark.\nYou trip and fall, and the forest snickers.")
    pygame.time.wait(1800)
    print("There is a single path in front of you. Go forth!")
    #Running sounds
    #Scripted encounter
    print("\nWalking Simulator Activated!")
    walking=True
    while walking!=False:
        tWalk=rdm.randint(1,100)
        if tWalk in range(37,50):
            print("You stumble!")
            break
        else:
            print("\n.")
            continue
    enemy=mon.rank1Assign()
    defender=mon.Monster.Rank1[enemy]
    attacker=rpg.Player.playerList[1]
    rpg.battle(enemy,attacker,defender)
    print("\nWhich way will you go?\n>Right    >Left\n")
    if rpg.Player.playerList[1].karma>=0:
        print("Instinctively, you take the path to the left!\n")
        defender=mon.Monster.Rank1[enemy]
        rpg.battle(enemy,attacker,defender)
        TownSucreNoir()
    else:
        print("Following your instincts, you take the right path!\n")
        enemy=mon.rank1Assign()
        defender=mon.Monster.Rank1[enemy]
        rpg.battle(enemy,attacker,defender)
        print("The forest roars!")
        enemy=mon.rank1Assign()
        defender=mon.Monster.Rank1[enemy]
        rpg.battle(enemy,attacker,defender)
        TownSucreNoir()
def TownSucreNoir():
    playerName=rpg.Player.playerList[1].name
    print("A town appears into your view.")
start()
# ForestBisca()
