import pygame
from config import *
from menu import Menu
from main_screen import Game
pygame.init()

pygame.display.set_caption('Artem-Moonlander')
flags = "play"

game = Game(W, H)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
    
    if flags == "play":
        game.draw()
        game.update()
        
    pygame.display.flip()
    pygame.time.Clock().tick(FPS)