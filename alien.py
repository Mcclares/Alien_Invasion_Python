import pygame
from pygame.sprite import Sprite, spritecollide

class Alien(Sprite):
    def __init__(self, ai_setting, screen): 
        super(Alien,self).__init__()
        self.screen = screen
        self.ai_settings = ai_setting
        
        self.image = pygame.image.load("images/AlienShip.png")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()

        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def blitme(self):
        self.screen.blit(self.image, self.rect)