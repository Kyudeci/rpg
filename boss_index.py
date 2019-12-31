from boss import Boss
import random as rn
import time
class Virus(Boss):

    def corrupt(self):
        dmg = round(self.matk*.1) + (rn.randint(20,25))
        return dmg 

    def replicate(self):
        self.hp+=round(self.baseHP*.15)
        return 0
    
    def powered(self):
        self.giga = True
    
    def inspect(self):
        
# Add tk insert
incarnateV = Virus("","Virus",500,34,56,101,125,77,267)
incarnateV.powered()
print(incarnateV.giga)
print(incarnateV.corruption())
