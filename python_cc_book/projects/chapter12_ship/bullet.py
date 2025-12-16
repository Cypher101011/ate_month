import pygame
from pygame.sprite import Sprite

class Bullet(Sprite):
    '''A class to manage bullets fired from the ship using image'''

    def __init__(self, ai_game):
        super().__init__()

        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # Load bullet image (PNG recommended with transparency)
        self.image = pygame.image.load("images/laserRed06.png")
        self.rect = self.image.get_rect()

        # Start bullet at ship's top
        self.rect.midtop = ai_game.ship.rect.midtop

        # Store bullet position as float
        self.y = float(self.rect.y)

    def update(self):
        """Move bullet upwards"""
        self.y -= self.settings.bullet_speed
        self.rect.y = self.y

    def draw_bullet(self):
        """Draw bullet image on screen"""
        self.screen.blit(self.image, self.rect)
