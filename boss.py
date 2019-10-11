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
