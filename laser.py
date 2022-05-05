import pygame
from pygame.sprite import Sprite

class Laser(Sprite):
    """A Class to manage the lasers fired from the ship."""
    
    def __init__(self, ss_game):
        """Create a bullet object at the ship's position."""
        super().__init__()
        self.screen = ss_game.screen
        self.settings = ss_game.settings
        self.color = self.settings.laser_color
        
        # Create a bullet rect at (0, 0) and then set correct position.
        self.rect = pygame.Rect(0, 400, self.settings.laser_width, self.settings.laser_height)
        self.rect.midright = ss_game.rocket.rect.midright
       
        
        # Store the bullet's position as a decimal value
        self.x = float(self.rect.x)
        
    def update(self):
        """Move the bullet up the screen."""
        # Update the decimal position of the bullet.
        self.x += self.settings.laser_speed
        # Update the rect postion
        self.rect.x = self.x
        
    def draw_laser(self):
        """Draw the bullet to the screen."""
        pygame.draw.rect(self.screen, self.color, self.rect)