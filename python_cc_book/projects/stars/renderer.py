import pygame
from explosion import Explosion

class GameRenderer:
    def __init__(self, screen):
        self.screen = screen

        # Load + scale background once
        try:
            self.background = pygame.image.load("images/background.png")
            self.background = pygame.transform.scale(
                self.background,
                (screen.get_width(), screen.get_height())
            )
        except:
            # fallback background
            self.background = None

        # explosion frames will be generated when needed
        self.explosions = pygame.sprite.Group()
    def spawn_explosion(self, x, y, color=(255, 200, 80)):
        from explosion import Explosion
        ex = Explosion(x, y, color)
        self.explosions.add(ex)


    def draw_background(self):
        if self.background:
            self.screen.blit(self.background, (0, 0))
        else:
            self.screen.fill((10, 10, 30))

    def draw_ship(self, ship):
        ship.blitme()

    def draw_bullets(self, bullets):
        for bullet in bullets:
            bullet.draw()

    def add_explosion(self, explosion):
        self.explosions.add(explosion)

    def draw_explosions(self):
        finished = []

        for ex in self.explosions:
            ex.update()
            if ex.done:
                finished.append(ex)
            else:
                ex.draw(self.screen)

        # remove finished explosions
        for ex in finished:
            self.explosions.remove(ex)
    