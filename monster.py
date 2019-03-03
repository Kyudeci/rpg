import random
from math import ceil,floor
class Monster:
    def __init__(self,monstertype,rank,hp,atk,dfn,matk,mdef,spd):
        self.m_type=monstertype
        self.rank=rank
        self.hp=hp
        self.atk=atk
        self.dfn=dfn
        self.matk=matk
        self.mdef=mdef
        self.spd=spd
enemyList=[]
def enemy():
    monstertype=["Gooblins","Slime","Cherry Slime","Dragonn","Virus","Jack Squat","Sphiren","Sfiren"]
    for x in range(1):
        for i in range(len(monstertype)):
            if monstertype:
                rank=random.randint(1,5)
                if rank==1:
                    hp=random.randint(20,30)
                    atk=random.randint(12,18)
                    dfn=random.randint(12,18)
                    matk=random.randint(5,10)
                    mdef=random.randint(5,10)
                    spd=random.randint(10,15)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd)
                    enemyList.append(enemies)
                elif rank==2:
                    hp=random.randint(40,60)
                    atk=random.randint(24,36)
                    dfn=random.randint(24,36)
                    matk=random.randint(15,30)
                    mdef=random.randint(15,30)
                    spd=random.randint(30,45)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd)
                    enemyList.append(enemies)
                elif rank==3:
                    hp=random.randint(70,100)
                    atk=random.randint(72,108)
                    dfn=random.randint(72,108)
                    matk=random.randint(50,100)
                    mdef=random.randint(50,100)
                    spd=random.randint(50,75)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd)
                    enemyList.append(enemies)
                elif rank==4:
                    hp=random.randint(80,120)
                    atk=random.randint(78,117)
                    dfn=random.randint(78,117)
                    matk=random.randint(70,120)
                    mdef=random.randint(70,120)
                    spd=random.randint(75,113)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd)
                    enemyList.append(enemies)
                elif rank==5:
                    hp=random.randint(120,180)
                    atk=random.randint(84,126)
                    dfn=random.randint(84,126)
                    matk=random.randint(100,150)
                    mdef=random.randint(100,150)
                    spd=random.randint(80,120)
                    enemies=Monster(monstertype[i],rank,hp,atk,dfn,matk,mdef,spd)
                    enemyList.append(enemies)

def enemy_stats(num):
    print("")
    print("Monster Type:",enemyList[num].m_type)
    print("Rank:",enemyList[num].rank)
    print("HP:",enemyList[num].hp)
    print("Attack:",enemyList[num].atk)
    print("Defense:",enemyList[num].dfn)
    print("Magic Attack:",enemyList[num].matk)
    print("Magic Defence:",enemyList[num].mdef)
    print("Speed:",enemyList[num].spd)
def monster_assign_random():
    global defender
    enemy=random.randint(0,len(enemyList)-1)
    defender=enemyList[enemy]
    return enemy
def monster_type():
    return defender.m_type

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
# def exit_sphere_mode(counter):
#     if sphere_mode==True:
# enemy()
# sphere_mode=False
# defender=enemyList[6]
# defender.hp=45
# counter=1
# while defender.hp!=0:
#     print("\nTurn",counter,"\n")
#     counter+=1
#     sphere_mode=in_sphere_mode(counter,sphere_mode)
#     print(sphere_mode)
#     defender.hp-=5
# enemy_stats(6)
# print(len(enemyList))
# for x in range (0,10):
#     enemy=monster_assign_random()
#     print(x,enemy)
# for x in range(0,len(enemyList)):
#     enemy_stats(x)
#     print("")
