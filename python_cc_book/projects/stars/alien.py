import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """A single alien that falls downward slowly."""

    def __init__(self, game):
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        # Load & scale alien image
        original = pygame.image.load("images/alien2.png")
        self.image = pygame.transform.scale(original, (50, 40))

        # Rect & start position
        self.rect = self.image.get_rect()

        # Start at a random horizontal position
        self.rect.x = self.rect.width + (pygame.time.get_ticks() % (self.settings.screen_width - 2 * self.rect.width))
        self.rect.y = -self.rect.height   # start above the screen

        # Use float for smooth downward movement
        self.y = float(self.rect.y)

        # Falling speed (constant or random)
        self.fall_speed = 0.8

    def update(self):
        """Move the alien downward each frame."""
        self.y += self.fall_speed
        self.rect.y = int(self.y)

        # Remove alien if it goes off-screen bottom
        if self.rect.top > self.settings.screen_height:
            self.kill()

    def blitme(self):
        """Draw the alien on the screen."""
        self.screen.blit(self.image, self.rect)
