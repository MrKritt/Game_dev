import pygame
from config import *
from menu import Menu
from main_screen import Game

pygame.init()

pygame.display.set_caption('Artem-Pong')
game = Game(W, H)
flags = "menu"
sond_wing = pygame.mixer.Sound(sound_wing)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()
        if (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE or event.type == pygame.MOUSEBUTTONDOWN) and game.bird.velocity[1] > -15:
            game.bird.velocity[1] = 0 + -6
            sond_wing.play()
            
    if flags == "menu":
        menu = Menu(W, H, bg) 
        menu.draw()
        menu.update()
        flags = menu.flags

    if flags == "play":
        game.draw()
        game.update()

    pygame.display.flip()
    pygame.time.Clock().tick(FPS)