import pygame
from config import *
from bird import Bird
from pipe import Pipe
from score import Score

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.bird = Bird(W//2, H//2)
        self.background = pygame.image.load(bg).convert()
        self.platform = pygame.image.load(platform).convert()
        self.rect_bg = self.background.get_rect()
        self.rect_platform = self.platform.get_rect()
        self.x = 0
        self.y = 0
        self.x1 = -self.width
        self.y1 = 0
        self.pipe = Pipe(W, H)
        self.gameover = pygame.image.load(gameover).convert_alpha()
        self.sound_die = pygame.mixer.Sound(sound_die)
        self.score = 0
        self.score1 = 0
        self.score_paint = Score(W//2, H//2)
        self.vel = -3
        
        
    def draw(self):
        self.screen.blit(self.background, (self.x, self.y))
        self.screen.blit(self.background, (self.x1, self.y1))
        self.pipe.draw(self.screen)
        self.screen.blit(self.platform, (self.x, self.height - 100))
        self.screen.blit(self.platform, (self.x1, self.height - 100))
        self.bird.draw(self.screen)
        
        
    def update(self):
        self.bird.update()
        self.pipe.update()
        
        if self.pipe.collision(self.bird) == "game_over" or self.bird.rect.y > H - 161:
            self.screen.blit(self.gameover, (W//2.5, H//2.5))
            pygame.display.flip()
            self.sound_die.play()
            pygame.time.wait(2000)
            pygame.quit()
            exit()
        
        if self.pipe.score(self.bird) == "score":
            self.score += 1
            if self.score >= 10:
                self.score = 0
                self.score1 += 1
                self.pipe.velocity += -1

                  
        self.x += self.vel
        self.x1 += self.vel
        
        if self.x < -self.width:
            self.x = self.width
        if self.x1 < -self.width:
            self.x1 = self.width
        
        self.score_paint.draw(self.screen, self.score, self.score1)
        