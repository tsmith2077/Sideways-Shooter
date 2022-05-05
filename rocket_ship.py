import pygame

class Rocket:
    """A class to manage the rocket."""
    def __init__(self, ss_game):
        """Initialize the rocket and it's starting position."""
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.screen_rect = ss_game.screen.get_rect()
        
        # Load the rocket and get it's rect.
        self.image = pygame.image.load('../images/rocket.bmp')
        self.image = pygame.transform.scale(self.image, (50, 100)) 
        self.image = pygame.transform.rotate(self.image, 270)
        self.rect = self.image.get_rect()
        
        # Set starting position
        self.rect.x = 0
        self.rect.y = 400   
        
        # Store a decial value for the ship's vertical position
        self.x = float(self.rect.x)            
        
        # Movement Flags
        self.moving_up = False
        self.moving_down = False
        
    def update(self):
        if self.moving_up and self.rect.top > 0:
            self.rect.y -= self.settings.rocket_speed
        if self.moving_down and self.rect.bottom < self.screen_rect.bottom:
            self.rect.y += self.settings.rocket_speed
            
        # Update rect object from self.x
        self.rect.x = self.x
    
    def center_ship(self):
        """Center the ship on the screen."""
        self.rect.x = 0
        self.rect.y = 400
        self.x = float(self.rect.x)
            
    def blitme(self):
        self.screen.blit(self.image, self.rect)