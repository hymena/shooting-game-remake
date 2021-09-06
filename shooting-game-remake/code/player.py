import pygame

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.x = 250
        self.y = 750
        self.speed = 15
        self.image = pygame.image.load('images\shooter.png')
        self.rect = self.image.get_rect(topleft=(self.x, self.y))
    

    def get_input_and_move(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            if self.rect.x >= 450:
                pass
            else:
                self.rect.x += self.speed
        if keys[pygame.K_LEFT]:
            if self.rect.x <= 0:
                pass
            else:
                self.rect.x -= self.speed

    def update(self):
        self.get_input_and_move()