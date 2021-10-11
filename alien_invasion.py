
import pygame
from pygame.sprite import Group
from settings import Settings
from ship import Ship
from alien import Alien
import game_functions as gf


def run_game():

   pygame.init()
   try:
    ai_settings = Settings()
    screen = pygame.display.set_mode((ai_settings.screen_width,ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    ship = Ship(ai_settings,screen) 
    bullets = Group()
    aliens = Group()
    gf.create_fleet(ai_settings,screen,aliens)
    
    while True:
            gf.Check_Events(ai_settings,screen,ship,bullets)
            ship.update()
            gf.Update_bullets(bullets)
            
            gf.Update_Screen(ai_settings,screen,ship,aliens,bullets) 
   except Exception as e:
       print(e)
       pygame.quit()

run_game()


