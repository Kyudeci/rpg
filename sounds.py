import pygame
pygame.mixer.init()
def punch():
    punch_sound=pygame.mixer.Sound("audio/punch.ogg")
    pygame.mixer.Sound.play(punch_sound)
def tackle():
    tackle_sound=pygame.mixer.Sound("audio/tackle1.ogg")
    pygame.mixer.Sound.play(tackle_sound)
def background_music(num):
    song=["audio/battlemusic1.ogg","audio/ntBattle1.ogg","audio/ntBattle2-intense.ogg","audio/Darkness.ogg","audio/Temple.ogg"]
    pygame.mixer.music.set_volume(0.2)
    pygame.mixer.music.load(song[num])
    pygame.mixer.music.play(-1)
def magicAttack():
    magic_sound=pygame.mixer.Sound("audio/magicAttack.ogg")
    pygame.mixer.Sound.play(magic_sound)
def victory():
    victory_sound=pygame.mixer.Sound("audio/victory.ogg")
    pygame.mixer.Sound.play(victory_sound,-1)
def defeat():
    defeat_sound=pygame.mixer.Sound("audio/gameOver.ogg")
    pygame.mixer.Sound.play(defeat_sound,-1)
def mainTheme():
    pygame.mixer.music.load("audio/MainTheme.ogg")
    pygame.mixer.music.play(-1)
def musicStop():
    pygame.mixer.stop()
