from sys import pycache_prefix
import sys
import pygame as py
from settings import Settings


def run():
    py.init()
    ai_settings = Settings()
    screen = py.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    ship = py.image.load("images/kotik2.bmp")
    ship.set_colorkey((255,255,255))
    rect = ship.get_rect()
    screen_rect = screen.get_rect()
    rect.centerx = screen_rect.centerx
    rect.centery = screen_rect.centery
    

    
    while(True):
        for event in py.event.get():
            if(event.type == py.QUIT):
                sys.exit()
            screen.fill((0,0,255))
            screen.blit(ship,rect)
            py.display.flip()

run()
    