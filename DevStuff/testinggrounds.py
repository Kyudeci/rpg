# def TownSucreNoir():
#     print("Adamant")
# locations={"TownSucreNoir":TownSucreNoir}
# location="TownSucreNoir"
# if location in locations:
#     locations[location]()
options=["1","2","3"]
loop=0
# menu=input("""\nWhat would you like to do?
#     1.Look Around\n    2.Loop\n    3.Check Stats\n    4.Save\n""")
# import sys
# from time import sleep
#
# words = "This is just a test :P"
# for char in words:
#     sleep(0.5)
#     sys.stdout.write(char)
#     sys.stdout.flush()
# from time import sleep
# import sys
# from random import uniform
# lines = ["You have woken up in a mysterious maze",
#          "The building has 5 levels",
#          " Scans show that the floors increase in size as you go down "]
# for line in lines[2]:
    # for c in line:
    #     print(c, end='')
    #     sys.stdout.flush()
    #     sleep(uniform(0, 0.3))
    # print('')
# print(len(lines[2]))
from asciimatics.effects import Cycle, Stars
from asciimatics.renderers import FigletText
from asciimatics.scene import Scene
from asciimatics.screen import Screen
from time import sleep

def demo(screen):
    screen.move(30, 30)
    screen.draw(10, 10)
    screen.draw(15, 15)
    screen.fill_polygon([[(60, 0), (70, 0), (70, 10), (60, 10)],
                     [(63, 2), (67, 2), (67, 8), (63, 8)]])
    screen.refresh()
    sleep(10)

Screen.wrapper(demo)
