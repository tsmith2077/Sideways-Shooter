class GameStats:
    """Track statistics for Sideways Shooter."""
    
    def __init__(self, ss_game):
        """Initialize statistics."""
        self.settings = ss_game.settings 
        self.reset_stats()
        
        # Start Alien Invasion in an active state.
        self.game_active = True
        
    def reset_stats(self):
        """Initiatize statistics that can change during the game."""
        # self.ships_left = self.settings.ship_limit   ADD BACK FOR SIDEWAYS SHOOTER!!!
        # For Target Practise only
        self.lasers_left = self.settings.lasers_allowed