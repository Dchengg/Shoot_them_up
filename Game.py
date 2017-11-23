import pygame
import random
import Entities
import Power_ups
from Entities import player
import Commons
from bullet import BulletEnemy
from sprites import sprites
from sprites import enemies
from sprites import bullets
from sprites import PlayerSprite
from sprites import bulletsEnemy
from sprites import power_ups
from os import path

#sprites folder
img_dir = path.join(path.dirname(__file__), 'Sprites')
class Game_Loop():
    def __init__(self):
        clock = pygame.time.Clock() 
        pygame.init()
        screen = pygame.display.set_mode((Commons.WIDTH,Commons.HEIGHT),pygame.FULLSCREEN)
        pygame.display.set_caption("Game")
        background = pygame.image.load(path.join(img_dir,'background.png')).convert()
        background = pygame.transform.scale(background,(Commons.WIDTH,Commons.HEIGHT))
        background_rect = background_rect = background.get_rect()
        #game loop
        running  = True
        while True:
            ev = pygame.event.poll()
            if ev.type == pygame.KEYDOWN:
                if ev.key == pygame.K_RETURN:
                    break
                elif ev.key == pygame.K_q:
                    pygame.quit()
                    quit()
            else:
                self.draw_text(screen, "Press [ENTER] To Begin", 30, Commons.WIDTH/2, Commons.HEIGHT/2)
                self.draw_text(screen, "or [Q] To Quit", 30, Commons.   WIDTH/2, (Commons.HEIGHT/2)+40)
                pygame.display.update()
        while running:
            clock.tick(120)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        running = False
            hits = pygame.sprite.groupcollide(enemies, bullets, True, True)
            for hit in hits:
                print("HIT")
                Entities.new_enemy()
                if random.random() > 0.8:
                    pw = Power_ups.Pow(hit.rect.center)
                    sprites.add(pw)
                    power_ups.add(pw)
                    
            hitsPlayer = pygame.sprite.spritecollide(player,bulletsEnemy,True,pygame.sprite.collide_circle)
            for hitP in hitsPlayer:
                print("DEAD")
                player.lives -=1
                player.power = 1
                #player.hide()
                for sprite in bulletsEnemy:
                    if isinstance(sprite, BulletEnemy):
                        sprite.kill()
            if player.lives == 0:
                running = False
            hits = pygame.sprite.spritecollide(player, power_ups, True)
            for hit in hits:
                if hit.type == 'extra_live':
                    if player.lives < 5:
                        player.lives += 1
                if hit.type == 'upgrade':
                    player.powerup()
                
            screen.fill(Commons.BLACK)
            sprites.update()
            screen.blit(background, background_rect)
            sprites.draw(screen)
            self.draw_lives(screen,5,5,player.lives,player.image_lives)
            pygame.display.flip()      
            
        pygame.quit()
           
    def draw_lives(self,surf, x, y, lives, img):
        for i in range(lives):
            img_rect= img.get_rect()
            img_rect.x = x + 30 * i
            img_rect.y = y
            surf.blit(img, img_rect)
    def draw_text(self,surf, text, size, x, y):
        font_name = pygame.font.match_font('arial')
        font = pygame.font.Font(font_name, size)
        text_surface = font.render(text, True, Commons.WHITE)      
        text_rect = text_surface.get_rect()
        text_rect.midtop = (x, y)
        surf.blit(text_surface, text_rect)


