import tkinter as tk
from inventory import Inventory
class Item(Inventory):
    def __init__(self, idn, name, tags, desc):
        self.idn = idn
        self.name = name
        self.tags = tags #location, battle, key-item, dungeon, field, multi
        self.desc = desc
        self.amount = 0
    Inventory.__init__
    def info(self):
        root = tk.Tk()
        item_text = tk.Text(root)
        item_text.grid()
        insert = tk.INSERT
        item_text.insert(insert,"Item Name: " + self.name+"\n")
        item_text.insert(insert,"Description: " + self.desc)
        root.mainloop()

