import random
from math import ceil,floor
class Monster:
    def __init__(self,monstertype,rank,hp,atk,dfn,matk,mdef,spd,mxp):
        self.m_type=monstertype
        self.rank=rank
        self.hp=hp
        self.atk=atk
        self.dfn=dfn
        self.matk=matk
        self.mdef=mdef
        self.spd=spd
        self.mxp=mxp
    enemyList=[]
    Rank1=[]
    Rank2=[]
    Rank3=[]
    Rank4=[]
    Rank5=[]
# Enemy Creation and Stats #
def enemy():
    monstertype=["Gooblins","Slime","Cherry Slime","Dragonn","Virus","Jack Squat","Sphiren","Sfiren"]
    for i in range(len(monstertype)):
        for rank in range(1,6):
            if monstertype:
                if rank==1:
                    hp=random.randint(20,30)
                    atk=random.randint(12,18)
                    dfn=random.randint(12,18)
                    matk=random.randint(5,10)
                    mdef=random.randint(5,10)
                    spd=random.randint(10,15)
                    mxp=random.randint(5,8)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd,mxp)
                    Monster.enemyList.append(enemies)
                    Monster.Rank1.append(enemies)
                elif rank==2:
                    hp=random.randint(40,60)
                    atk=random.randint(24,36)
                    dfn=random.randint(24,36)
                    matk=random.randint(15,30)
                    mdef=random.randint(15,30)
                    spd=random.randint(30,45)
                    mxp=random.randint(10,15)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd,mxp)
                    Monster.enemyList.append(enemies)
                    Monster.Rank2.append(enemies)
                elif rank==3:
                    hp=random.randint(70,100)
                    atk=random.randint(72,108)
                    dfn=random.randint(72,108)
                    matk=random.randint(50,100)
                    mdef=random.randint(50,100)
                    spd=random.randint(50,75)
                    mxp=random.randint(40,65)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd,mxp)
                    Monster.enemyList.append(enemies)
                    Monster.Rank3.append(enemies)
                elif rank==4:
                    hp=random.randint(80,120)
                    atk=random.randint(78,117)
                    dfn=random.randint(78,117)
                    matk=random.randint(70,120)
                    mdef=random.randint(70,120)
                    spd=random.randint(75,113)
                    mxp=random.randint(66,90)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd,mxp)
                    Monster.enemyList.append(enemies)
                    Monster.Rank4.append(enemies)
                elif rank==5:
                    hp=random.randint(120,180)
                    atk=random.randint(84,126)
                    dfn=random.randint(84,126)
                    matk=random.randint(100,150)
                    mdef=random.randint(100,150)
                    spd=random.randint(87,130)
                    mxp=random.randint(100,131)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd,mxp)
                    Monster.enemyList.append(enemies)
                    Monster.Rank5.append(enemies)

def enemy_stats(num):
    print("\nMonster Type:",Monster.enemyList[num].m_type,"\nRank:",Monster.enemyList[num].rank)
    print("HP:",Monster.enemyList[num].hp,"\nAttack:",Monster.enemyList[num].atk)
    print("Defense:",Monster.enemyList[num].dfn,"\nMagic Attack:",Monster.enemyList[num].matk)
    print("Magic Defence:",Monster.enemyList[num].mdef,"\nSpeed:",Monster.enemyList[num].spd)
    # print(Monster.enemyList[num].mxp)

def rankStats(num):
    if defender.rank==1:
        print("\nMonster Type:",Monster.Rank1[num].m_type,"\nRank:",Monster.Rank1[num].rank)
        print("HP:",Monster.Rank1[num].hp,"\nAttack:",Monster.Rank1[num].atk)
        print("Defense:",Monster.Rank1[num].dfn,"\nMagic Attack:",Monster.Rank1[num].matk)
        print("Magic Defence:",Monster.Rank1[num].mdef,"\nSpeed:",Monster.Rank1[num].spd)
    elif defender.rank==2:
        print("\nMonster Type:",Monster.Rank2[num].m_type,"\nRank:",Monster.Rank2[num].rank)
        print("HP:",Monster.Rank2[num].hp,"\nAttack:",Monster.Rank2[num].atk)
        print("Defense:",Monster.Rank2[num].dfn,"\nMagic Attack:",Monster.Rank2[num].matk)
        print("Magic Defence:",Monster.Rank2[num].mdef,"\nSpeed:",Monster.Rank2[num].spd)
    elif defender.rank==3:
        print("\nMonster Type:",Monster.Rank3[num].m_type,"\nRank:",Monster.Rank3[num].rank)
        print("HP:",Monster.Rank3[num].hp,"\nAttack:",Monster.Rank3[num].atk)
        print("Defense:",Monster.Rank3[num].dfn,"\nMagic Attack:",Monster.Rank3[num].matk)
        print("Magic Defence:",Monster.Rank3[num].mdef,"\nSpeed:",Monster.Rank3[num].spd)
    elif defender.rank==4:
        print("\nMonster Type:",Monster.Rank4[num].m_type,"\nRank:",Monster.Rank4[num].rank)
        print("HP:",Monster.Rank4[num].hp,"\nAttack:",Monster.Rank4[num].atk)
        print("Defense:",Monster.Rank4[num].dfn,"\nMagic Attack:",Monster.Rank4[num].matk)
        print("Magic Defence:",Monster.Rank4[num].mdef,"\nSpeed:",Monster.Rank4[num].spd)
    elif defender.rank==5:
        print("\nMonster Type:",Monster.Rank5[num].m_type,"\nRank:",Monster.Rank5[num].rank)
        print("HP:",Monster.Rank5[num].hp,"\nAttack:",Monster.Rank5[num].atk)
        print("Defense:",Monster.Rank5[num].dfn,"\nMagic Attack:",Monster.Rank5[num].matk)
        print("Magic Defence:",Monster.Rank5[num].mdef,"\nSpeed:",Monster.Rank5[num].spd)
# Enemy Assignment #
def monster_assign_random():
    global defender
    enemy=random.randint(0,len(Monster.enemyList)-1)
    defender=Monster.enemyList[enemy]
    return enemy
def rank1Assign():
    global defender
    enemy=random.randint(0,len(Monster.Rank1)-1)
    defender=Monster.Rank1[enemy]
    return enemy
def rank2Assign():
    global defender
    enemy=random.randint(0,len(Monster.Rank2)-1)
    defender=Monster.Rank2[enemy]
    return enemy
def rank3Assign():
    global defender
    enemy=random.randint(0,len(Monster.Rank3)-1)
    defender=Monster.Rank3[enemy]
    return enemy
def rank4Assign():
    global defender
    enemy=random.randint(0,len(Monster.Rank4)-1)
    defender=Monster.Rank4[enemy]
    return enemy
def rank5Assign():
    global defender
    enemy=random.randint(0,len(Monster.Rank5)-1)
    defender=Monster.Rank5[enemy]
    return enemy
def monster_type():
    return defender.m_type

def xpGain(num):
    if defender.rank==1:
        xp=Monster.Rank1[num].mxp
    elif defender.rank==2:
        xp=Monster.Rank2[num].mxp
    elif defender.rank==3:
        xp=Monster.Rank3[num].mxp
    elif defender.rank==4:
        xp=Monster.Rank4[num].mxp
    elif defender.rank==5:
        xp=Monster.Rank5[num].mxp
    return xp
def healthReset(num):
    if defender.rank==1:
        health=Monster.Rank1[num].hp
    elif defender.rank==2:
        health=Monster.Rank2[num].hp
    elif defender.rank==3:
        health=Monster.Rank3[num].hp
    elif defender.rank==4:
        health=Monster.Rank4[num].hp
    elif defender.rank==5:
        health=Monster.Rank5[num].hp
    return health
def in_sphere_mode(counter,sphere_mode):
    if defender.m_type == "Sphiren" or defender.m_type == "Sfiren" :
        if sphere_mode==False and defender.hp!=0:
            if counter%3==0:
                print(defender.m_type,"is now in sphere mode!\n")
                defender.atk=floor(defender.atk*0.5)
                defender.matk=floor(defender.matk*0.5)
                defender.dfn=floor(defender.dfn*1.5)
                defender.mdef=floor(defender.mdef*1.5)
                return True
            else:
                return False
        else:
            if counter%5==0:
                print(defender.m_type, "is no longer in sphere mode!\n")
                defender.atk=ceil(defender.atk*2)
                defender.matk=ceil(defender.matk*2)
                defender.dfn=ceil(defender.dfn/1.5)
                defender.mdef=ceil(defender.mdef/1.5)
                return False
            else:
                return True

# def recovery(maxHealth_D):
#     if defender.m_type == "Jack Squat":
#         heal=random.randint(14,30)
#         defender.hp+=heal
#         if defender.hp>=maxHealth_D:
#             defender.hp=maxHealth_D
#         print("Jack Squat healed",heal,"hit points!")
#     elif defender.m_type=="Dragonn":
#         heal=floor(maxHealth_D*0.4)
#         defender.hp+=heal
#         if defender.hp>=maxHealth_D:
#             defender.hp=maxHealth_D
#         print("Dragonn healed",heal,"hit points!")

# enemy()
# sphere_mode=False
# defender=Monster.enemyList[6]
# defender.hp=45
# counter=1
# while defender.hp!=0:
#     print("\nTurn",counter,"\n")
#     counter+=1
#     sphere_mode=in_sphere_mode(counter,sphere_mode)
#     print(sphere_mode)
#     defender.hp-=5
# enemy_stats(6)
# print(len(Monster.enemyList))
# for x in range (0,10):
#     enemy=monster_assign_random()
#     print(x,enemy)
# rank1Assign()
# for x in range(0,len(Monster.Rank1)):
#     rankStats(x)
