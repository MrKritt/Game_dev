import pygame
import random
from config import *

class Ball(pygame.sprite.Sprite):
    def __init__(self, x, y,  filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = velocity0
        self.sound_pong = pygame.mixer.Sound("Game_dev/pong/sound_effects/pong.wav")
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, *args):
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]
            
            
    def repulsion(self, racket):
        if pygame.sprite.collide_rect(self, racket):
            self.velocity[0] = -self.velocity[0]
            self.velocity[1] = self.velocity[1]
            self.sound_pong.play()
            
    def in_game(self, W, H):
        if self.rect.x < 0 or self.rect.x > W - 55:
            self.rect.x = W//2
            self.rect.y = H//2
            self.velocity = [random.randint(4,8),random.randint(-8,8)]
            
    def score1(self):
        return 1 if self.rect.x < 5 else 0
    
    def score2(self, W):
        return 1 if self.rect.x > W - 60 else 0
    
    
        