HEIGHT = 1920
WIDTH = 1080
COLOR_X = 230
COLOR_Y = 230
COLOR_Z = 230

class Settings:
    """A class to store all settings for Alien Invasion game."""

    def __init__(self):
        """Initialize game settings."""
        self.screen_width = HEIGHT
        self.screen_height = WIDTH
        self.bg_color = (COLOR_X, COLOR_Y, COLOR_Z)
