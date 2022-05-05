import sys
from time import sleep
import pygame

from settings_sideways import Settings
from game_stats import GameStats
from rocket_ship import Rocket
from laser import Laser
from aliens_sideways import Alien

class RocketGame:
    
    def __init__(self):
        pygame.init()
        self.settings = Settings()
        
        self.screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)
        pygame.display.set_caption("13-5 Sideways Shooter")
        self.screen_rect = self.screen.get_rect()
        
        # Create an instance to store game statistics.
        self.stats = GameStats(self)
        
        self.rocket = Rocket(self)
        self.lasers = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()
        
        self._create_fleet()
        
    def run_game(self):
        while True:
            self._check_events()
            
            if self.stats.game_active:
                self.rocket.update()
                self._update_aliens()
                self._update_lasers()
                
            self._update_screen()
            
    
    def _check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)
                
    def _check_keydown_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = True
        elif event.key == pygame.K_SPACE:
            self._fire_laser()
        
    
    def _check_keyup_events(self, event):
        if event.key == pygame.K_UP:
            self.rocket.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.rocket.moving_down = False
    
    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        available_space_y = self.settings.screen_height - (alien_height)
        number_aliens_y = available_space_y // (2 * alien_height)
        
        # Determine the number of columns
        rocket_height = self.rocket.rect.height
        available_space_x = (self.settings.screen_width - (3 * alien_height) - rocket_height)
        number_of_columns = available_space_x // (3 * alien_height)
        
        # Create the full fleet of aliens
        for column_number in range(number_of_columns):
            for alien_number in range(number_aliens_y):
                self._create_alien(alien_number, column_number)
            
    def _create_alien(self, alien_number, column_number):
        # Create the alien and place it in the row.
        alien = Alien(self)
        alien_height, alien_width = alien.rect.size
        alien.y = alien_height + 2 * alien_height * alien_number
        alien.rect.y = alien.y
        alien.rect.x = (self.settings.screen_width - alien.rect.height)-(alien.rect.height + 2 * alien.rect.height * column_number)
        self.aliens.add(alien)
        
    def _update_aliens(self):
        """Check if alien is on the edge, then update the positions of all aliens in the fleet."""
        self._check_fleet_edges()
        self.aliens.update()
        
        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.rocket, self.aliens):
            self._ship_hit()
            
        # Look for aliens hitting the bottom of the screen.
        self._check_aliens_left()
        
    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if alien.check_edges():
                self._change_fleet_direction()
                break
            
    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direciton."""
        for alien in self.aliens.sprites():
            alien.rect.x -= self.settings.fleet_incoming_speed
        self.settings.fleet_direction *= -1
        
    def _check_aliens_left(self):
        """Check if aliens have reached the left side of screen."""
        for alien in self.aliens.sprites():
            if alien.rect.left <= 0:
                # Treat this as if the ship got hit.
                self._ship_hit()
                break
    
    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        if self.stats.ships_left > 0:
            # Decrement ships_left
            self.stats.ships_left -= 1
            
            # Get rid of any remaining aliens and bullets.
            self.aliens.empty()
            self.lasers.empty() 
            
            # Create a new fleet and center the ship
            self._create_fleet()
            self.rocket.center_ship()
            
            # Pause.
            sleep(0.5)  
        else:
            self.stats.game_active = False         
            
    def _fire_laser(self):
        """Create a new laser and add it to the lasers group.""" 
        if len(self.lasers) < self.settings.lasers_allowed:
            new_laser = Laser(self)
            self.lasers.add(new_laser) 
        
    def _update_lasers(self):
        """Update position of bullets and get rid of old bullets."""
        # Update laser positions.
        self.lasers.update()
            
        # Get rid of lasers that have disappeared.
        for laser in self.lasers.copy():
            if laser.rect.right >= 1200:
                self.lasers.remove(laser)

        # Check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.lasers, self.aliens, True, True)
        
        if not self.aliens:
            # Destroy esisting bullets and create new fleet.
            self.lasers.empty()
            self._create_fleet()
    
    def _update_screen(self):                
        self.screen.fill(self.settings.bg_color)
        self.rocket.blitme()
        for laser in self.lasers.sprites():
            laser.draw_laser()
        self.aliens.draw(self.screen)
        
        pygame.display.flip()

            
if __name__ == '__main__':
    ss = RocketGame()
    ss.run_game()