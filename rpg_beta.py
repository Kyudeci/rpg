import pygame
import pygame_gui
import sounds as snd
import story
import mechanics as mech
from player import Player

pygame.init()
pygame.mixer.init()

pygame.display.set_caption('Indev Eternal')
window_surface = pygame.display.set_mode((800, 600))

background_img = pygame.image.load(r'C:\Users\Kyu\Desktop\workspace\rpg\images\title.png')
background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

manager = pygame_gui.UIManager((800, 600))

start_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 275), (100, 50)),
          text='Start',
          manager=manager)

load_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 325), (100, 50)),
          text='Load',
          manager=manager)

quit_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((350, 375 ), (100, 50)),
          text='Load',
          manager=manager)

# title = pygame_gui.elements.UIPanel(relative_rect=pygame.Rect((175, 0), (150, 100)),
#             starting_layer_height=1,
#             manager=manager)

is_running = True
menu = True
clock = pygame.time.Clock()

while is_running:
    time_delta = clock.tick(60)/1000.0
    if menu:
        snd.mainTheme()
        menu = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == pygame_gui.UI_BUTTON_PRESSED:
                if event.ui_element == start_button:
                    snd.musicStop()
                    mech.gameStart()
                if event.ui_element == load_button and mech.is_accessible('savefile.dat')==True:
                    returning_player = mech.load()
                    snd.musicStop()
                    mech.gameStart(True, returning_player)
        
        manager.process_events(event)

    manager.update(time_delta)
    
    window_surface.blit(background_img,(190,0))
    manager.draw_ui(window_surface)

    pygame.display.update()

