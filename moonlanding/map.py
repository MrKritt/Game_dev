import pygame
import random
import numpy
from config import *

class Map():
    def __init__(self, width, height, screen):
        self.screen = screen
        self.points = []
        self.flags = flags
        self.rects = []
        self.land_rect = []
        self.dot_coordinates = [(random.randint(0,1900), (random.randint(0,800)) ) for i in range(35)]


    def point_generation(self):
        if len(self.points) == 0:
            for x in range(10000):
                if x % 15 == 0:
                    y = self.perlin_noise(x / 80, 0) * 100 + 900
                    self.points.append((x, int(y)))
        
    def draw(self, screen):
        pygame.draw.lines(self.screen, (255, 0, 0), False, self.points, 3)
        self.color_straight_section()
        for x, y in self.dot_coordinates:
            pygame.draw.circle(screen, (255, 255, 255), (x, y), 3)
        
                
    def color_straight_section(self):
        max_angle = 10
        
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i+1]
            
            angle = abs(numpy.arctan2(y2 - y1, x2 - x1) * 180 / numpy.pi)
            
            if angle < max_angle:
                pygame.draw.lines(self.screen, (150, 255, 0), False, self.points[i:i+2], 3)
                
    def perlin_noise(self, x, y):
        gradients = []
        for i in range(8):
            gradients.append((random.uniform(-1, 1), random.uniform(-1, 1)))
        
        x0 = int(x)
        y0 = int(y)
        x1 = x0 + 1
        y1 = y0 + 1
        
        g00 = gradients[(x0 + y0) % 8]
        g01 = gradients[(x0 + y1) % 8]
        g10 = gradients[(x1 + y0) % 8]
        g11 = gradients[(x1 + y1) % 8]
        
        
        u = x - x0
        v = y - y0
        
        nx = (1 - numpy.cos(u * numpy.pi)) / 2
        ny = (1 - numpy.cos(v * numpy.pi)) / 2
        
        return (g00[0] * u + g01[0] * v) * nx + (g10[0] * u + g11[0] * v) * ny

    def get_rects(self):
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i+1]
            line_surface = pygame.Surface((abs(x2 - x1), abs(y2 - y1)))
            line_surface.fill((255, 255, 255))
            line_surface.set_colorkey((255, 255, 255))
            pygame.draw.line(line_surface, (0, 0, 0), (0, 0), (x2 - x1, y2 - y1), 3)
            rect = line_surface.get_rect(topleft=(x1, y1))
            self.rects.append(rect)
        return self.rects

    def get_land_rect(self):
        max_angle = 10
        
        for i in range(len(self.points) - 1):
            x1, y1 = self.points[i]
            x2, y2 = self.points[i+1]
            
            angle = abs(numpy.arctan2(y2 - y1, x2 - x1) * 180 / numpy.pi)
            
            if angle < max_angle:
                line_surface = pygame.Surface((abs(x2 - x1), abs(y2 - y1)))
                line_surface.fill((255, 255, 255))
                line_surface.set_colorkey((255, 255, 255))
                land_rect = line_surface.get_rect(topleft=(x1, y1))
                self.land_rect.append(land_rect)
        return self.land_rect