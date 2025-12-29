WIDTH = 1280
HEIGHT = 720
COLOR_X = 230
COLOR_Y = 230
COLOR_Z = 230

class Settings:
    """A class to store all settings for Alien Invasion game."""

    def __init__(self):
        """Initialize game settings."""
        # Window Settings
        self.screen_width = WIDTH
        self.screen_height = HEIGHT
        self.bg_color = (COLOR_X, COLOR_Y, COLOR_Z)

        # Ship Settings
        self.ship_speed = 1.5
        
