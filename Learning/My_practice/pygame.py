#this is using  the pygame library 


import os 
import pygame

os.environ['SDL_VIDEO_WINDOW_POS'] =\
    '200,250'

pygame.init()

disPlay = pygame.display.set_mode((300,300))

for r in range(10,100,10):
    pygame.draw.circle(disPlay,(255,0,0),
                           (150,150),r)
    pygame.display.flip()
    pygame.time.wait(500)