import pygame
import random
from bullet import Bullet
from bullet import BulletEnemy
import Commons
from sprites import SpriteSheet
from sprites import sprites
from sprites import enemies
from sprites import bullets
from sprites import PlayerSprite
from sprites import bulletsEnemy
#from arduino_uno import ArduinoUNO

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_imgs[0]
        self.image = pygame.transform.scale(self.image,(50,50))
        self.image.set_colorkey(Commons.BLACK)
        self.rect = self.image.get_rect()
        self.image_lives = player_imgs[0]
        self.image_lives = pygame.transform.scale(self.image_lives,(30,30))
        self.image_lives.set_colorkey(Commons.BLACK)
        self.radius = 20
        self.rect.centerx = Commons.WIDTH / 2
        self.rect.bottom = Commons.HEIGHT - 10
        self.y = 0
        self.x = 0 
        self.shoot_delay = 250
        self.last_shot = pygame.time.get_ticks()
        self.lives = 3
        self.hidden = False
        self.hide_timer = pygame.time.get_ticks()
        self.power = 1
        self.power_timer = pygame.time.get_ticks()
        self.last_update = pygame.time.get_ticks()
        self.frame = -1
        self.frame_rate = 75
        """puerto  = "COM7"
        baudios = 9600
        try:
            self.arduino = ArduinoUNO(puerto, baudios)
            self.arduino.leer()
        except:
            self.arduino = None"""
        
    def update(self):
        ## time out for powerups
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1    
            center = self.rect.center
            self.image = player_imgs[self.frame]
            self.image = pygame.transform.scale(self.image,(50,50))
            self.rect = self.image.get_rect()
            self.rect.center = center
            if self.frame >= 3:
                self.frame = -1
                
        if self.power >=2 and pygame.time.get_ticks() - self.power_time > Commons.POWERUP_TIME:
            self.power -= 1
            self.power_time = pygame.time.get_ticks()

        ## unhide 
        if self.hidden and pygame.time.get_ticks() - self.hide_timer > 1000:
            self.hidden = False
            self.rect.centerx = Commons.WIDTH / 2
            self.rect.bottom = Commons.HEIGHT - 30

        self.x = 0     
        self.y = 0
        self.controls()
        
        if self.rect.right > Commons.WIDTH:
            self.rect.right = Commons.WIDTH
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.bottom > Commons.HEIGHT -10 :
            self.rect.bottom = Commons.HEIGHT -10
        if self.rect.top < 0:
            self.rect.top= 0
        self.rect.x += self.x
        self.rect.y += self.y
    def controls(self):
        keystate = pygame.key.get_pressed()     
        if keystate[pygame.K_LEFT]:
            self.x = -3
        elif keystate[pygame.K_RIGHT]:
            self.x = 3
        if keystate[pygame.K_UP]:
            self.y = -3
        elif keystate[pygame.K_DOWN]:
            self.y = 3
        if keystate[pygame.K_SPACE]:
            self.shoot()
       # if self.arduino:
        #    self.arduino_move(self.arduino.leer())
    def arduino_move(self,value):
        if value < 518:
            value = -3
            self.x = value
        elif value > 518:
            value = 3
            self.x = value
    def shoot(self):
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.left, self.rect.top,0)
                bullet2 = Bullet(self.rect.right,self.rect.top,0)
                sprites.add(bullet)
                sprites.add(bullet2)
                bullets.add(bullet)
                bullets.add(bullet2)
            if self.power >= 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery,-2)
                bullet2 = Bullet(self.rect.right, self.rect.centery,2)
                bullet3 = Bullet(self.rect.centerx,self.rect.centery,0)
                sprites.add(bullet1)
                sprites.add(bullet2)
                sprites.add(bullet3)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(bullet3)
            
            
 

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (Commons.WIDTH / 2, Commons.HEIGHT + 200)

class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = enemy_imgs[0]
        self.image = pygame.transform.scale(self.image,(50,50))
        self.rect = self.image.get_rect()
        self.radius = int(self.rect.width *.90 / 2)
        self.rect.x = random.randrange(0, Commons.WIDTH - self.rect.width)
        self.rect.y = random.randrange(-150, -100)
        self.speedx = random.randrange(-2,2)
        self.speedy = random.randrange(1,3)
        self.frame = -1
        self.frame_rate = 75
        self.last_update = pygame.time.get_ticks()
        self.last_shot = pygame.time.get_ticks()
        self.shoot_delay = 450
    def update(self):
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1    
            center = self.rect.center
            self.image = enemy_imgs[self.frame]
            self.image = pygame.transform.scale(self.image,(50,50))
            self.rect = self.image.get_rect()
            self.rect.center = center
            if self.frame >= 3:
                self.frame = -1
        self.shoot()
        self.rect.x += self.speedx
        self.rect.y += self.speedy
        if (self.rect.left < -25):
            self.speedx = 1
        elif (self.rect.right > Commons.WIDTH + 20):
            self.speedx = -1
        if (self.rect.top > Commons.HEIGHT + 10):
            self.rect.x = random.randrange(0, Commons.WIDTH + self.rect.width)
            self.rect.y = random.randrange(-100, -40)
    def shoot(self):
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            bullet = BulletEnemy(self.rect.centerx, self.rect.bottom,player.x,player.y)
            sprites.add(bullet)
            bulletsEnemy.add(bullet)
               
def new_enemy():
    enemy  = Enemy()
    sprites.add(enemy)
    enemies.add(enemy)
    
ss = SpriteSheet('Lightning.png')
player_imgs = []
player_imgs.append(ss.get_image(0,0,30,30))
player_imgs.append(ss.get_image(32,0,30,30))
player_imgs.append(ss.get_image(64,0,30,30))
player_imgs.append(ss.get_image(96,0,30,30))

ss1 = SpriteSheet('UFO.png')
enemy_imgs = []
enemy_imgs.append(ss1.get_image(0,0,30,30))
enemy_imgs.append(ss1.get_image(32,0,30,30))
enemy_imgs.append(ss1.get_image(64,0,30,30))
enemy_imgs.append(ss1.get_image(96,0,30,30))


player = Player()
for i in range(4):
    new_enemy()
PlayerSprite.add(player)
sprites.add(player)

