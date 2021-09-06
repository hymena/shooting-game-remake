import pygame
from settings import laser_speed

class Laser(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.image = pygame.image.load('images\laser.png')
        self.rect = self.image.get_rect(topleft=(self.x + 18, self.y - 10))
        

    def update(self):
        if self.rect.y <= 0:
            self.kill()
        else:
            self.rect.y -= laser_speed