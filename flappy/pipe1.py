import pygame
from config import *
import random

class Pipe(pygame.sprite.Sprite):
    def __init__(self, x, y, pipe_pos, *pipes):
        pygame.sprite.Sprite.__init__(self)
        self.pipe_pos = pipe_pos
        self.image = pygame.image.load(pipe_green).convert_alpha()
        if pipe_pos == "top":
            self.image = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = -3
        self.width = x
        self.sound_hit = pygame.mixer.Sound(sound_hit)
        self.sound_point = pygame.mixer.Sound(sound_point)
        self.counter = 0
        self.pipes = pipes
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):
        self.move(self.rect)
        self.random_pipe(self.rect, self.pipe_pos, self.pipes)
        
        
    def move(self, pipe):
        pipe.x += self.velocity

    
    def collision(self, bird):
        if self.rect.colliderect(bird.rect):
            self.sound_hit.play()
            return "game_over"

    def random_pipe(self, pipe, pipe_pos, pipes):
        if pipe.x < -100 and pipe_pos == "bot":
            pipe.y = random.randint(200, H - 100)
            pipe.x = self.width + 50
            
        if pipe.x < -100 and pipe_pos == "top":
            pipe.y = pipes[0].rect.y
            pipe.y = pipe.y - 750
            pipe.x = self.width + 50
