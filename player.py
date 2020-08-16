import random
from math import floor

import all_items.item_
from all_items.inventory import Inventory


class Player(Inventory):
    def __init__(self, name, hp, atk, dfn, matk, mdef, spd, lvl):
        self.name = name
        self.image = "images/qmark.png"
        self.baseHP = 100
        self.hp = hp
        self.atk = atk
        self.dfn = dfn
        self.matk = matk
        self.mdef = mdef
        self.spd = spd
        self.lvl = lvl
        self.xp = 0
        self.lvlNext = 50
        self.karma = 0
        self.location = "ForestBisca"
        self.bag = Inventory.bag
    Inventory.__init__

    def give_stats(self):
        print("\nName:", self.name,
            "\nLevel:", self.lvl)
        print("HP:", self.hp,
            "\nAttack:", self.atk)
        print("Defense:", self.dfn,
            "\nMagic Attack:", self.matk)
        print("Magic Defence:",
            self.mdef, "\nSpeed:", self.spd)
        print(self.location)

    def levelUp(self, xp):
        self.xp += xp
        while self.xp >= self.lvlNext:
            self.lvl += 1
            self.xp = self.xp - self.lvlNext
            self.lvlNext = floor(self.lvlNext * 1.5)
            print("\nYou are now level", self.lvl)
            print("Exp:", self.xp)
            print("To Next Level:", self.lvlNext, "\n")
            stat_attribute = [self.atk, self.dfn,
                              self.matk, self.mdef, self.spd]
            for x in range(len(stat_attribute)):
                stat = ["Attack:", "Defense:", "Magic Attack:",
                        "Magic Defense:", "Speed:"]
                increase = random.randint(0, 3)
                print(stat[x], stat_attribute[x], "+", increase)
                if stat[x] == stat[0]:
                    self.atk += increase
                elif stat[x] == stat[1]:
                    self.dfn += increase
                elif stat[x] == stat[2]:
                    self.matk += increase
                elif stat[x] == stat[3]:
                    self.mdef += increase
                elif stat[x] == stat[4]:
                    self.spd += increase


Origin = Player("Meikahs", 999, 999, 999, 999, 999, 999, 999)
Player1 = Player("Kyu", 100, 54, 24, 56, 57, 61, 1)
