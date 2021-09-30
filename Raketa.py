from pygame import sprite
from ship import Ship
from settings import Settings
import pygame as py
import game_functions as gf
from pygame.sprite import Group


def run_game() :
    py.init()
    ai_settings = Settings()
    screen = py.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = Ship(ai_settings,screen)
    bullets = Group()
    while True:
        gf.Check_Events(ai_settings,screen,ship,bullets)
        ship.update()
        gf.Update_bullets(bullets)

        gf.Update_Screen(ai_settings,screen,ship,bullets)


    
    

run_game()
    