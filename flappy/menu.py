import pygame
from config import *

class Menu():
    def __init__(self, width, height, background):
        self.screen = pygame.display.set_mode((width, height))
        self.menu = pygame.image.load(background).convert_alpha()
        self.message = pygame.image.load(message).convert_alpha()
        self.start_rect = pygame.draw.rect(self.screen, WHITE, (W//2 - 100, H//2 + 100, 200, 100))
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.flags = flags
        
    def draw(self):
        self.screen.blit(self.menu, (0, 0))
        self.screen.blit(self.message, (W//2.55, H//4))
        
    def update(self):
        self.button_ceck()

    def button_ceck(self):
        for event in pygame.event.get():
            if event.type in [pygame.MOUSEBUTTONDOWN, pygame.KEYDOWN]:
                self.flags = "play"
                return flags
            