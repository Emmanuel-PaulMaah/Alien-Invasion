from colors import Colors

class Settings:
    """ A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game settings"""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = Colors.LIGHTGREY

        # Bullet settings
        self.bullet_speed = 2.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = Colors.DARKGREY
        self.bullets_allowed = 10

        # Ship settings
        self.ship_speed = 3.0
