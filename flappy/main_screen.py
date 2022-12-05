import pygame
from config import *
from bird import Bird

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bird = Bird(W//2, H//2)
        self.background = pygame.image.load(bg).convert()
        self.rect_bg = self.background.get_rect()
        self.x = 0
        self.y = 0
        self.x1 = -self.width
        self.y1 = 0
        
    def draw(self):
        self.screen.blit(self.background, (self.x, self.y))
        self.screen.blit(self.background, (self.x1, self.y1))
        
        self.screen.blit(self.bird.image, self.bird.rect)
        
        
    def update(self):
        self.bird.update()
        
        self.x += -3
        self.x1 += -3
        
        if self.x < -self.width:
            self.x = self.width
        if self.x1 < -self.width:
            self.x1 = self.width
        
        
        