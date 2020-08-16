import random
import story
import pickle
import monster
import sounds
import eventFlags as ef
from player import Player

def save(player):
    ef.Events().Flags.clear()
    ef.onStartFlagSet()
    events = ef.Events().Flags
    with open('savefile.dat', 'wb') as f:
        pickle.dump([player, events], f, protocol=2)
    print("\nSave complete!")

def load():
    ef.Events().Flags.clear()
    with open('savefile.dat', 'rb') as f:
        player, events = pickle.load(f)
        for y in range(0, len(events)):
            ef.Events().Flags.append(events[y])
        monster.enemy()
        player.give_stats(1)
    return player

def gameStart(l_check=False, player=None):
    if l_check == False:
        sounds.background_music(3)
        story.start()
    else:
        location = player.location
        story.protag = player
        if location in story.locations:
            story.locations[location]()

def is_accessible(path, mode='r'):
    """
    Check if the file or directory at `path` can
    be accessed by the program using `mode` open flags.
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True

def create_player():
    name = input("Meikahs: What is your name by chance? => ")
    if len(name) < 3 and name != 'AI':
        print("Your name is not up to my standards.")
        return create_player()
    atk = random.randint(20, 50)
    dfn = random.randint(20, 50)
    matk = random.randint(20, 50)
    mdef = random.randint(20, 50)
    spd = random.randint(20, 50)
    lvl = 1
    new_player = Player(name, 100, atk, dfn, matk, mdef, spd, lvl)
    return new_player