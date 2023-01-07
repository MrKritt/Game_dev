import pygame
from config import *
from map import Map
from ship import Ship

class Game():
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.ship = Ship(W//2, H//2, 0.05)
        self.map = Map(W, H, self.screen)
        self.map.point_generation()
        self.background = pygame.Surface((self.width, self.height))
        

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.map.draw(self.screen)
        self.ship.draw(self.screen)

    
    def update(self):
        self.ship.update()
        self.ship.land(self.map, self.screen)
        self.ship.collision(self.map, self.screen)
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.ship.move_up()
        if keys[pygame.K_DOWN]:
            self.ship.move_down()
        if keys[pygame.K_LEFT]:
            self.ship.move_left()
            self.ship.angle += 5
            if self.ship.angle >= 90:
                self.ship.angle = 90
        if keys[pygame.K_RIGHT]:
            self.ship.move_right()
            self.ship.angle -= 5
            if self.ship.angle <= -90:
                self.ship.angle = -90
            
    