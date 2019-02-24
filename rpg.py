import random
import pygame
import sounds
from math import floor, ceil
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
        self.playerList=[]
    def combat_offense(self,current):
        base_dmg=0
        for n in range(5):
            roll=random.randint(1,6)
            base_dmg+=roll
        if current==attacker:
            if attacker.atk:
                dmg=(base_dmg+(attacker.atk*0.2))-(defender.dfn*0.6)
                defender.hp-=abs(dmg*2)
                print("")
                print("You used a Physical Attack!")
                print(defender.name,"took",ceil(abs(dmg*2)),"damage!")
                attacker.battle_state()
                sounds.punch()
                return dmg
        else:
            if defender.atk:
                dmg=(base_dmg+(defender.atk*0.2))-(attacker.dfn*0.6)
                attacker.hp-=abs(dmg*2)
                print("")
                print("The enemy used a Physical Attack!")
                print(attacker.name,"took",ceil(abs(dmg*2)),"damage!")
                defender.battle_state()
                sounds.tackle()
                return dmg
    def combat_magic_offense(self,current):
        base_dmg=0
        for n in range(5):
            roll=random.randint(1,6)
            base_dmg+=roll
        if current==attacker:
            if attacker.matk:
                dmg=(base_dmg+(attacker.matk*0.2))-(defender.mdef*0.6)
                defender.hp-=abs(dmg*2)
                print("")
                print("You used a Magic Attack!")
                print(defender.name,"took",ceil(abs(dmg*2)),"damage!")
                attacker.battle_state()
                sounds.magicAttack()
                return dmg
        else:
            if defender.matk:
                dmg=(base_dmg+(defender.matk*0.2))-(attacker.mdef*0.6)
                attacker.hp-=abs(dmg*2)
                print("")
                print("The enemy used a Magic Attack!")
                print(attacker.name,"took",ceil(abs(dmg*2)),"damage!")
                defender.battle_state()
                sounds.magicAttack()
                return dmg

    def defend(self,current):
        if current==defender:
            dmg=0
            if dmg<attacker.atk-defender.dfn:
                dmg=attacker.atk-defender.dfn
                dmg*=0.9
                print("")
                print("Reduced damage to",dmg)
                defender.hp-=dmg
                attacker.battle_state()
            elif dmg<attacker.matk-defender.mdef:
                dmg=attacker.matk-defender.mdef
                dmg*=0.8
                print("")
                print("Reduced damage to",dmg)
                defender.hp-=dmg
                attacker.battle_state()
        else:
            dmg=0
            if dmg<defender.atk-attacker.dfn:
                dmg=defender.atk-attacker.dfn
                dmg*=0.9
                print("")
                print("Reduced damage to",dmg)
                attacker.hp-=dmg
                defender.battle_state()
            elif dmg<defender.matk-attacker.mdef:
                dmg=defender.matk-attacker.mdef
                dmg*=0.8
                print("")
                print("Reduced damage to",dmg)
                attacker.hp-=dmg
                defender.battle_state()

    def battle_state(self):
        if attacker.hp<=0:
            attacker.hp=0
            print(attacker.name,"has",attacker.hp,"hit points!")
        else:
            print(attacker.name,"has",floor(attacker.hp),"hit points!")
        if defender.hp<=0:
            defender.hp=0
            print(defender.name, "has",defender.hp,"hit points!")
        else:
            print(defender.name, "has",floor(defender.hp),"hit points!")

    def speed_check(self,attacker,defender):
        if attacker.spd>defender.spd:
            print("You may attack first!")
            attacker.battle_options()
            defender.comp()
        elif attacker.spd<defender.spd:
            print("The enemy charges forth")
            defender.comp()
            attacker.battle_options()
        else:
            choose=random.randint(1,2)
            if choose=="1":
                defender.comp()
            else:
                attacker.battle_options()

    def comp(self):
        # currently does not defend//all offense
        comp_options=random.randint(0,1)
        if comp_options==0:
            defender.combat_offense(defender)
        elif comp_options==1:
            defender.combat_magic_offense(defender)
        elif comp_options==2:
            defender.defend(defender)

    def battle_options(self):
        # battle=["Physical Attack", "Magic Attack","Defend","Flee"]
        print(""" --------------------------------------
| 1.Physical Attack    2.Magic Attack  |
| 3.Defend             4.Flee          |
 --------------------------------------""")
        battle=int(input())
        if battle==1:
            attacker.combat_offense(attacker)
        elif battle==2:
            attacker.combat_magic_offense(attacker)
        elif battle==3:
            attacker.defend(attacker)
        elif battle==4:
            print("Hahahahaha There is no running!")
            attacker.battle_options()
        else:
            print("Definitely not valid, what is you doing?")
            attacker.battle_options()
Player1=Player("Kyu",100,23,24,56,57,60)
Player2=Player("Varis",100,45,54,34,24,60)
Player3=Player("Y",100,23,25,54,34,90)
attacker=Player1
defender=Player3
# Figure out how to create a list of players and append each new created player
def general():
    name=input("Give me a name peasant! =>")
    atk=random.randint(20,100)
    dfn=random.randint(20,100)
    matk=random.randint(20,100)
    mdef=random.randint(20,100)
    spd=random.randint(20,100)
    new_player=Player(name,100,atk,dfn,matk,mdef,spd)
    return new_player
    # print(new_player.name)
    # confirm=input("Do you wish to fight?")
# attacker.battle_options(attacker,defender)
def main():
    print("Skipping character creation...")
    sounds.background_music(1)
    pygame.time.wait(2000)
    print("")
    print("Deciding who is moving first...")
    pygame.time.wait(4000)
    print("")
    while attacker.hp!=0 or defender.hp!=0:
        attacker.speed_check(attacker,defender)
        print("")
        if attacker.hp<=0:
            attacker.hp=0
            print(defender.name,"is the winner")
            sounds.victory()
            break
        elif defender.hp<=0:
            defender.hp=0
            print(attacker.name,"is the winner")
            sounds.victory()
            break
    pygame.mixer.music.pause()
    restart=int(input("Would you like to start a new battle?(1 for yes): "))
    pygame.mixer.stop()
    if restart==1:
        attacker.hp=100
        defender.hp=100
        main()

main()
# attacker.combat_offense(attacker)

# Flee function should to changed to dodge/evade, chance 50%, set damage equal to zero --Savon
# Change attack/defense comparison to dice rolls where the sum is multplied by a fraction of the attackers atk/matk--Creator
# In the event that we implement crits every point of luck will be 0.33%--Savon
# https://codereview.stackexchange.com/questions/94116/turn-based-battle-simulator
# Either create a new function or append main() that switches the players which will be saved in a list
# Nice to have: dynamic music shift at low health
