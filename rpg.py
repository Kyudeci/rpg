import random
import pygame
import sounds
import monster
import moves
import sys
import pickle
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
        self.lvl=1
        self.xp=0
        self.lvlNext=25
        self.karma=0
    playerList=[]

    def levelUp(self,xp):
        self.xp+=xp
        while self.xp>=self.lvlNext:
            self.lvl+=1
            self.xp=self.xp-self.lvlNext
            self.lvlNext=floor(self.lvlNext*1.5)
            print("\nYou are now level",self.lvl)
            print("Exp:",self.xp)
            print("Next Level:",self.lvlNext,"\n")
            stat_attribute=[self.atk,self.dfn,self.matk,self.mdef,self.spd]
            for x in range(len(stat_attribute)):
                stat=["\nAttack:","Defense:","Magic Attack:","Magic Defense:","Speed:"]
                increase=random.randint(0,3)
                print(stat[x],stat_attribute[x],"+",increase)
                if stat[x]==stat[0]:
                    self.atk+=increase
                elif stat[x]==stat[1]:
                    self.dfn+=increase
                elif stat[x]==stat[2]:
                    self.matk+=increase
                elif stat[x]==stat[3]:
                    self.mdef+=increase
                elif stat[x]==stat[4]:
                    self.spd+=increase

def combat_offense(current,enemy,maxHealth_A,maxHealth_D,comp_options):
    base_dmg=0
    for n in range(3):
        roll=random.randint(1,6)
        base_dmg+=roll
    if current==attacker:
        if attacker.atk:
            if attacker.atk==defender.dfn:
                dmg=floor((100/(attacker.atk-(defender.dfn+1)))*base_dmg*(attacker.lvl/6))
            else:
                dmg=floor((100/(attacker.atk-defender.dfn))*base_dmg*(attacker.lvl/6))
            if game_mode==3:
                defender.hp-=abs(dmg)
            else:
                defender.hp-=abs(dmg)
            print("")
            print("You used a Physical Attack!")
            if game_mode==3:
                print(monster.monster_type(),"took",floor(abs(dmg)),"damage!\n")
            else:
                print(defender.name,"took",floor(abs(dmg)),"damage!\n")
            battle_state(maxHealth_A,maxHealth_D)
            sounds.punch()
            return dmg
    else:
        if defender.atk:
            if game_mode==3:
                if monster.monster_type()=="Jack Squat":
                    base_dmg=moves.js_moves(comp_options,enemy,maxHealth_D)
                elif monster.monster_type()=="Gooblins":
                    base_dmg=moves.gob_moves(comp_options)
                elif monster.monster_type()=="Dragonn":
                    base_dmg=moves.dg_moves(comp_options,maxHealth_D)
                    if base_dmg==2:
                        base_dmg=random.randint(12,16)
                        defender.dfn=defender.dfn*0.8
                if base_dmg==0:
                    dmg=0
                else:
                    if defender.atk==attacker.dfn:
                        dmg=floor((75/(defender.atk-(attacker.dfn+1)))*base_dmg*(defender.rank/8))
                    else:
                        dmg=floor((75/(defender.atk-attacker.dfn))*base_dmg*(defender.rank/8))
            else:
                if defender.atk==attacker.dfn:
                    dmg=floor((75/(defender.atk-(attacker.dfn+1)))*base_dmg)
                else:
                    dmg=floor((75/(defender.atk-attacker.dfn))*base_dmg)
            attacker.hp-=abs(dmg)
            print("")
            if game_mode==1 or game_mode==2:
                print("The enemy used a Physical Attack!")
            print(attacker.name,"took",floor(abs(dmg)),"damage!\n")
            battle_state(maxHealth_A,maxHealth_D)
            sounds.tackle()
            return dmg
def combat_magic_offense(current,enemy,maxHealth_A,maxHealth_D,comp_options):
    base_dmg=0
    for n in range(3):
        roll=random.randint(1,6)
        base_dmg+=roll
    if current==attacker:
        if attacker.matk:
            if attacker.matk==defender.mdef:
                dmg=floor((100/(attacker.matk-(defender.mdef+1)))*base_dmg*(attacker.lvl/6))
            else:
                dmg=floor((100/(attacker.matk-defender.mdef))*base_dmg*(attacker.lvl/6))
            if game_mode==3:
                defender.hp-=abs(dmg)
            else:
                defender.hp-=abs(dmg)
            print("")
            print("You used a Magic Attack!")
            if game_mode==3:
                print(monster.monster_type(),"took",floor(abs(dmg)),"damage!\n")
            else:
                print(defender.name,"took",floor(abs(dmg)),"damage!\n")
            battle_state(maxHealth_A,maxHealth_D)
            sounds.magicAttack()
            return dmg
    else:
        if defender.matk:
            if game_mode==3:
                if monster.monster_type()=="Jack Squat":
                    base_dmg=moves.js_moves(comp_options,enemy,maxHealth_D)
                elif monster.monster_type()=="Gooblins":
                    base_dmg=moves.gob_moves(comp_options)
                elif monster.monster_type()=="Dragonn":
                    base_dmg=moves.dg_moves(comp_options,maxHealth_D)
                    if base_dmg==1:
                        base_dmg=0
                        print("Run....")
                if base_dmg<0:
                    base_dmg=0
                    heal=random.randint(14,30)
                    defender.hp+=heal
                    if defender.hp>maxHealth_D:
                        defender.hp=maxHealth_D
                    print(monster.monster_type(),"recovered health!")
                else:
                    if defender.matk==attacker.mdef:
                        dmg=floor((75/(defender.matk-(attacker.mdef+1)))*base_dmg*(defender.rank/8))
                    else:
                        dmg=floor((75/(defender.matk-attacker.mdef))*base_dmg*(defender.rank/8))
                    attacker.hp-=abs(dmg)
                    print(attacker.name,"took",floor(abs(dmg)),"damage!\n")
            else:
                if defender.matk==attacker.mdef:
                    dmg=floor((75/(defender.matk-(attacker.mdef+1)))*base_dmg)
                else:
                    dmg=floor((75/(defender.matk-attacker.mdef))*base_dmg)
                attacker.hp-=abs(dmg)
                print(attacker.name,"took",floor(abs(dmg)),"damage!\n")
            print("")
            battle_state(maxHealth_A,maxHealth_D)
            sounds.magicAttack()
            return

def defend(current,maxHealth_A,maxHealth_D):
    if current==defender:
        dmg=0
        if dmg<attacker.atk-defender.dfn:
            dmg=attacker.atk-defender.dfn
            dmg*=0.9
            print("")
            print("Reduced damage to",dmg)
            defender.hp-=dmg
            battle_state(maxHealth_A,maxHealth_D)
        elif dmg<attacker.matk-defender.mdef:
            dmg=attacker.matk-defender.mdef
            dmg*=0.8
            print("")
            print("Reduced damage to",dmg)
            defender.hp-=dmg
            battle_state(maxHealth_A,maxHealth_D)
    else:
        dmg=0
        if dmg<defender.atk-attacker.dfn:
            dmg=defender.atk-attacker.dfn
            dmg*=0.9
            print("")
            print("Reduced damage to",dmg)
            attacker.hp-=dmg
            battle_state(maxHealth_A,maxHealth_D)
        elif dmg<defender.matk-attacker.mdef:
            dmg=defender.matk-attacker.mdef
            dmg*=0.8
            print("")
            print("Reduced damage to",dmg)
            attacker.hp-=dmg
            battle_state(maxHealth_A,maxHealth_D)
def battle_state(maxHealth_A,maxHealth_D):
    if attacker.hp<=0:
        attacker.hp=0
        health_A(maxHealth_A)
    else:
        health_A(maxHealth_A)
    if defender.hp<=0:
        defender.hp=0
        if game_mode==3:
            health_D(game_mode,maxHealth_D)
        else:
            health_D(game_mode,maxHealth_D)
    else:
        if game_mode==3:
            health_D(game_mode,maxHealth_D)
        else:
            health_D(game_mode,maxHealth_D)
def health_A(maxHealth_A):
    healthDashes = 20
    CEND = '\033[0m'
    CRED2='\33[91m'
    CGREEN2='\33[92m'
    CYELLOW2='\33[93m'
    dashConvert = int(maxHealth_A/healthDashes)
    currentDashes = int(attacker.hp/dashConvert)
    remainingHealth = healthDashes - currentDashes

    healthDisplay = ''.join(['█' for i in range(currentDashes)])
    remainingDisplay = ''.join([' ' for i in range(remainingHealth)])
    percent = str(int((attacker.hp/maxHealth_A)*100)) + "%"
    print(attacker.name)
    if attacker.hp>66:
        print("|" +CGREEN2+ healthDisplay + remainingDisplay +CEND+ "|" + percent)
    elif attacker.hp>33:
        print("|" +CYELLOW2+ healthDisplay + remainingDisplay + CEND+ "|" + percent)
    else:
        print("|" +CRED2+ healthDisplay + remainingDisplay + CEND+ "|" + percent)
def health_D(game_mode,maxHealth_D):
    healthDashes = 20
    CEND = '\033[0m'
    CRED2='\33[91m'
    CGREEN2='\33[92m'
    CYELLOW2='\33[93m'
    if game_mode==3:
        dashConvert = int(maxHealth_D/healthDashes)
        currentDashes = int(defender.hp/dashConvert)
        remainingHealth = healthDashes - currentDashes

        healthDisplay = ''.join(['█' for i in range(currentDashes)])
        remainingDisplay = ''.join([' ' for i in range(remainingHealth)])
        percent = str(int((defender.hp/maxHealth_D)*100)) + "%\n"
        print(monster.monster_type())
        if defender.hp>0.66*maxHealth_D:
            print("|" +CGREEN2+ healthDisplay + remainingDisplay +CEND+ "|" + percent)
        elif defender.hp>0.33*maxHealth_D:
            print("|" +CYELLOW2+ healthDisplay + remainingDisplay + CEND+ "|" + percent)
        else:
            print("|" +CRED2+ healthDisplay + remainingDisplay + CEND+ "|" + percent)
    else:
        dashConvert = int(maxHealth_D/healthDashes)
        currentDashes = int(defender.hp/dashConvert)
        remainingHealth = healthDashes - currentDashes

        healthDisplay = ''.join(['█' for i in range(currentDashes)])
        remainingDisplay = ''.join([' ' for i in range(remainingHealth)])
        percent = str(int((defender.hp/maxHealth_D)*100)) + "%\n"
        print(defender.name)
        if defender.hp>66:
            print("|" +CGREEN2+ healthDisplay + remainingDisplay +CEND+ "|" + percent)
        elif defender.hp>33:
            print("|" +CYELLOW2+ healthDisplay + remainingDisplay + CEND+ "|" + percent)
        else:
            print("|" +CRED2+ healthDisplay + remainingDisplay + CEND+ "|" + percent)
def speed_check(attacker,defender,enemy,maxHealth_A,maxHealth_D,comp_options):
    if game_mode==3:
        if attacker.spd>defender.spd:
            print("You may attack first!")
            battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
            comp(enemy,maxHealth_A,maxHealth_D)
        elif attacker.spd<defender.spd:
            print("The enemy charges forth")
            comp(enemy,maxHealth_A,maxHealth_D)
            while attacker.hp<=0:
                break
            else:
                battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
        else:
            choose=random.randint(1,2)
            if choose=="1":
                print("The enemy makes thier move!")
                comp(enemy,maxHealth_A,maxHealth_D)
                while attacker.hp<=0:
                    break
                else:
                    battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
            else:
                print("")
                print("Your fate had been decided in a coin flip.\nYou may make the first move!")
                print("")
                battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
                comp(enemy,maxHealth_A,maxHealth_D)
    else:
        if attacker.spd>defender.spd:
            print("You may attack first!")
            battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
            comp(enemy,maxHealth_A,maxHealth_D)
        elif attacker.spd<defender.spd:
            print("The enemy charges forth")
            comp(enemy,maxHealth_A,maxHealth_D)
            while attacker.hp<=0:
                break
            else:
                battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
        else:
            choose=random.randint(1,2)
            if choose=="1":
                print("The enemy makes thier move!")
                comp(enemy,maxHealth_A,maxHealth_D)
                while attacker.hp<=0:
                    break
                else:
                    battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
            else:
                print("")
                print("Your fate had been decided in a coin flip.\nYou may make the first move!")
                print("")
                battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
                comp(enemy,maxHealth_A,maxHealth_D)

def comp(enemy,maxHealth_A,maxHealth_D):
    # currently does not defend//all offense
    comp_options=random.randint(0,1)
    if comp_options==0:
        combat_offense(defender,enemy,maxHealth_A,maxHealth_D,comp_options)
    elif comp_options==1:
        combat_magic_offense(defender,enemy,maxHealth_A,maxHealth_D,comp_options)
    elif comp_options==2:
        defend(defender,maxHealth_A,maxHealth_D)

def battle_options(enemy,maxHealth_A,maxHealth_D,comp_options):
    # battle=["Physical Attack", "Magic Attack","Defend","Flee"]
    print("""■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■
■  1.Physical Attack    2.Magic Attack  ■
■  3.Defend             4.Inspect       ■
■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■ ■  """)
    battle=int(input())
    if battle==1:
        combat_offense(attacker,enemy,maxHealth_A,maxHealth_D,comp_options)
    elif battle==2:
        combat_magic_offense(attacker,enemy,maxHealth_A,maxHealth_D,comp_options)
    elif battle==3:
        defend(attacker,maxHealth_A,maxHealth_D)
    elif battle==4:
        if game_mode==3:
            monster.enemy_stats(enemy)
            battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
        else:
            give_stats(enemy)
            battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
    else:
        print("Definitely not valid, what are you doing?")
        battle_options(enemy,maxHealth_A,maxHealth_D,comp_options)
Origin=Player("Meikahs",999,999,999,999,999,999)
Player.playerList.append(Origin)
Player1=Player("Kyu",100,23,24,56,57,60)
Player2=Player("Varis",100,45,54,34,24,60)
Player3=Player("Y",100,23,25,54,34,90)
Monsta1=monster.Monster("WizCat",1,100,100,100,100,100,100,34)
def save(player,plist,elist):
    player=attacker
    plist=Player.playerList
    elist=monster.Monster.enemyList
    with open('savefile.dat', 'wb') as f:
        pickle.dump([player,plist,elist], f, protocol=2)
def load():
    with open('savefile.dat', 'rb') as f:
        player,plist,elist = pickle.load(f)
        for x in range(1,len(plist)):
            Player.playerList.append(plist[x])
        for y in range(0,len(elist)):
            monster.Monster.enemyList.append(elist[y])
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
def subs():
    global defender
    if game_mode==3:
        defender=Monsta1
    else:
        defender=Player2
def give_stats(num):
    print("\nName:",Player.playerList[num].name,"\nLevel:",Player.playerList[num].lvl)
    print("HP:",Player.playerList[num].hp,"\nAttack:",Player.playerList[num].atk)
    print("Defense:",Player.playerList[num].dfn,"\nMagic Attack:",Player.playerList[num].matk)
    print("Magic Defence:",Player.playerList[num].mdef,"\nSpeed:",Player.playerList[num].spd)
    print(Player.playerList[num].karma)
def create_player():
    global attacker
    name=input("Meikahs: What is your name by chance? =>")
    if len(name)<3:
        print("Your name is too short.")
        return create_player()
    atk=random.randint(20,100)
    dfn=random.randint(20,100)
    matk=random.randint(20,100)
    mdef=random.randint(20,100)
    spd=random.randint(20,100)
    new_player=Player(name,100,atk,dfn,matk,mdef,spd)
    Player.playerList.append(new_player)
    attacker=Player.playerList[1]
    return name
def random_player():
    names=["NorthStar","Ventus","Xero","Anna","Malla","Korrin"]
    for i in range(len(names)):
        atk=random.randint(20,100)
        dfn=random.randint(20,100)
        matk=random.randint(20,100)
        mdef=random.randint(20,100)
        spd=random.randint(20,100)
        new_player=Player(names[i],100,atk,dfn,matk,mdef,spd)
        Player.playerList.append(new_player)
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
def mainMenu():
    print("""
      █
     ███
    █████
    █████
    █████
    █████      Welcome to the Indev Battlesim/RPG V1.5!
    █████
 █  ██●██  █
  ███●●●███
     ███
      █
      █
    █ █ █
     ███ \n""")
    print("Currently only Monsters give experience.\n")
    if is_accessible('savefile.dat')==True:
        print("1.Start\n2.Load\n3.Save\n4.Quit")
        choice=int(input(">"))
        if choice==1:
            gameStart(False)
        elif choice==2:
            l_check=load()
            gameStart(l_check)
        elif choice==3:
            save(attacker,Player.playerList,monster.Monster.enemyList)
        elif choice==4:
            sys.exit()
    else:
        print("1.Start\n2.Quit")
        choice=int(input(">"))
        if choice==1:
            gameStart(False)
def gameStart(l_check):
    if l_check==False:
        sounds.background_music(1)
        create_player()
        give_stats(1)
        random_player()
        monster.enemy()
        vfr=monster.Monster.enemyList
        save(attacker,Player.playerList,vfr)
    else:
        main()
    main()
repeat=0
low_health=0
game_mode=0
def main():
    global repeat, low_health, game_mode, attacker
    attacker=Player.playerList[1]
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
    elif game_mode==3:
        enemy=monster.monster_assign_random()
        defender.hp=monster.Monster.enemyList[enemy].hp
    maxHealth_A=100
    maxHealth_D=defender.hp
    pygame.time.wait(1000)
    print("")
    print("Deciding who is moving first...")
    pygame.time.wait(1000)
    print("")
    counter=1
    sphere_mode=False
    while attacker.hp!=0 or defender.hp!=0:
        print("Turn",counter,"\n")
        counter+=1
        speed_check(attacker,defender,enemy,maxHealth_A,maxHealth_D,1)
        print("")
        if game_mode==3:
            sphere_mode=monster.in_sphere_mode(counter,sphere_mode)
        if low_health==0:
            if attacker.hp<50:
                pygame.mixer.stop()
                sounds.background_music(2)
                low_health+=1
        if floor(attacker.hp)<=0:
            if game_mode==3:
                attacker.hp=0
                print(monster.monster_type(),"is the winner")
                xp=floor(monster.Monster.enemyList[enemy].mxp*0.25)
                attacker.hp=maxHealth_A
                give_stats(1)
                print("You earned",xp,"exp. points!\n")
                attacker.levelUp(xp)
                give_stats(1)
                sounds.defeat()
                break
            else:
                attacker.hp=0
                print(defender.name,"is the winner")
                sounds.defeat()
                break
        elif floor(defender.hp)<=0:
            defender.hp=0
            print(attacker.name,"is the winner\n")
            if game_mode==3:
                xp=monster.Monster.enemyList[enemy].mxp
                attacker.hp=maxHealth_A
                give_stats(1)
                print("You earned",xp,"exp. points!\n")
                attacker.levelUp(xp)
                give_stats(1)
            sounds.victory()
            break
    pygame.mixer.music.pause()
    restart=int(input("\nWould you like to start a new battle?(1 for yes): "))
    pygame.mixer.stop()
    repeat+=1
    if restart==1:
        attacker.hp=maxHealth_A
        if game_mode==3:
            defender.hp=50
        else:
            defender.hp=100
        low_health=0
        save(attacker,Player.playerList,monster.Monster.enemyList)
        return main()
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
