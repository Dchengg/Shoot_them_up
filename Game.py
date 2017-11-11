import pygame
import random
from Entities import Player
import Commons
from sprites import sprites

from os import path

#sprites folder
img_dir = path.join(path.dirname(__file__), 'Sprites')

pygame.init()
screen = pygame.display.set_mode((Commons.WIDTH,Commons.HEIGHT))
pygame.display.set_caption("Game")

font_name = pygame.font.match_font('Nova Square')
background = pygame.image.load(path.join(img_dir,'background.png')).convert()
background = pygame.transform.scale(background,(Commons.WIDTH,Commons.HEIGHT))
background_rect = background_rect = background.get_rect()



#game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                running = False
    screen.fill(Commons.BLACK)
    sprites.update()
    screen.blit(background, background_rect)
    sprites.draw(screen)
    pygame.display.flip()      
    
pygame.quit()
