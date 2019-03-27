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
import sys
import numpy as np
Red="\033[0;31m"
Green="\033[0;32m"
Cyan="\033[0;36m"
CEND = '\033[0m'
Yellow="\033[0;33m"
On_White="\033[47m"
# puzzleSol=[2,4,1,3]
# puzzle=[1,2,3,4]
# print("Find the correct combination!")
# print("Rules:\n1.Select the first tile you want to move.\n2.Select the tile to switch with.\n")
# while puzzle!=puzzleSol:
#     for y in range(0,4):
#         if puzzle[y]==puzzleSol[y]:
#             print(Green,On_White,puzzle[y],CEND,end="")
#         if puzzle[y]!=puzzleSol[y]:
#             print(Red,On_White,puzzle[y],CEND,end="")
#     print("")
#     sel1=int(input())
#     sel2=int(input())
#     sel1=sel1-1
#     sel2=sel2-1
#     if sel1==sel2:
#         print("No tiles moved!")
#         continue
#     if sel1>4 or sel2>4:
#         continue
#     puzzle[sel1],puzzle[sel2]=puzzle[sel2],puzzle[sel1]
# print("\nPuzzle Complete!")
# for x in range(4):
#     print(Cyan,On_White,puzzle[x],CEND,end="")

sol=[2,6,8,9,3,5,4,1,7]
np.random.shuffle(sol)
puzzSol=np.array(sol).reshape((3,3))
# puzz=np.arange(1,10).reshape((3,3))
np.random.shuffle(sol)
puzz=np.array(sol).reshape((3,3))
moves=0
play=True
while play==True:
    ccc=0
    print("\n")
    print(Yellow,"  C1 C2 C3")
    for x in range(0,len(puzzSol)):
        if ccc%3==0:
            print(Yellow,"R{0}".format(x+1),end="")
        for y in range(0,len(puzzSol)):
            if puzzSol[x][y]==puzz[x][y]:
                print(Green,puzz[x][y],CEND,end="")
                ccc+=1
            if puzzSol[x][y]!=puzz[x][y]:
                print(Red,puzz[x][y],CEND,end="")
                ccc+=1
            if ccc%3==0:
                print("\n")
    print("Make a selection for the first number.")
    r1=int(input("Row:"))
    c1=int(input("Column:"))
    print("\nMake a selection for the second number.")
    r2=int(input("Row:"))
    c2=int(input("Column:"))
    r1=r1-1
    c1=c1-1
    r2=r2-1
    c2=c2-1
    puzz[r1][c1],puzz[r2][c2]=puzz[r2][c2],puzz[r1][c1]
    moves+=1
    if np.array_equal(puzzSol,puzz)==True:
        print("\n")
        print(Yellow,"  C1 C2 C3")
        for x in range(0,len(puzzSol)):
            if ccc%3==0:
                print(Yellow,"R{0}".format(x+1),end="")
            for y in range(0,len(puzzSol)):
                if puzzSol[x][y]==puzz[x][y]:
                    print(Green,puzz[x][y],CEND,end="")
                    ccc+=1
                if puzzSol[x][y]!=puzz[x][y]:
                    print(Red,puzz[x][y],CEND,end="")
                    ccc+=1
                if ccc%3==0:
                    print("\n")
        print("Puzzle Complete!")
        print("Moves Taken:",moves)
        play=False
