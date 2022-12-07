import pygame
from config import *

class Bird(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(bird_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (65, 50))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [7, 0]
        self.sound_hit = pygame.mixer.Sound(sound_hit)
        self.counter = 0
    
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        self.rect.y += self.velocity[1]
        self.counter += 1


        if self.counter % 10 == 0 and self.velocity[1] < 14:
            self.velocity[1] += 3

        # если вылетает за экран
        if self.rect.y > H - 155 :
            self.rect.y = H - 155
            self.sound_hit.play()
        if self.rect.y < 0:
            self.rect.y = 0    
        
        