from boss import Boss
import random as rn
import time
from tqdm import tqdm
class Virus(Boss):

    def corrupt(self):
        dmg = round(self.matk*.1) + (rn.randint(20,25))
        return dmg 

    def replicate(self):
        self.hp+=round(self.baseHP*.15)
        return 0
    
    def initiate(self):
        self.multiplier("M",1.2)

class Slime(Boss):

    def glomp(self):
        dmg = round(1)
# Add tk insert
incarnateV = Virus("","Virus",500,34,56,101,125,77,2670)
incarnateV.powered()
