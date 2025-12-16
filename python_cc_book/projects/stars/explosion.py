import pygame

class Explosion(pygame.sprite.Sprite):
    """Small glowing pop animation for bullet impact."""

    def __init__(self, x, y, color=(255, 200, 80)):
        super().__init__()

        self.frames = []
        self.frame_index = 0
        self.done = False

        # Create glow-like expanding circles
        for r in range(4, 30, 6):
            surf = pygame.Surface((60, 60), pygame.SRCALPHA)
            pygame.draw.circle(surf, (*color, max(20, 255 - r * 6)), (30, 30), r)
            self.frames.append(surf)

        self.image = self.frames[0]
        self.rect = self.image.get_rect(center=(x, y))

    def update(self):
        self.frame_index += 0.4
        if self.frame_index >= len(self.frames):
            self.done = True
        else:
            self.image = self.frames[int(self.frame_index)]

    def draw(self, screen):
        if not self.done:
            screen.blit(self.image, self.rect)
