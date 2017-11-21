import pygame
import random
import Commons
from sprites import SpriteSheet
from sprites import power_ups
class Pow(pygame.sprite.Sprite):
    def __init__(self, center):
        pygame.sprite.Sprite.__init__(self)
        self.type = random.choice(['upgrade', 'extra_live'])
        self.image = powerup_imgs[self.type]
        self.image.set_colorkey(Commons.BLACK)
        self.image = pygame.transform.scale(self.image,(30,30))
        self.rect = self.image.get_rect()
        self.rect.center = center
        self.speedy = 1

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.top > Commons.HEIGHT:
            self.kill()

            
ss = SpriteSheet('Power_Ups.png')

extra_live  = ss.get_image(525,30,130,130)
upgrade = ss.get_image(792,33,120,120)
powerup_imgs = {}
powerup_imgs['upgrade'] = upgrade
powerup_imgs['extra_live'] = extra_live

