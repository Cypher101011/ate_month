import pygame
import sys
from settings import Settings
from ship import Ship
from bullets import Bullet

def run_game():
    pygame.init()
    settings = Settings()
    screen = pygame.display.set_mode(
        (settings.screen_width, settings.screen_height)
    )
    background = pygame.image.load("images/background.png")
    background = pygame.transform.scale( background, 
    (settings.screen_width, settings.screen_height)
)
    try:
        laser_sound = pygame.mixer.Sound("sounds/laser.wav")
    except Exception as e:
        print("Couldn't load laser sound:", e)
        laser_sound = None

    bullets = pygame.sprite.Group()
    pygame.display.set_caption("Alien Invasion – Step 3")

    ship = Ship(screen, settings)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    # limit bullets (e.g. max 5)
                    if len(bullets) < 5:
                        # ship.rect.midtop is top center of ship; use that as spawn point
                        bx = ship.rect.centerx
                        by = ship.rect.top - 8
                        new_bullet = Bullet(screen, bx, by, color=(160,220,255), radius=8, speed=-8)
                        bullets.add(new_bullet)
                        if laser_sound:
                            laser_sound.play()


            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_RIGHT:
                    ship.moving_right = False
                if event.key == pygame.K_LEFT:
                    ship.moving_left = False


        screen.blit(background, (0, 0))
        ship.update()
        bullets.update()
        for b in bullets.sprites():
          b.draw()

        ship.blitme()
        pygame.display.flip()


run_game()
