class GameStats():
    """Track statistics for Alien Invasion."""
    
    def __init__(self, ai_settings):
        """Initialize statistics."""
        self.ai_settings = ai_settings
        self.reset_stats()
        
        # Start game in an inactive state.
        self.game_active = False
        
        # High score will be read from high_score.txt file, or set to 0
        try:
            with open('part_2_projects\game_alien_invasion\high_score.txt') as high_score_file:
                self.high_score = int(high_score_file.read())
        except FileNotFoundError:
            self.high_score = 0
    
    def reset_stats(self):
        """Initialize statistics that can change during the game."""
        self.ships_left = self.ai_settings.ship_limit
        self.score = 0
        self.level = 1
        