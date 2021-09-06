from math import e
from bullets import Laser
import pygame
from settings import *
from player import Player
from meteors import Meteor


class Layout:
    def __init__(self, surface):
        self.surface = surface
        self.meteors = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.lasers = pygame.sprite.Group()
        player_sprite = Player()
        self.player.add(player_sprite)
        self.counter = 0
        self.boom = pygame.mixer.Sound('musics/boom.wav')
        self.laser_sound = pygame.mixer.Sound('musics\laser-sound.mp3')
        self.score = 0
        self.game_over = False
        
        

    def add_meteor(self): 
        if self.counter % meteor_spawn_frequenty == 0:
            meteor_sprite = Meteor()
            self.meteors.add(meteor_sprite)

    def add_laser(self):
        if self.counter % laser_spawn_frequenty == 0:
            laser_sprite = Laser(self.player.sprite.rect.x, self.player.sprite.rect.y)
            self.lasers.add(laser_sprite)
            self.laser_sound.play()

    def collisions(self):
        for laser in self.lasers.sprites():
            for meteor in self.meteors.sprites():
                if laser.rect.colliderect(meteor.rect):
                    self.boom.play()
                    laser.kill()
                    meteor.kill()
                    self.score += 10

    def score_show(self):
        fontObj = pygame.font.Font("freesansbold.ttf", 16)
        self.score_text = fontObj.render("Score: " + str(self.score), True, 'orange')
        self.textRect = self.score_text.get_rect()
        self.textRect.center = (450, 50)
        self.surface.blit(self.score_text, self.textRect)
 
    def check_game_over(self):
        for meteor in self.meteors.sprites():
            if meteor.rect.y >= 800:
                self.game_over = True

    def run(self):
        self.score_show()
        self.counter += 10
        self.add_meteor()
        self.add_laser()
        self.meteors.draw(self.surface)
        self.player.draw(self.surface)
        self.lasers.draw(self.surface)
        self.meteors.update()
        self.player.update()
        self.lasers.update()
        self.collisions()
        self.check_game_over()
        if self.game_over:
            return 'end'
        else:
            return 'main_game'
        

        