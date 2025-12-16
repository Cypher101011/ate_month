import pygame
class Ship:
    def __init__(self,screen,settings):
        self.screen =screen
        self.settings =settings

            # Load the ship image
        self.image =pygame.image.load("./images/ship.bmp")

        # get rect of ship and screen

        self.rect =self.image.get_rect()
        self.screen_rect=screen.get_rect()

        #start the ship at bottom center
        self.rect.midbottom=self.screen_rect.midbottom

        #store a float for smooth movement
        self.x =float(self.rect.x)

        #Movement flags
        self.moving_right=False
        self.moving_left=False

        # Velocity for acceleration movement
        self.dx = 0.0
        self.acc = 0.3       # acceleration per frame
        self.friction = 0.95#how fast it slows down (0.9–0.95 smooth)


    def update(self):
        """Accelerate and move the ship smoothly."""

        # Accelerate
        if self.moving_right:
            self.dx += self.acc

        if self.moving_left:
            self.dx -= self.acc

        # Apply friction (slow down when no keys pressed)
        self.dx *= self.friction
      


        # Movement limit (avoid going infinite speed)
        max_speed = self.settings.ship_speed * 6
        if self.dx > max_speed:
            self.dx = max_speed
        if self.dx < -max_speed:
            self.dx = -max_speed

        # Update position
        self.x += self.dx
        self.rect.x = self.x

        # Keep ship on screen
        if self.rect.right > self.screen_rect.right:
            self.rect.right = self.screen_rect.right
            self.x = self.rect.x
            self.dx = 0.3
        if self.rect.left < 0:
            self.rect.left = 0
            self.x = self.rect.x
            self.dx = 0.3
        



    def blitme(self):
        #draw the sip at its current location
        self.screen.blit(self.image,self.rect)

    #