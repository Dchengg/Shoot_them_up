import pygame
import random
import Commons
from sprites import SpriteSheet
class Bullet(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_img
        self.image.set_colorkey(Commons.BLACK)
        self.rect = self.image.get_rect()
        ## place the bullet according to the current position of the player
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        ## kill the sprite after it moves over the top border
        if self.rect.bottom < 0:
            self.kill()

        ## now we need a way to shoot
        ## lets bind it to "spacebar".
        ## adding an event for it in Game loop

class BulletEnemy(pygame.sprite.Sprite):
    def __init__(self, x, y,PlayerX,PlayerY):
        pygame.sprite.Sprite.__init__(self)
        self.image = bullet_enemy_img
        self.image = pygame.transform.scale(self.image,(12,12))
        self.image.set_colorkey(Commons.BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y 
        self.rect.centerx = x
        self.speedy = random.randrange(1,3)
        self.speedx = random.randrange(-1,1)
    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        self.rect.x += self.speedx
        if self.rect.bottom < 0:
            self.kill()

        
## FIRE ZE MISSILES
class Missile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = missile_img
        self.image.set_colorkey(Commons.BLACK)
        self.rect = self.image.get_rect()
        self.rect.bottom = y
        self.rect.centerx = x
        self.speedy = -10

    def update(self):
        """should spawn right in front of the player"""
        self.rect.y += self.speedy
        if self.rect.bottom < 0:
            self.kill()
            
ss = SpriteSheet('Bullet_Collection.png')
bullet_img = ss.get_image(398,255,20,20)
bullet_enemy_img = ss.get_image(320,268,18,18)
