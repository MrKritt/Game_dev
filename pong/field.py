from re import S
import pygame
from config import *
from ball import Ball
from racket import Racket, RacketAI

class Field:
    def __init__(self, width, height, background):
        self.width = width
        self.height = height
        self.background = background
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()
        self.bg = pygame.image.load(self.background).convert()
        self.b1 = Ball(self.width//2, self.height//2,  face)
        self.rack1 = Racket(50, self.height//2, speed, zach)
        self.rack2 = RacketAI(self.width - 50, self.height//2, speed, stud)
        self.bound_1 = pygame.draw.line(self.screen, BLACK, [0, H], [W, H], 30)
        self.bound_2 = pygame.draw.line(self.screen, BLACK, [0, 0], [W, 0], 30)
        self.score1 = self.b1.score1()
        self.score2 = self.b1.score2(self.width)
        self.sound_win = pygame.mixer.Sound("Game_dev/pong/sound_effects/victory.wav")
        self.sound_lose = pygame.mixer.Sound("Game_dev/pong/sound_effects/gameover.wav")
        
        
    def draw(self):
        self.screen.blit(self.bg, (0, 0))
        self.screen.blit(self.b1.image, self.b1.rect)
        self.screen.blit(self.rack1.image, self.rack1.rect)
        self.screen.blit(self.rack2.image, self.rack2.rect)
        self.bound_1
        self.bound_2
        self.screen.blit(pygame.font.SysFont('Atari Classic', 42).render(str(self.score2) + " : " + str(self.score1), True, BLACK), (W//2 , H//2 - 350 ))

    def update(self):  
        self.b1.update(self.width,self.height)
        self.rack1.update(self.width,self.height)
        self.rack2.update(self.b1,self.width,self.height)
        self.b1.repulsion(self.rack1)
        self.b1.repulsion(self.rack2)
        self.b1.in_game(self.width,self.height)
        self.bounds = pygame.Rect(self.bound_1)
        self.bounds1 = pygame.Rect(self.bound_2)
        self.score1 += self.b1.score1()
        self.score2 += self.b1.score2(self.width)
        
        
        if not self.bounds.colliderect(self.b1.rect):
            self.b1.velocity[1] = -self.b1.velocity[1]
        if not self.bounds1.colliderect(self.b1.rect):
            self.b1.velocity[1] = -self.b1.velocity[1]
            
        """if self.score1 >= 3 or self.score2 >= 3:
            self.b1.velocity = velocity1
        if self.score1 >= 5 or self.score2 >= 5:
            self.b1.velocity = velocity2
        if self.score1 >= 7 or self.score2 >= 7:
            self.b1.velocity = velocity3"""
            
            
        if self.score1 == 9:
            self.screen.blit(pygame.image.load(lose).convert_alpha(), (0, 0))
            self.screen.blit(pygame.font.SysFont('Atari Classic', 42).render(lose_text, True, BLACK), (W//2 - 500, H//2 - 50))
            self.sound_lose.play()
            pygame.display.flip()
            pygame.time.wait(8000)
            pygame.quit()
            exit()
            
        if self.score2 == 9:
            self.screen.blit(pygame.image.load(win).convert_alpha(), (0, 0))
            self.screen.blit(pygame.font.SysFont('Atari Classic', 42).render(win_text, True, BLACK), (W//2 - 500, H//2 - 50))
            pygame.display.flip()
            pygame.time.wait(8000)
            pygame.quit()
            exit()
        
    def __del__(self):
        pygame.quit()