import pygame
from bullet import Bullet
import Commons
from sprites import SpriteSheet
from sprites import sprites

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = player_imgs[0]
        self.image.set_colorkey(Commons.BLACK)
        self.rect = self.image.get_rect()
        self.radius = 20
        self.rect.centerx = Commons.WIDTH / 2
        self.rect.bottom = Commons.HEIGHT - 10
        self.y = 0
        self.x = 0 
        self.shield = 100
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
        
    def update(self):
        ## time out for powerups
        now = pygame.time.get_ticks()
        if now - self.last_update > self.frame_rate:
            self.last_update = now
            self.frame += 1    
            center = self.rect.center
            self.image = player_imgs[self.frame]
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

        self.x = 0     ## makes the player static in the screen by default.
        self.y = 0
        # then we have to check whether there is an event hanlding being done for the arrow keys being 
        ## pressed 

        ## will give back a list of the keys which happen to be pressed down at that moment
        keystate = pygame.key.get_pressed()     
        if keystate[pygame.K_LEFT]:
            self.x = -5
        elif keystate[pygame.K_RIGHT]:
            self.x = 5
        if keystate[pygame.K_UP]:
            self.y = -5
        elif keystate[pygame.K_DOWN]:
            self.y = 5

        #Fire weapons by holding spacebar
        if keystate[pygame.K_SPACE]:
            self.shoot()

        ## check for the borders at the left and right
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
        

    def shoot(self):
        ## to tell the bullet where to spawn
        now = pygame.time.get_ticks()
        if now - self.last_shot > self.shoot_delay:
            self.last_shot = now
            if self.power == 1:
                bullet = Bullet(self.rect.centerx, self.rect.top)
                sprites.add(bullet)
                #bullets.add(bullet)
                #shooting_sound.play()
            if self.power == 2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shooting_sound.play()

            """ MOAR POWAH """
            if self.power >= 3:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                #missile1 = Missile(self.rect.centerx, self.rect.top) # Missile shoots from center of ship
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                all_sprites.add(missile1)
                bullets.add(bullet1)
                bullets.add(bullet2)
                bullets.add(missile1)
                shooting_sound.play()
                missile_sound.play()

    def powerup(self):
        self.power += 1
        self.power_time = pygame.time.get_ticks()

    def hide(self):
        self.hidden = True
        self.hide_timer = pygame.time.get_ticks()
        self.rect.center = (Commons.WIDTH / 2, Commons.HEIGHT + 200)
        
ss = SpriteSheet('Lightning.png')
player_imgs = []
player_imgs.append(ss.get_image(0,0,30,30))
player_imgs.append(ss.get_image(32,0,30,30))
player_imgs.append(ss.get_image(64,0,30,30))
player_imgs.append(ss.get_image(96,0,30,30))

player = Player()
sprites.add(player)
