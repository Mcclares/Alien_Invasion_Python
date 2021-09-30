
import pygame
from bullet import Bullet

class Ship():
    def __init__(self, ai_settings,  screen):
        self.screen = screen
        self.ai_setting = ai_settings
        self.image = pygame.image.load("images/Raketa.bmp")
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()
    
        # self.image = pygame.transform.rotate(self.image, -90)
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom
        # self.rect.left = self.screen_rect.left
        # self.rect.bottom = self.screen_rect.bottom
        self.moving_right = False
        self.moving_left = False
        self.moving_up = False
        self.moving_down = False
        
        self.centerX = float(self.rect.centerx)
        self.centerY =float(self.rect.centery)
        
    def update(self):
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.centerX += self.ai_setting.ship_speed_factor
        if self.moving_left and self.rect.left > 0 :
            self.centerX -= self.ai_setting.ship_speed_factor
        if self.moving_up and self.rect.top > self.screen_rect.top :
            self.centerY -= self.ai_setting.ship_speed_factor
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.centerY += self.ai_setting.ship_speed_factor
       
        self.rect.centery = self.centerY
        self.rect.centerx = self.centerX

    def blitme(self):
        self.screen.blit(self.image, self.rect)
        