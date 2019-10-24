
class Inventory():
    inventory = {}
    bag = {}

    def add_item(self):
        Inventory.inventory[self.idn] = self

    def get_item(self, amt):
        if self.name in Inventory.bag:
            Inventory.bag[self.name]['amount'] += amt
        else:
            Inventory.bag[self.name] = {"Item": self, "id": self.idn, "description": self.desc, "amount": amt}
    
    def use_item(self):
        if self.tags:
            Inventory.bag[self.name]['amount'] -= 1
        if Inventory.bag[self.name]['amount'] == 0:
            Inventory.bag.pop(self.name)

    def dev_check_inventory(self):
        print(Inventory.bag)
        print(Inventory.inventory)


