import random
import monster as mon
from tkinter import *
from tkinter import messagebox
import math
jsPhys = {'Nil!': "Jack Squat lounges about...",'Squat!': random.randint(10,15),'Exist!': random.randint(5,10)}
jsMagic = {'Nil!': "Jack Squat lounges about...",'Schwave!': random.randint(20,25),'Sleep!': "Heal"}

gbPhys = {'Gooblin Attack Force!': random.randint(2,20),'Pointy Assaulturu!': random.randint(5,16),'Full Charge!': 'Who knows?'}
gbMagic = {'Gooblin Magic Force!': random.randint(2,20),'Magiku Assaulturu!': random.randint(5,16), 'Fireballs!': 'What will it be?' }

dgPhys = {"Aerial Strike!": random.randint(15,21),"Shatter Scales!": random.randint(12,16),"Dragonn's Fury!":random.randint(37,45)}
dgMagic = {"Leftovers!": "+baseHP*0.4", "Bye!": "Dragonn makes its exit!", "Dragonn's Breath": random.randint(13,18)}

spfPhys = {"Sphere Volley!": random.randint(10,20),"Resolution!": 50,"Sea Sharp!": random.randint(9,25),"Blazing Notes!":random.randint(9,25)}
spfMagic = {"Resonating Rings!": random.randint(12,20),"Lunarchestry!": 1.2,"Ocean's Wail!": random.randint(3,26),"Heliosymphony!":1.2,"Steam Pitch!":random.randint(3,26)}

csPhys = {"Double or Nothing!":"Double Attack or Not","Double Cherry Trouble!":random.randint(10,13),"Very Berry Cherry Smash!":25}
csMagic = {"Double or Nothing!":"Double Magic or Not","Cherry Smoothie!":random.randint(12,15),"Sweet Slime!":random.randint(10,15)}

vtPhys = {"Sacrifice!":"Random Stat Boost","Vitale Dagger!":15,"Forsen Lunge!":random.randint(5,20),"Sever!":random.randint(12,50)}
vtMagic = {"Vitality!":"Heal","Illusory Strike!":random.randint(15,20),"Ancestral Flame!":35,"Allegory!":random.randint(9,16)}
def js_moves(attack,enemy,txt):
    jsP = list(jsPhys.items())
    jsM = list(jsMagic.items())
    chance = random.randint(0,14)
    if attack==0:
        if chance>=7:
            # Nil
            txt.insert(INSERT,enemy.name+" used "+jsP[0][0]+"\n")
            txt.insert(INSERT,jsP[0][1]+"\n")
            return 0
        elif chance>=3:
            # Squat
            txt.insert(INSERT,enemy.name+" used "+jsP[1][0]+"\n")
            return jsP[1][1]
        else:
            # Exist
            txt.insert(INSERT,enemy.name+" used "+jsP[2][0]+"\n")
            return jsP[2][1]
    else:
        if chance>=7:
            # Nil
            txt.insert(INSERT,enemy.name+" used "+jsM[0][0]+"\n")
            txt.insert(INSERT,jsM[0][1]+"\n")
            return 0
        elif chance>=3:
            # Schwave
            txt.insert(INSERT,enemy.name+" used "+jsM[1][0]+"\n")
            return jsM[1][1]
        else:
            # Sleep
            txt.insert(INSERT,enemy.name+" used "+jsM[2][0]+"\n")
            heal = .3*enemy.baseHP
            enemy.hp+=math.floor(heal)
            if enemy.hp>enemy.baseHP:
                enemy.hp=enemy.baseHP
            txt.insert(INSERT,enemy.name+" recovered some health\n")
            return 0

def gob_moves(attack,enemy,txt):
    gbP = list(gbPhys.items())
    gbM = list(gbMagic.items())
    chance = random.randint(0,14)
    if attack==0:
        if chance>=8:
            txt.insert(INSERT,enemy.name+" used "+gbP[0][0]+"\n")
            txt.insert(INSERT,"THE GOOBLINS ATTACK WITH ALL THEIR MIGHT!!!\n")
            return gbP[0][1]
        elif chance>=4:
            txt.insert(INSERT,enemy.name+" used "+gbP[1][0]+"\n")
            txt.insert(INSERT,"Teh pointiest of blades!\n")
            return gbP[1][1]
        else:
            txt.insert(INSERT,enemy.name+" used "+gbP[2][0]+"\n")
            choiceof3=random.randint(0,5)
            if choiceof3==0:
                txt.insert(INSERT,"A Full Scale Assualt!\n")
                return random.randint(17,22)
            elif choiceof3==2 or choiceof3==3:
                txt.insert(INSERT,"It's not all of them but it's something!\n")
                return random.randint(10,14)
            else:
                txt.insert(INSERT,"They tried their best...\n")
                return random.randint(3,7)
    else:
        if chance>=8:
            txt.insert(INSERT,enemy.name+" used "+gbM[0][0]+"\n")
            txt.insert(INSERT,"THE GOOBLINS ATTACK WITH ALL THEIR MIGHT!!!\n")
            return gbM[0][1]
        elif chance>=4:
            txt.insert(INSERT,enemy.name+" used "+gbM[1][0]+"\n")
            txt.insert(INSERT,"Teh magicky of magics!\n")
            return gbM[1][1]
        else:
            txt.insert(INSERT,enemy.name+" used "+gbM[2][0]+"\n")
            choiceof3=random.randint(0,5)
            if choiceof3==0:
                txt.insert(INSERT,"A Full Scale Assualt!\n")
                return random.randint(17,22)
            elif choiceof3==2 or choiceof3==3:
                txt.insert(INSERT,"It's not all of them but it's something!\n")
                return random.randint(10,14)
            else:
                txt.insert(INSERT,"They tried their best...\n")
                return random.randint(3,7)

def dg_moves(attack,enemy,root,txt):
    dgP = list(dgPhys.items())
    dgM = list(dgMagic.items())
    chance = random.randint(0,14)
    if attack==0:
        if chance>=8:
            # Aerial Strike
            txt.insert(INSERT,enemy.name+" used "+dgP[0][0]+"\n")
            return dgP[0][1]
        elif chance>=1:
            # Shatter Scales
            txt.insert(INSERT,enemy.name+" used "+dgP[1][0]+"\n")
            txt.insert(INSERT,"Its defense decreased!\n")
            mon.multiplier(enemy,"d",0.8)
            return dgP[1][1]
        else:
            # Dragonne's Fury
            txt.insert(INSERT,enemy.name+" used "+dgP[2][0]+"\n")
            txt.insert(INSERT,enemy.name+" is thrown into a frenzy!\n")
            mon.multiplier(enemy,"A",1.1)
            return dgP[2][1]
    else:
        if chance>=12:
            # Leftovers
            txt.insert(INSERT,enemy.name+" used "+dgM[0][0]+"\n")
            heal = .3*enemy.baseHP
            enemy.hp+=math.floor(heal)
            if enemy.hp>enemy.baseHP:
                enemy.hp=enemy.baseHP
            txt.insert(INSERT,enemy.name+" recovered some health\n")
            return 0
        elif chance==11 and enemy.hp<=0.3*enemy.baseHP:
            # Bye
            txt.insert(INSERT,enemy.name+" used "+dgM[1][0]+"\n")
            messagebox.showinfo("Alert",enemy.name+" has fled!")
            root.destroy()
            return (-7133)
        else:
            # Dragonne's Breath
            txt.insert(INSERT,enemy.name+" used "+dgM[2][0]+"\n")
            return dgM[2][1]

def spf_moves(attack,enemy,txt):
    spfP = list(spfPhys.items())
    spfM = list(spfMagic.items())
    chance = random.randint(0,14)
    if attack==0:
        if chance>=2 and enemy.sphere_mode==True:
            txt.insert(INSERT,enemy.name+" used "+spfP[0][0]+"\n")
            return  spfP[0][1]
        elif chance<2 and enemy.sphere_mode==True:
            txt.insert(INSERT,enemy.name+" used "+spfP[1][0]+"\n")
            return  spfP[1][1]
        elif enemy.sphere_mode==False and enemy.m_type=="Sphiren":
            txt.insert(INSERT,enemy.name+" used "+spfP[2][0]+"\n")
            return  spfP[2][1]
        elif enemy.sphere_mode==False and enemy.m_type=="Sfiren":
            txt.insert(INSERT,enemy.name+" used "+spfP[3][0]+"\n")
            return  spfP[3][1]
    else:
        if enemy.sphere_mode==True:
            txt.insert(INSERT,enemy.name+" used "+spfM[0][0]+"\n")
            return  spfM[0][1]
        elif enemy.sphere_mode==False and enemy.m_type=="Sphiren" and chance<2:
            txt.insert(INSERT,enemy.name+" used "+spfM[1][0]+"\n")
            txt.insert(INSERT,enemy.name+"'s stats increased!\n")
            mon.multiplier(enemy,"f",spfM[1][1])
            return 0
        elif enemy.sphere_mode==False and enemy.m_type=="Sphiren" and chance>=2:
            txt.insert(INSERT,enemy.name+" used "+spfM[2][0]+"\n")
            return spfM[2][1]
        elif enemy.sphere_mode==False and enemy.m_type=="Sfiren" and chance<2:
            txt.insert(INSERT,enemy.name+" used "+spfM[3][0]+"\n")
            txt.insert(INSERT,enemy.name+"'s stats increased!\n")
            mon.multiplier(enemy,"f",spfM[3][1])
            return 0
        elif enemy.sphere_mode==False and enemy.m_type=="Sfiren" and chance>=2:
            txt.insert(INSERT,enemy.name+" used "+spfM[4][0]+"\n")
            return spfM[4][1]

def cs_moves(attack,enemy,txt):
    csP = list(csPhys.items())
    csM = list(csMagic.items())
    chance = random.randint(0,14)
    double = random.randint(1,6)
    if attack==0:
        if chance>=13:
            # Double or Nothing
            txt.insert(INSERT,enemy.name+" used "+csP[0][0]+"\n")
            if double%2==0:
                mon.multiplier(enemy,"A",2)
                txt.insert(INSERT,enemy.name+"'s Attack doubled!\n")
            else:
                txt.insert(INSERT,"Nothing happened!\n")
            return 0
        elif chance>=3:
            # Double Cherry Trouble
            txt.insert(INSERT,enemy.name+" used "+csP[1][0]+"\n")
            return csP[1][1]
        else:
            # Very Berry Cherry Smash
            txt.insert(INSERT,enemy.name+" used "+csP[2][0]+"\n")
            return csP[2][1]
    else:
        if chance>=13:
            # Double or Nothing
            txt.insert(INSERT,enemy.name+" used "+csM[0][0]+"\n")
            if double%2==0:
                mon.multiplier(enemy,"M",2)
                txt.insert(INSERT,enemy.name+"'s Magic doubled!\n")
            else:
                txt.insert(INSERT,"Nothing happened!\n")
            return 0
        elif chance>=7:
            # Cherry Smoothie
            txt.insert(INSERT,enemy.name+" used "+csM[1][0]+"\n")
            return csM[1][1]
        else:
            # Sweet Slime
            txt.insert(INSERT,enemy.name+" used "+csM[2][0]+"\n")
            return csM[2][1]

def vt_moves(attack,enemy,txt):
    vtP = list(vtPhys.items())
    vtM = list(vtMagic.items())
    chance = random.randint(0,100)
    if attack==0:
        if enemy.sacrifice==False:
            # Sacrifice
            txt.insert(INSERT,enemy.name+" used "+vtP[0][0]+"\n")
            if chance>90:
                mon.multiplier(enemy,"f",1.3)
                txt.insert(INSERT,"A gift of burning blood!\n")
            elif chance>70:
                mon.multiplier(enemy,"d",1.5)
                txt.insert(INSERT,"A gift of frozen flesh!\n")
            elif chance>50:
                mon.multiplier(enemy,"o",1.5)
                txt.insert(INSERT,"A gift of spatial fangs!\n")
            elif chance>30:
                mon.multiplier(enemy,"m",1.5)
                txt.insert(INSERT,"A gift of tuned scales!\n")
            elif chance>10:
                mon.multiplier(enemy,"ad",1.5)
                txt.insert(INSERT,"A gift of warrior tears!\n")
            else:
                mon.multiplier(enemy,"s",1.8)
                txt.insert(INSERT,"A gift of restless bones!\n")
            enemy.sacrifice=True
            return 0
        elif chance>75:
            # Vitale Dagger
            txt.insert(INSERT,enemy.name+" used "+vtP[1][0]+"\n")
            return vtP[1][1]
        elif chance >15:
            # Forsen Lunge
            txt.insert(INSERT,enemy.name+" used "+vtP[2][0]+"\n")
            return vtP[2][1]
        else:
            # Sever
            txt.insert(INSERT,enemy.name+" used "+vtP[3][0]+"\n")
            return vtP[3][1]
    else:
        if chance>85 and enemy.sacrifice==True:
            # Vitality
            txt.insert(INSERT,enemy.name+" used "+vtM[0][0]+"\n")
            heal = .3*enemy.baseHP
            enemy.hp+=math.floor(heal)
            if enemy.hp>enemy.baseHP:
                enemy.hp=enemy.baseHP
            txt.insert(INSERT,enemy.name+" recovered some health\n")
            return 0
        elif chance>=55:
            # Illusory Strike
            txt.insert(INSERT,enemy.name+" used "+vtM[1][0]+"\n")
            return vtM[1][1]
        elif chance>=25 and enemy.sacrifice==True:
            # Ancestral Flame
            txt.insert(INSERT,enemy.name+" used "+vtM[2][0]+"\n")
            return vtM[2][1]
        else:
            # Allegory
            txt.insert(INSERT,enemy.name+" used "+vtM[3][0]+"\n")
            return vtM[3][1]

def movePool(attack,enemy,root,txt):
    if enemy.m_type=="Jack Squat":
        dmg = js_moves(attack,enemy,txt)
    elif enemy.m_type=="Gooblins":
        dmg = gob_moves(attack,enemy,txt)
    elif enemy.m_type=="Dragonne":
        dmg = dg_moves(attack,enemy,root,txt)
    elif enemy.m_type=="Sphiren" or enemy.m_type=="Sfiren":
        dmg = spf_moves(attack,enemy,txt)
    elif enemy.m_type=="Cherry Slime":
        dmg = cs_moves(attack,enemy,txt)
    elif enemy.m_type=="Vitaro1" or enemy.m_type=="Vitaro2":
        dmg = vt_moves(attack,enemy,txt)
    else:
        dmg = 10
    return dmg
