from math import floor
from tkinter import *
import random
import monster as mon
def abiVitaro2(enemy):
    # Regeneration
    if enemy.sacrifice==True:
        enemy.hp+=random.randint(1,7)

def abiCherryS(enemy,txt):
    # Rebirth
    if enemy.hp<=0 and enemy.rebirth==False:
        txt.insert(INSERT,enemy.name+" was resurrected!\n")
        enemy.hp+=floor(0.5*enemy.baseHP)

def abiDragonne(enemy,turn,txt):
    # Bolster
    if turn==1:
        enemy.dfn*=1.5

def abiGooblins(enemy,turn,txt):
    mul = 0.1*turn
    if turn%2==0:
        mon.multiplier(enemy,"o",mul)
        txt.insert(INSERT,"More Gooblins join the fight!\n")

def passiveAbi(enemy,turn,txt):
    if enemy.m_type=="Dragonne":
        abiDragonne(enemy,turn,txt)
    elif enemy.m_type=="Vitaro2":
        abiVitaro2(enemy)
    elif enemy.m_type=="Gooblins":
        abiGooblins(enemy,turn,txt)
