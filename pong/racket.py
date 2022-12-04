import pygame

class Racket(pygame.sprite.Sprite):
    def __init__(self, x, y, speed, filename):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(filename).convert_alpha()
        self.image = pygame.transform.scale(self.image, (85, 200))
        self.rect = self.image.get_rect(center=(x, y))
        self.speed = speed
        
    def draw(self, screen):
        screen.blit(self.image, self.rect)
    
    def update(self, *args):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.rect.y -= self.speed
            if self.rect.y < 0:
                self.rect.y = 0
        if keys[pygame.K_DOWN]:
            self.rect.y += self.speed
            if self.rect.y > args[1] - 200:
                self.rect.y = args[1] - 200
                
                
class RacketAI(Racket):
    def update(self, Ball, *args, speed = 3.3):
        if Ball.rect.x > args[0]//2:
            if self.rect.y < Ball.rect.y:
                self.rect.y += speed
            if self.rect.y > Ball.rect.y:
                self.rect.y -= speed
            if self.rect.y < 0:
                self.rect.y = 0
            if self.rect.y > args[1] - 200:
                self.rect.y = args[1] - 200
        
