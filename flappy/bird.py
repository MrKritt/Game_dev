import pygame
from config import *
import random

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bird_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (75, 75))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [7, 0]
        #self.sound_up = pygame.mixer.Sound('sounds/up.wav')
        self.counter = 0
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        self.rect.y += self.velocity[1]
        self.counter += 1
        

        if self.counter % 200 == 0:
            self.velocity[1] += 5
            print("fall")    
            
        # если вылетает за экран
        if self.rect.y > 700 or self.rect.y < 0:
            self.rect.y = H//2
        
        