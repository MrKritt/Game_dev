import pygame
from config import *

class Menu():
    def __init__(self, width, height, background):
        self.screen = pygame.display.set_mode((width, height))
        self.menu = pygame.image.load(background).convert_alpha()
        self.star_txt = menu_start
        self.exit_txt = menu_exit
        self.start = pygame.font.SysFont('Atari Classic', 38).render(self.star_txt, True, BLACK)
        self.exit = pygame.font.SysFont('Atari Classic', 38).render(self.exit_txt, True, BLACK)
        self.start_rect = pygame.draw.rect(self.screen, WHITE, (W//2 - 100, H//2 - 100, 200, 100))
        self.exit_rect = pygame.draw.rect(self.screen, WHITE, (W//2 - 100, H//2 + 100, 200, 100))
        self.start_rect = self.start.get_rect(center=(W//2, H//2))
        self.exit_rect = self.exit.get_rect(center=(W//2, H//2 + 100))
        self.mouse = pygame.mouse.get_pos()
        self.click = pygame.mouse.get_pressed()
        self.flags = flags
        
    def draw(self):
        self.screen.blit(self.menu, (0, 0))
        self.screen.blit(self.start, self.start_rect)
        self.screen.blit(self.exit, self.exit_rect)
        
    def update(self):
        self.button_ceck()

    def button_ceck(self):
        for event in pygame.event.get():
            if self.start_rect.collidepoint(self.mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                self.flags = "play"
                return flags
            if self.exit_rect.collidepoint(self.mouse) and event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                exit()