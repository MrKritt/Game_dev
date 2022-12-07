import pygame
from config import *

class Score(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.score_img = []
        for i in range(10):
            
            self.img = pygame.image.load(score_img[i]).convert_alpha()
            self.img = pygame.transform.scale(self.img, (50, 50))
            self.score_img.append(self.img)
            
        self.score_img = self.score_img
        
    def draw(self, screen, score, score1):
        self.rect = self.score_img[score1].get_rect(center=(W//2 - 30, 0 + 100))
        screen.blit(self.score_img[score1], self.rect)
        self.rect = self.score_img[score].get_rect(center=(W//2 + 30, 0 + 100))
        screen.blit(self.score_img[score], self.rect)
        
        

