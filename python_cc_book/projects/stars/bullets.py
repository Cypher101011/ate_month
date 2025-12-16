import pygame
import math

class Bullet(pygame.sprite.Sprite):
    """A glowing circular energy ball that moves upward."""

    def __init__(self, screen, x, y, color=(180,220,255), radius=8, speed= -6):
        super().__init__()
        self.screen = screen
        self.color = color
        self.radius = radius
        self.speed = speed  # negative => moves up

        # Create a surface for the glow (with alpha)
        size = radius * 6  # allow outer glow
        self.image = pygame.Surface((size, size), pygame.SRCALPHA)
        cx, cy = size // 2, size // 2

        # Draw concentric circles to simulate glow
        max_alpha = 200
        layers = 25
        for i in range(layers, 0, -1):
            r = int(radius * (i / layers) * 1.8)
            a = int(max_alpha * (i / layers) ** 1.4)
            pygame.draw.circle(
                self.image,
                (*self.color, a),
                (cx, cy),
                r
            )
        # A bright core
        pygame.draw.circle(self.image, (*self.color, 255), (cx, cy), radius)

        # Get rect and center on (x,y)
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y

        # Use float y for smooth movement
        self.y = float(self.rect.y)

    def update(self):
        """Move the bullet."""
        self.y += self.speed
        self.rect.y = int(self.y)

        # Kill the sprite when it moves off-screen
        if self.rect.bottom < 0:
            self.kill()

    def draw(self):
        """Draw the bullet to the screen."""
        self.screen.blit(self.image, self.rect)
