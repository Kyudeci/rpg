import pygame
pygame.mixer.init()
def punch():
    punch_sound=pygame.mixer.Sound("punch.ogg")
    pygame.mixer.Sound.play(punch_sound)
def tackle():
    tackle_sound=pygame.mixer.Sound("tackle1.ogg")
    pygame.mixer.Sound.play(tackle_sound)
def background_music():
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load("battlemusic1.ogg")
    pygame.mixer.music.play(-1)
def magicAttack():
    magic_sound=pygame.mixer.Sound("magicAttack.ogg")
    pygame.mixer.Sound.play(magic_sound)
def victory():
    victory_sound=pygame.mixer.Sound("victory.ogg")
    pygame.mixer.Sound.play(victory_sound)
