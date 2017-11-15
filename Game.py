import pygame
import random
import Entities
import Power_ups
from Entities import player
import Commons
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
        pygame.init()
        screen = pygame.display.set_mode((Commons.WIDTH,Commons.HEIGHT))
        pygame.display.set_caption("Game")
        font_name = pygame.font.match_font('Nova Square')
        background = pygame.image.load(path.join(img_dir,'background.png')).convert()
        background = pygame.transform.scale(background,(Commons.WIDTH,Commons.HEIGHT))
        background_rect = background_rect = background.get_rect()
        #game loop
        running  = True
        while running:
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
                player.hide()
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
