import pygame
from config import *
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(pipe_green).convert_alpha()
        self.image1 = pygame.image.load(pipe_green).convert_alpha()
        self.sec_pipe = self.image1
        self.image1 = pygame.transform.rotate(self.image1, 180)
        self.sec_pipe_revers = pygame.transform.rotate(self.sec_pipe, 180)
        self.rect = self.image.get_rect(center=(x, y ))
        self.rect1 = self.image1.get_rect(center=(x, y - 750))
        self.rect_sec = self.sec_pipe.get_rect(center=(x + 350, y))
        self.rect_sec_revers = self.sec_pipe_revers.get_rect(center=(x + 350, y - 750))
        self.velocity = -3
        self.width = x
        self.sound_hit = pygame.mixer.Sound(sound_hit)
        self.sound_point = pygame.mixer.Sound(sound_point)
        self.counter = 0
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        screen.blit(self.image1, self.rect1)

        screen.blit(self.sec_pipe, self.rect_sec)
        screen.blit(self.sec_pipe_revers, self.rect_sec_revers)
        
    def update(self):
        self.move(self.rect, self.rect1, self.rect_sec, self.rect_sec_revers)
        self.random_pipe(self.rect, self.rect1)
        self.random_pipe(self.rect_sec, self.rect_sec_revers)
        
        
    def move(self, pipe, pipe1, pipe_sec, pipe_sec_revers):
        pipe.x += self.velocity
        pipe1.x += self.velocity
        pipe_sec.x += self.velocity
        pipe_sec_revers.x += self.velocity
    
    def collision(self, bird):
        if self.rect.colliderect(bird.rect) or self.rect1.colliderect(bird.rect) or self.rect_sec.colliderect(bird.rect) or self.rect_sec_revers.colliderect(bird.rect):
            self.sound_hit.play()
            return "game_over"

    def random_pipe(self, pipe, pipe1):
        if pipe.x < -100:
            pipe.y = random.randint(200, H - 100)
            pipe1.y = pipe.y - 750
            pipe.x = self.width + 50
            pipe1.x = self.width + 50
    
    def score(self, bird):
        if (bird.rect.left > self.rect.right and bird.rect.left < self.rect.right + 5 or bird.rect.left > self.rect_sec.right and bird.rect.left < self.rect_sec.right + 5) and self.counter % 4 == 0:
            self.sound_point.play()
            return "score"
            
