import pygame
from sys import exit


pygame.init()
screen = pygame.display.set_mode((800,400))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit() #exit opiton
            exit()

    #draw elements and update everything
    pygame.display.update() #very imp line and do not run cuz you didn't give the option to end the game yet
