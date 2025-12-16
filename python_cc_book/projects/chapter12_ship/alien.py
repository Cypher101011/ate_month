import pygame
from pygame.sprite import Sprite

def shrink_image_quarter(image):
    """Return image scaled to half width and half height (1/4 area)."""
    w = image.get_width() // 4
    h = image.get_height() // 4
    return pygame.transform.scale(image, (w, h))


class Alien(Sprite):
    '''a class to represent a single alien in the fleet'''
    def __init__(self, ai_game):
        super().__init__()
        self.screen = ai_game.screen
        self.settings = ai_game.settings

        # load image
        original_image = pygame.image.load('images/alien2.png')

        # shrink to 1/4 size
        self.image = shrink_image_quarter(original_image)

        # set rect
        self.rect = self.image.get_rect()
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        self.x = float(self.rect.x)
    def check_edges(self):
        '''return true if alien is at edge of screen'''
        screen_rect=self.screen.get_rect()
        return (self.rect.right>=screen_rect.right) or (self.rect.left<=0)


    def update(self):
        self.x+=self.settings.alien_speed*self.settings.fleet_direction
        self.rect.x=self.x