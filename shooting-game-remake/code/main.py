from meteors import Meteor
from player import Player
from layout import Layout
import pygame
import sys
from pygame.locals import *
from settings import *

pygame.init()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Save the world!')
clock = pygame.time.Clock()
layout = Layout(screen)
bg = pygame.image.load('images/background.png')
pygame.mixer.music.load('musics/background.mp3')
pygame.mixer.music.play(-1, 0.0)

class Game_state():
    def __init__(self):
        self.state = 'pre_game'
        self.ready_image = pygame.image.load('images\get-ready.png')
        self.ready_image_rect = self.ready_image.get_rect(topleft=(0, 300))
        self.game_over_image = pygame.image.load('images\gameover.png')
        self.game_over_rect = self.game_over_image.get_rect(topleft=(0, 100))

    
    def run_pre(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONUP:
                self.state = 'main_game'
        screen.fill('white')
        screen.blit(self.ready_image,self.ready_image_rect)
        pygame.display.update()

    def run_main(self):   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        
        screen.blit(bg, (-200,0))
        self.state = layout.run()
        pygame.display.update()

    def game_over_run(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT or event.type == pygame.MOUSEBUTTONDOWN:
                pygame.quit()
                sys.exit()
        screen.blit(self.game_over_image, self.game_over_rect)   
        pygame.display.update()

    def state_manager(self):
        if self.state == 'pre_game':
            self.run_pre()
        if self.state == 'main_game':      
            self.run_main()
        if self.state == 'end':
            self.game_over_run()

 
state = Game_state()
# Main game loop
while True:
    state.state_manager()
    clock.tick(FPS)