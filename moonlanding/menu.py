import pygame
from config import *

class Menu():
    def __init__(self, width, height):
        self.screen = pygame.display.set_mode((width, height))
        self.message = pygame.image.load(message).convert_alpha()
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.flags = flags
        
    def draw(self):
        self.screen.blit(self.message, (W//2.55, H//4))
        
    def update(self):
        self.button_ceck()

    def button_ceck(self):
        for event in pygame.event.get():
            if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                self.flags = "play"
                return flags