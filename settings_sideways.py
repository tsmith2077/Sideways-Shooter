class Settings:
    """A class to store all settings for Alien Invasion."""
    
    def __init__(self):
        """Initialize the game's settings."""
        # Screen Settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)
        
        # Alien Settings
        self.alien_speed = 1
        self.fleet_incoming_speed = 100
        # flee_direction of 1 represents right; -1 represents left
        self.fleet_direction = -1
        
        # Rocket Settings
        self.rocket_speed = 3
        self.ship_limit = 3
        
        # Laser Settings
        self.laser_speed = 3
        self.laser_width = 15
        self.laser_height = 3
        self.laser_color = (60, 60, 60)
        self.lasers_allowed = 3
        