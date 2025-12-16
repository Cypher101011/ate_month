import sys
import pygame
from settings import Settings
from ship import Ship
from bullet import Bullet
from alien import Alien
from time import sleep
from game_stats import GameStats
from button import Button
from game_stats import GameStats

class AlienInvasion:

    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((0,0), pygame.FULLSCREEN)
        self.settings.screen_width = self.screen.get_rect().width
        self.settings.screen_height = self.screen.get_rect().height

        pygame.display.set_caption("Alien Invasion")

        self.stats=GameStats(self)
        self.sb =Scoreboard(self)

        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.game_active=True
        self.play_button=Button(self,'Play')
        


    
    def run_game(self):
        while True:
            self._check_events()
            if self.game_active:
                self.ship.update()
                self._update_bullets()
                self._update_aliens()
            
            self._update_screen()
            self.clock.tick(30)
    def _check_play_button(self,mouse_pos):
        button_clicked =self.play_button.rect.collidepoint(mouse_pos)
        if button_clicked and not self.game_active:
            self.game_active=True
            # get rid of any remaining bullets and aliens
            self.bullets.empty()
            self.aliens.empty()
            self.stats.reset_stats()
            self.sb.prep_score()
            #create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship()
            pygame.mouse.set_visible(False)
    def _check_events(self):
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos =  pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)

            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
            
    
    def _check_keydown_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = True

        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = True

        elif event.key == pygame.K_SPACE or event.key == pygame.K_UP:
            self._fire_bullet()

        elif event.key == pygame.K_q:
            sys.exit()

    def _check_keyup_events(self, event):
        if event.key == pygame.K_RIGHT:
            self.ship.moving_right = False
        elif event.key == pygame.K_LEFT:
            self.ship.moving_left = False

    def _fire_bullet(self):
        if len(self.bullets) < self.settings.bullets_allowed:
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _update_bullets(self):
        self.bullets.update()
        for bullet in self.bullets.copy():
            if bullet.rect.bottom <= 0:
                self.bullets.remove(bullet)
        self._check_bullet_alien_collision()

    def _check_bullet_alien_collision(self):
        collision=pygame.sprite.groupcollide(self.bullets,self.aliens,True,True)
        if collision:
            for aliens in collision.values():
                set.stats.score+=self.settings.alien_points*len(aliens)
                self.sb.prep_score()
            self.stats.score+=self.settings.alien_points
            self.sb.prep_score()
        if not self.aliens:
            # Distroy existing bullet and create new fleet
            self.bullets.empty()
            self._create_fleet()
            self.settings.increase_speed()
    def _update_aliens(self):
        '''update the position of the all aliens i the fleet'''
        self._check_fleet_edges()
        self.aliens.update()

        if pygame.sprite.spritecollideany(self.ship,self.aliens):
            # self.pygame.sprite.spritecollideany(self.ship,self.aliens):
            self._ship_hit()
            print("ship hit")
        self._check_aliens_bottom()
    def _update_screen(self):
        self.screen.fill(self.settings.bg_color)

        for bullet in self.bullets.sprites():
            bullet.draw_bullet()

       
        self.ship.blitme()
        self.aliens.draw(self.screen)
        self.sb.show_score()
   
        if  not self.game_active:
            self.play_button.draw_button()
        pygame.display.flip()
    def _create_fleet(self):
        """Create the full fleet of aliens."""
        alien = Alien(self)
        alien_width, alien_height = alien.rect.size

        # Start one alien width/height from edges
        current_y,current_x = alien_height,alien_width

        # loop rows
        while current_y < (self.settings.screen_height - 3 * alien_height):
        

            # loop columns
            while current_x < (self.settings.screen_width - 2 * alien_width):
                self._create_alien(current_x, current_y)
                current_x += 2 * alien_width   # FIXED

            current_y += 2 * alien_height  
            current_x=alien_width    # next row
    def _create_alien(self,x_position,y_position):
        '''create an alien and place it in the row'''
        new_alien =Alien(self)
        new_alien.x=x_position
        new_alien.rect.x=x_position
        new_alien.rect.y=y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        #respond approximately if any aliens have reached and edge
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
    def _change_fleet_direction(self):
        #drop the entire fleet and change the fleet's direction
        for alien in self.aliens.sprites():
            alien.rect.y+=self.settings.fleet_drop_speed
        self.settings.fleet_direction*=-1


    def _ship_hit(self):
        if self.stats.ship_left>0:
        # decrement ship left
                self.stats.ship_left-=1
                self.bullets.empty()
                self.aliens.empty()
                self._create_fleet()
                self.ship.center_ship()
        else:
            self.game_active=False
            pygame.mouse.set_visible(True)
        sleep(0.5)
    def _check_aliens_bottom(self):
        # '''check if any aliens have reached the bottom of the screen
        for alien in self.aliens.sprites():
            if alien.rect.bottom>=self.settings.screen_height:
                self._ship_hit()
                break


    
if __name__ == '__main__':

    ai = AlienInvasion()
    ai.run_game()
