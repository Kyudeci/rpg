import random
from math import ceil,floor
import os
from monster import Monster
class Boss():
    def __init__(self,image,monstertype,hp,atk,dfn,matk,mdef,spd,mxp):
        self.image = image
        self.m_type = monstertype
        self.baseHP = hp
        self.hp = hp
        self.atk = atk
        self.baseATK = atk
        self.dfn = dfn
        self.baseDFN = dfn
        self.matk = matk
        self.baseMATK = matk
        self.mdef = mdef
        self.baseMDEF = mdef
        self.spd = spd
        self.baseSPD = spd
        self.mxp = mxp
        self.giga = False
    
    def powered(self):
        self.giga = True
        
    def multiplier(self,type,multi):
        if type=="f":
            self.atk*=multi
            self.matk*=multi
            self.dfn*=multi
            self.mdef*=multi
            self.spd*=multi
        elif type=="o":
            self.atk*=multi
            self.matk*=multi
        elif type=="d":
            self.dfn*=multi
            self.mdef*=multi
        elif type=="s":
            self.spd*=multi
        elif type=="ad":
            self.atk*=multi
            self.dfn*=multi
        elif type=="m":
            self.matk*=multi
            self.mdef*=multi
        elif type=="A":
            self.atk*=multi
        elif type=="M":
            self.matk*=multi