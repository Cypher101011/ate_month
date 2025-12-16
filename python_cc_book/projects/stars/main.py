import pygame
import sys
from settings import Settings
from ship import Ship
from bullets import Bullet
from renderer import GameRenderer
from alien import Alien
import random
from scoreboard import Scoreboard
class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()   # <-- ADD THIS LINE

        self.settings = Settings()
        self.screen = pygame.display.set_mode(
            (self.settings.screen_width, self.settings.screen_height)
        )
        pygame.display.set_caption("Alien Game (Modular)")

        self.ship = Ship(self.screen, self.settings)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self.renderer = GameRenderer(self.screen)
        font_path =None
        self.scoreboard =Scoreboard(self,font_path=font_path)
        self._spawn_initial_aliens()

    def run(self):
        while True:
            self._check_events()
            self._update_objects()
            self._draw_frame()
            self.clock.tick(60)   # Limit FPS to 60


    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = True
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = True
                if event.key == pygame.K_SPACE:
                    self._fire_bullet()

            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    self.ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    self.ship.moving_left = False
    def _create_fleet(self):
        """Create a fleet of aliens."""
        alien = Alien(self)  # temp alien to get size
        alien_width, alien_height = alien.rect.size

        current_y = alien_height
        while current_y < (self.settings.screen_height - 3 * alien_height):

            current_x = alien_width
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width

            current_y += 2 * alien_height

    def _create_alien(self, x, y):
        alien = Alien(self)
        alien.x = x
        alien.rect.x = x
        alien.rect.y = y
        self.aliens.add(alien)


    def _fire_bullet(self):
        if len(self.bullets) < 5:
            bx = self.ship.rect.centerx
            by = self.ship.rect.top - 6
            bullet = Bullet(self.screen, bx, by)
            self.bullets.add(bullet)

    def _update_objects(self):
        self.ship.update()
        self.bullets.update()
        self.aliens.update()
        self._check_bullet_alien_collisions()
        if random.random() < 0.02:   # lower = less frequent
           self.aliens.add(Alien(self))
    def _check_bullet_alien_collisions(self):
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if collisions:
            for bullet, aliens_hit in collisions.items():
                for alien in aliens_hit:
                    self.renderer.spawn_explosion(
                        alien.rect.centerx, 
                        alien.rect.centery
                    )
                    self.scoreboard.increase(amount=12)

    def _draw_frame(self):
        self.renderer.draw_background()
        self.renderer.draw_ship(self.ship)
        self.renderer.draw_bullets(self.bullets)
        self.aliens.draw(self.screen)
        self.renderer.draw_explosions()
        self.scoreboard.draw()
        pygame.display.flip()
    def _spawn_initial_aliens(self):
        # Spawn 10 aliens to start the game
        for _ in range(10):
            self.aliens.add(Alien(self))




if __name__ == "__main__":
    Game().run()
