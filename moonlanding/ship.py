import pygame
from config import *
import random
class Ship(pygame.sprite.Sprite):
    def __init__(self, x, y, speed):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(ship_img).convert_alpha()
        self.image = pygame.transform.scale(self.image, (30, 25))
        self.rect = self.image.get_rect(center=(x, y))
        self.velocity = [0.1, 0.1]
        self.gravity = 0.001
        self.speed = speed
        self.font = pygame.font.Font(None, 36)
        self.angle = 0
        self.rotated_sprite = pygame.transform.rotate(self.image, self.angle)
        
    def draw(self, screen):
        self.vertical_speed = self.font.render('Velocity: {:.4f}'.format(self.velocity[0]), True, (87, 50, 255))
        self.horizontal_speed = self.font.render('Velocity: {:.4f}'.format(self.velocity[1]), True, (87, 50, 255))
        self.altitude = self.font.render('Altitude: {:.4f}'.format(self.rect.y), True, (87, 50, 255))
        screen.blit(self.rotated_sprite, self.rect)
        screen.blit(self.vertical_speed, (10, 10))
        screen.blit(self.horizontal_speed, (10, 50))
        screen.blit(self.altitude, (10, 90))
        
    def update(self):
        self.rotated_sprite = pygame.transform.rotate(self.image, self.angle)
        self.velocity[1] += self.gravity
        
        self.rect.x += self.velocity[0]
        self.rect.y += self.velocity[1]

    def collision(self, map, screen):
        if self.rect.collidelist(map.get_rects()) != -1:
            self.velocity[0] = 0
            self.velocity[1] = 0
            self.rect.x -= self.velocity[0]
            self.rect.y -= self.velocity[1]
            self.my_animation(8, 6, 48, 60, "explode", (self.rect.x - 100, self.rect.y - 100), screen)
            self.lose = self.font.render('You Lose'.format(self.velocity[0]), True, (87, 50, 255))
            screen.blit(self.lose, (W//2 - 50, H//2))
            
    def land(self, map, screen):
        if self.rect.collidelist(map.get_land_rect()) != -1:
            self.velocity[0] = 0
            self.velocity[1] = 0
            self.rect.x -= self.velocity[0]
            self.rect.y -= self.velocity[1]
            self.win = self.font.render('You Win'.format(self.velocity[0]), True, (87, 50, 255))
            screen.blit(self.win, (W//2, H//2))
    
    def move_up(self):
        self.velocity[1] -= self.speed
    
    def move_down(self):
        self.velocity[1] += self.speed
    
    def move_left(self):
        self.velocity[0] -= self.speed
    
    def move_right(self):
        self.velocity[0] += self.speed
    
    def my_animation(self, w1, h1, k, fps, name, position, screen):
        animation_frames = []
        timer = pygame.time.Clock()
    
        scr = screen
        sprite = pygame.image.load("{0}.png".format(name)).convert_alpha()
    
        width, height = sprite.get_size()
        w, h = width/w1, height/h1
    
        row = 0
    
        for j in range(int(height/h)):
            for i in range(int(width / w)):
                    animation_frames.append(sprite.subsurface(pygame.Rect(i * w, row, w, h)))
        row += int(h)
    
        counter = 0
        
        scr.blit(animation_frames[counter], position)

        counter = (counter + 1) % k
            
        pygame.display.update()
        timer.tick(fps)
        