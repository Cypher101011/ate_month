class Settings:
    '''A class to store all settings for Alien Invasion'''

    def __init__(self):
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)


        # Bullet
        self.bullet_speed = 55
        self.bullet_width = 1
        self.bullet_height = 5
        self.bullet_color = (60, 60, 60)
        self.bullets_allowed = 95

        # alien settings
        self.alien_speed=1.0
        self.fleet_drop_speed=10
        #fleet_direction of 1 represent right;-1 represent left
        self.fleet_direction=1

        #ship settings
        self.ship_speed =5
        self.ship_limit=5
        self.initilize_dynamic_settings()
    def initilize_dynamic_settings(self):
        '''initilize settings that change throughout the game '''
        self.ship_speed =50
        self.bullet_speed=25
        self.alien_speed=1
        self.fleet_direction=0
        self.alien_points=50
    
    def increase_speed(self):
        self.ship_speed *=self.speedup_scale
        self.bullet_speed*=self.speedup_scale
        self.alien_speed*=self.speedup_scale

