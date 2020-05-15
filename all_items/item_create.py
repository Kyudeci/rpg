import json
from pprint import pprint

def load_json():
    with open('C://Users//Kyu//Desktop//workspace//rpg//all_items//items_index.json') as f:
        items = json.load(f)
    return items

def create(ID):
    itemName = input('Item Name: ')
    tags = input('Item Tags: ')
    tagList = tags.split(",")
    desc = input('Description: ')
    buy = input('Buy Price: ')
    sellback = input('Sellback Price: ')

    item_object = {
        "id": ID,
        "name": itemName,
        "tags": tagList,
        "description": desc,
        "buy_price": int(buy),
        "sellback_price": int(sellback)
    }
    return item_object

def creation():
    listOfItems = load_json()
    for item in listOfItems:
        pprint(item)

    creating = True
    idNum = len(listOfItems)
    while creating:
        print('')
        new_item = create(idNum)
        listOfItems.append(new_item)
        with open('C://Users//Kyu//Desktop//workspace//rpg//all_items//items_index.json', 'w') as f:
            json.dump(listOfItems, f)
        idNum += 1
        end = input('Quit: ')
        if end == 'n':
            creating = True
        else:
            creating = False

creation()