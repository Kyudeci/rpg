import json

from all_items.items import Item
# from items import Item
# item1 = Item(1,"Potion","Multi","Restore 20 HP",0,0)
# item1.add_item()
# item1.dev_check_inventory()

ITEMS = json.load(open("all_items/items_index.json","r"),)
for item in ITEMS:
    Item(item['id'],item['name'],item['tags'],item['description'],item['buy_price'],item['sellback_price']).add_item()

def pageSel(inv, page):
    INV = [(k,v['amount']) for k,v in inv.items()]
    pages = list(INV[pos:pos+5] for pos in range(0,len(INV),5))
    if page in range(len(pages)):
        print("Displaying Page {0} of {1}".format(page+1,len(pages)))
        for name, amt in pages[page]:
            print(name, "x", amt)
    else: return(pageSel(inv,page-1))

def viewInv(inv):
    INV = [(k,v['amount']) for k,v in inv.items()]
    pages = list(INV[pos:pos+5] for pos in range(0,len(INV),5))
    for x in pages:
        print("Displaying Page {0} of {1}\n".format(pages.index(x)+1,len(pages)))
        for name, amt in x:
            print(name, "x", amt)
        input()
# print(Item.inventory[0])
# while input() != '3':
#     print(False)