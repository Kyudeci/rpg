import pygame
import sounds
import sys
import rpg
affirm=['yes','y','1']
deny=['no','n','2']
def start():
    intro=input('???: Are you perhaps LOST?\n>Yes...\n>No, not really!\n')
    if intro in affirm:
        print('\nWelcome! I am Meikahs, Keeper of the Lost!\n')
    elif intro in deny:
        print('\n???: Then begone from here! uwu\n')
        sys.exit()
    pygame.time.wait(1000)
    playerName=rpg.create_player()
    joke=["Do you really want to go with that?", "I mean come on! There are better names!","Here, I'll even give the chance to change it this one time!"]
    print(playerName,"was it?")
    for x in range(len(joke)):
        print("Meikahs:",joke[x])
        pygame.time.wait(1800)

start()
