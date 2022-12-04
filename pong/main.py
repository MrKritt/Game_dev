from typing_extensions import runtime
import pygame
from config import *
from field import Field
from menu import Menu

pygame.init()

pygame.display.set_caption('Artem-Pong')
field = Field(W, H, rasp)
flag = True
flags = "menu"
while flag:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            exit()

    if flags == "menu":
        menu = Menu(W, H, rasp)
        menu.draw()
        menu.update()
        flags = menu.flags
        
    if flags == "play":
        field.update()
        field.draw()
        score += field.score1
        score1 += field.score2

    pygame.display.flip()
    field.clock.tick(FPS)


pygame.quit()

    




