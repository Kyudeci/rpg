# from playsound import playsound
from time import sleep
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import ttk
import os
import re
import pygame
import pygame_gui
# print("Now Playing: Team Skull Encounter Music")
# playsound("C:\\Users\\Kyu\\Music\\Lost in Thoughts All Alone - Azura (English Ver) [Fire Emblem Fates].mp3",block=False)
# print("X")
# playsound("C:\\Users\\Kyu\\Music\\Pokemon Sun & Moon - Team Skull Encounter Music (HQ).mp3")
# def pball():
#     print("This is a Poke Ball")
#     root.destroy()
# def bball():
#     print("This is a Beast Ball")
#     root.destroy()
# def uball():
#     print("This is a Ultra Ball")
#     root.destroy()
# image = Image.open("C:\\Users\\Kyu\\Desktop\\atomprojects\\pokedex-project\\Ultraball-ani.gif")
# photo = ImageTk.PhotoImage(image)
# photo2 = ImageTk.PhotoImage(file="C:\\Users\\Kyu\\Desktop\\atomprojects\\pokedex-project\\Beastball-ani.gif")
# photo3 = ImageTk.PhotoImage(file="C:\\Users\\Kyu\\Desktop\\atomprojects\\pokedex-project\\Pokeball-ani.gif")
# v = tk.Button(root,image=photo,command=uball).grid(row=0,column=2)
# label = tk.Button(root,image=photo2,command=bball).grid(row=0,column=1)
# w = tk.Button(root,image=photo3,command=pball).grid(row=0,column=3)
# w.after(500,root.destroy)

# def mod():
#     # progress['value']+=20.5
#     progress.step(12)
#
# progress = ttk.Progressbar(root,orient="horizontal",length=100,mode='determinate')
# progress.pack()
# button = tk.Button(root,text="Modify",command=mod)
# button.pack()
# root.mainloop()
# help(ttk.Progressbar)
affirm=['yes','YES','Yes','y','Y','1']
deny=['no','NO','No','n','N','2']

# print("Casual fights in\033[0;32m bioluminescent\033[0m lights")
# while input().lower() not in affirm:
#     print(True)
# pygame.init()
# pygame.display.set_caption('Quick Start')
# window_surface = pygame.display.set_mode((800, 600))

# background = pygame.Surface((800, 600))
# background.fill(pygame.Color('#000000'))

# manager = pygame_gui.UIManager((800, 600))

# hello_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
#                                             text='Say Hello',
#                                             manager=manager)

# clock = pygame.time.Clock()
# is_running = True

# while is_running:
#     time_delta = clock.tick(60)/1000.0
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             is_running = False

#         if event.type == pygame.USEREVENT:
#             if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
#                 if event.ui_element == hello_button:
#                     print('Hello World!')

#         manager.process_events(event)

#     manager.update(time_delta)

#     window_surface.blit(background, (0, 0))
#     manager.draw_ui(window_surface)

#     pygame.display.update()