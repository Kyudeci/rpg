import pygame
import sounds
import sys
import rpg
import random as rdm
import monster as mon
import eventFlags as ef
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
    joke=["Do you really want to go with that?","I mean come on! There are better names!",
    "Here, I'll even give the chance to change it this one time!","I'll even forget what your previous name was!"]
    print(Meikahs+":",playerName,"was it?")
    for x in range(len(joke)):
        print(Meikahs+":",joke[x])
        pygame.time.wait(1800)
    nameChange=input('Meikahs: So will you change your name?\n>>')
    if nameChange in affirm:
        rpg.Player.playerList.pop()
        playerName=rpg.create_player()
    elif nameChange in deny:
        print(Meikahs+": I guess you're sticking with "+playerName+", then?")
    pygame.time.wait(1800)
    print(Meikahs+": Oh! That reminds me, I have something for you.")
    pygame.time.wait(1800)
    rpg.give_stats(1)
    Red="\033[0;31m"
    Green="\033[0;32m"
    Yellow="\033[0;33m"
    # Blue="\033[0;34m"
    Purple="\033[0;35m"
    Cyan="\033[0;36m"
    CEND = '\033[0m'
    pygame.time.wait(2000)
    print('\n'+Meikahs+": Yes, these are your",Red,"Specific but",Cyan,"Telling",Yellow,"Attributes of",Green,"Tactical",Purple,"Strength",CEND,"or STATS for short!")
    pygame.time.wait(1800)
    clarity=input("\nDo you understand so far?\n1.Yes\n2.Also Yes\n3.What kind of options are these?\n>>")
    if clarity=="1":
        rpg.Player.playerList[1].karma+=1
        print(Meikahs+": How compliant! Surely you'll survive.")
        pygame.time.wait(1800)
    elif clarity=="2":
        print(Meikahs+": You could have just chosen the first option...")
        pygame.time.wait(1800)
    else:
        rpg.Player.playerList[1].karma-=1
        print(Meikahs+": Silly child, you are guided by my hand. I cannot simply leave you to your own devices, now can I?")
        pygame.time.wait(1800)
    if clarity=="1" or clarity=="2":
        print(Meikahs+": Well now, it's time for you to get going. Ta ta!")
        pygame.time.wait(1800)
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
            print("You stumble!\n")
            break
        else:
            print("\n.")
            pygame.time.wait(500)
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
        print("\nThe forest roars!")
        enemy=mon.rank1Assign()
        defender=mon.Monster.Rank1[enemy]
        rpg.battle(enemy,attacker,defender)
        TownSucreNoir()
def TownSucreNoir():
    playerName=rpg.Player.playerList[1].name
    player=rpg.Player.playerList[1]
    if ef.Events().Flags[0].loop==0:
        print("\nA town appears into your view.")
        rpg.Player.playerList[1].location="TownSucreNoir"
        print("\nWelcome to Town de SucreNoir!")
        ef.Events().Flags[0].loop+=TownMenu()
    if ef.Events().Flags[0].loop==1:
        def TownSucreNoir2():
            print("\nA twisted pillar appears before you...")
            pygame.time.wait(1000)
            print("\nYou inspect it for quite some time before coming to the conclusion it is made of resin.")
            if ef.Events().Flags[0].loop==2:
                print("\nA second inspection reveals an indentation that was not previously there.")
            else:
                print("You make your leave.")
                pygame.time.wait(1800)
                GeardegCrestPath()
        TownSucreNoir2()
def GeardegCrestPath():
    playerName=rpg.Player.playerList[1].name
    player=rpg.Player.playerList[1]
    attacker=rpg.Player.playerList[1]
    print("\nA road of battle and desire: Geardeg Crest.")
    # rpg.save(player,rpg.Player.playerList)
    rpg.Player.playerList[1].location="GeardegCrestPath"
    while ef.Events().Flags[1].battles!=10:
        walking=True
        while walking==True:
            walking=rpg.walking()
            if walking==False:
                break
            else:
                continue
        if ef.Events().Flags[1].battles<5:
            enemy=mon.rank1Assign()
            defender=mon.Monster.Rank1[enemy]
            rpg.battle(enemy,attacker,defender)
        else:
            enemy=mon.rank2Assign()
            defender=mon.Monster.Rank2[enemy]
            rpg.battle(enemy,attacker,defender)
        ef.Events().Flags[1].battles+=1
    print("\nHaving survived the onslaught of foes, {0} presses forth".format(playerName))
    pygame.time.wait(1800)
    if ef.Events().Flags[1].dagger==True:
        print("Your dagger glows with a brillant but ominous light.")
    GeardegRath()
def GeardegRath():
    print("Soldier: Halt!")
    obey=input("Obey?\n>")
    if obey in affirm:
        rpg.Player.playerList[1].karma+=1
    elif obey in deny:
        rpg.Player.playerList[1].karma-=1
    # rpg.Player.playerList[1].location="GeardegRath"
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
                    quit=input("Would you like to quit the game?")
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
                    quit=input("Would you like to quit the game?")
                    return TownMenu()
                else:
                    return TownMenu()
    elif location=="GeardegRath":
        pass


locations={"TownSucreNoir":TownSucreNoir,"GeardegCrestPath":GeardegCrestPath,"GeardegRath":GeardegRath}
ef.onStartFlagSet()
rpg.mainMenu()
# ForestBisca()
