import pygame
import random
from settings import meteor_speed

class Meteor(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = random.randint(0, 450)
        self.y = -50
        self.image = pygame.image.load('images\meteor.png')
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    

    def update(self):
        self.rect.y += meteor_speed 