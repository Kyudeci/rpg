import random
import pygame
import sounds
import monster
from monster import enemyList
from math import floor
pygame.mixer.init()
class Player:
    def __init__(self,name,hp,atk,dfn,matk,mdef,spd):
        self.name=name
        self.hp=hp
        self.atk=atk
        self.dfn=dfn
        self.matk=matk
        self.mdef=mdef
        self.spd=spd
def combat_offense(current,enemy):
    base_dmg=0
    for n in range(5):
        roll=random.randint(1,6)
        base_dmg+=roll
    if current==attacker:
        if attacker.atk:
            dmg=base_dmg+(attacker.atk/defender.dfn)
            if game_mode==3:
                defender.hp-=abs(dmg)
            else:
                defender.hp-=abs(dmg)
            print("")
            print("You used a Physical Attack!")
            if game_mode==3:
                print(monster.monster_type(),"took",floor(abs(dmg)),"damage!")
            else:
                print(defender.name,"took",floor(abs(dmg)),"damage!")
            battle_state()
            sounds.punch()
            return dmg
    else:
        if defender.atk:
            dmg=base_dmg+(defender.atk/attacker.dfn)
            attacker.hp-=abs(dmg)
            print("")
            print("The enemy used a Physical Attack!")
            print(attacker.name,"took",floor(abs(dmg)),"damage!")
            battle_state()
            sounds.tackle()
            return dmg
def combat_magic_offense(current,enemy):
    base_dmg=0
    for n in range(5):
        roll=random.randint(1,6)
        base_dmg+=roll
    if current==attacker:
        if attacker.matk:
            dmg=base_dmg+(attacker.matk/defender.mdef)
            if game_mode==3:
                defender.hp-=abs(dmg)
            else:
                defender.hp-=abs(dmg)
            print("")
            print("You used a Magic Attack!")
            if game_mode==3:
                print(monster.monster_type(),"took",floor(abs(dmg)),"damage!")
            else:
                print(defender.name,"took",floor(abs(dmg)),"damage!")
            battle_state()
            sounds.magicAttack()
            return dmg
    else:
        if defender.matk:
            dmg=base_dmg+(defender.matk/attacker.mdef)
            attacker.hp-=abs(dmg)
            print("")
            print("The enemy used a Magic Attack!")
            print(attacker.name,"took",floor(abs(dmg)),"damage!")
            battle_state()
            sounds.magicAttack()
            return dmg

def defend(current):
    if current==defender:
        dmg=0
        if dmg<attacker.atk-defender.dfn:
            dmg=attacker.atk-defender.dfn
            dmg*=0.9
            print("")
            print("Reduced damage to",dmg)
            defender.hp-=dmg
            battle_state()
        elif dmg<attacker.matk-defender.mdef:
            dmg=attacker.matk-defender.mdef
            dmg*=0.8
            print("")
            print("Reduced damage to",dmg)
            defender.hp-=dmg
            battle_state()
    else:
        dmg=0
        if dmg<defender.atk-attacker.dfn:
            dmg=defender.atk-attacker.dfn
            dmg*=0.9
            print("")
            print("Reduced damage to",dmg)
            attacker.hp-=dmg
            battle_state()
        elif dmg<defender.matk-attacker.mdef:
            dmg=defender.matk-attacker.mdef
            dmg*=0.8
            print("")
            print("Reduced damage to",dmg)
            attacker.hp-=dmg
            battle_state()

def battle_state():
    if attacker.hp<=0:
        attacker.hp=0
        print(attacker.name,"has",floor(attacker.hp),"hit points!")
    else:
        print(attacker.name,"has",floor(attacker.hp),"hit points!")
    if defender.hp<=0:
        defender.hp=0
        if game_mode==3:
            print(monster.monster_type(), "has",floor(defender.hp),"hit points!")
        else:
            print(defender.name, "has",defender.hp,"hit points!")
    else:
        if game_mode==3:
            print(monster.monster_type(), "has",floor(defender.hp),"hit points!")
        else:
            print(defender.name, "has",floor(defender.hp),"hit points!")

def speed_check(attacker,defender,enemy):
    if game_mode==3:
        if attacker.spd>defender.spd:
            print("You may attack first!")
            battle_options(enemy)
            comp(enemy)
        elif attacker.spd<defender.spd:
            print("The enemy charges forth")
            comp(enemy)
            while attacker.hp<=0:
                break
            else:
                battle_options(enemy)
        else:
            choose=random.randint(1,2)
            if choose=="1":
                print("The enemy makes thier move!")
                comp(enemy)
                while attacker.hp<=0:
                    break
                else:
                    battle_options(enemy)
            else:
                print("")
                print("Your fate had been decided in a coin flip.\nYou may make the first move!")
                print("")
                battle_options(enemy)
                comp(enemy)
    else:
        if attacker.spd>defender.spd:
            print("You may attack first!")
            battle_options(enemy)
            comp(enemy)
        elif attacker.spd<defender.spd:
            print("The enemy charges forth")
            comp(enemy)
            while attacker.hp<=0:
                break
            else:
                battle_options(enemy)
        else:
            choose=random.randint(1,2)
            if choose=="1":
                print("The enemy makes thier move!")
                comp(enemy)
                while attacker.hp<=0:
                    break
                else:
                    battle_options(enemy)
            else:
                print("")
                print("Your fate had been decided in a coin flip.\nYou may make the first move!")
                print("")
                battle_options(enemy)
                comp(enemy)

def comp(enemy):
    # currently does not defend//all offense
    comp_options=random.randint(0,1)
    if comp_options==0:
        combat_offense(defender,enemy)
    elif comp_options==1:
        combat_magic_offense(defender,enemy)
    elif comp_options==2:
        defend(defender)

def battle_options(enemy):
    # battle=["Physical Attack", "Magic Attack","Defend","Flee"]
    print(""" --------------------------------------
| 1.Physical Attack    2.Magic Attack  |
| 3.Defend             4.Inspect       |
--------------------------------------""")
    battle=int(input())
    if battle==1:
        combat_offense(attacker,enemy)
    elif battle==2:
        combat_magic_offense(attacker,enemy)
    elif battle==3:
        defend(attacker)
    elif battle==4:
        if game_mode==3:
            monster.enemy_stats(enemy)
            battle_options(enemy)
        else:
            give_stats(enemy-1)
            battle_options(enemy)
    else:
        print("Definitely not valid, what are you doing?")
        battle_options(enemy)
# End of class #
playerList=["Null"]
Player1=Player("Kyu",100,23,24,56,57,60)
Player2=Player("Varis",100,45,54,34,24,60)
Player3=Player("Y",100,23,25,54,34,90)
Monsta1=monster.Monster("WizCat",1,100,100,100,100,100,100)
def subs():
    global attacker
    global defender
    attacker=Player1
    if game_mode==3:
        defender=Monsta1
    else:
        defender=Player2
def give_stats(num):
    print("")
    print("Name:",playerList[num].name)
    print("HP:",playerList[num].hp)
    print("Attack:",playerList[num].atk)
    print("Defense:",playerList[num].dfn)
    print("Magic Attack:",playerList[num].matk)
    print("Magic Defence:",playerList[num].mdef)
    print("Speed:",playerList[num].spd)
def create_player():
    global attacker
    name=input("Give me a name peasant! =>")
    atk=random.randint(20,100)
    dfn=random.randint(20,100)
    matk=random.randint(20,100)
    mdef=random.randint(20,100)
    spd=random.randint(20,100)
    new_player=Player(name,100,atk,dfn,matk,mdef,spd)
    playerList.append(new_player)
    attacker=playerList[1]
def random_player():
    names=["NorthStar","Ventus","Xero","Anna","Malla","Korrin"]
    for i in range(len(names)):
        atk=random.randint(20,100)
        dfn=random.randint(20,100)
        matk=random.randint(20,100)
        mdef=random.randint(20,100)
        spd=random.randint(20,100)
        new_player=Player(names[i],100,atk,dfn,matk,mdef,spd)
        playerList.append(new_player)
def enemy_assign_manual():
    global defender
    print("")
    for x in range(2,len(playerList)):
        print(x-1,".",playerList[x].name,sep="")
    print("")
    enemy=int(input("Choose an opponent by selecting a number: "))
    if enemy+1>=len(playerList):
        enemy_assign_manual()
    else:
        defender=playerList[enemy+1]
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
    enemy=random.randint(2,len(playerList))
    defender=playerList[enemy]
    return enemy+1
repeat=0
low_health=0
game_mode=0
def main():
    global repeat
    global low_health
    global game_mode
    if repeat==0:
        sounds.background_music(1)
        create_player()
        give_stats(1)
        random_player()
        monster.enemy()
    else:
        sounds.background_music(1)
    pygame.time.wait(1000)
    print("")
    print("""Pick Game Mode:
1.Free Play       2.Random       3.Monsters""")
    print("")
    game_mode=int(input("Choose one: "))
    subs()
    if game_mode==1:
        enemy=enemy_assign_manual()
    elif game_mode==2:
        enemy=enemy_assign_random()
    else:
        enemy=monster.monster_assign_random()
        defender.hp=enemyList[enemy].hp
    pygame.time.wait(1000)
    print("")
    print("Deciding who is moving first...")
    pygame.time.wait(1000)
    print("")
    while attacker.hp!=0 or defender.hp!=0:
        speed_check(attacker,defender,enemy)
        print("")
        if low_health==0:
            if attacker.hp<50:
                pygame.mixer.stop()
                sounds.background_music(2)
                low_health+=1
        if floor(attacker.hp)<=0:
            if game_mode==3:
                attacker.hp=0
                print(monster.monster_type(),"is the winner")
                sounds.defeat()
                break
            else:
                attacker.hp=0
                print(defender.name,"is the winner")
                sounds.defeat()
                break
        elif floor(defender.hp)<=0:
            defender.hp=0
            print(attacker.name,"is the winner")
            sounds.victory()
            break
    pygame.mixer.music.pause()
    restart=int(input("Would you like to start a new battle?(1 for yes): "))
    pygame.mixer.stop()
    repeat+=1
    if restart==1:
        attacker.hp=100
        if game_mode==3:
            defender.hp=enemyList[enemy].hp
        else:
            defender.hp=100
        low_health=0
        main()
### Testing Below ###
main()
# create_player()
# random_player()
# enemy_assign_random()
# print(defender.name)
# for x in range(0,len(playerList)):
#     Player.give_stats(x)
#     print("")
# attacker.combat_offense(attacker,enemy)
