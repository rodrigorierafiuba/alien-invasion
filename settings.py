WIDTH = 1280
HEIGHT = 720

COLOR_X = 230
COLOR_Y = 230
COLOR_Z = 230

BULLET_COLOR_X = 60
BULLET_COLOR_Y = 60
BULLET_COLOR_Z = 60

SHIP_SPEED = 1.5

BULLET_SPEED = 2.0
BULLET_WIDTH = 3
BULLET_HEIGHT = 15
BULLETS_ALLOWED = 3

class Settings:
    """A class to store all settings for Alien Invasion game."""
    def __init__(self):
        """Initialize game settings."""
        # Window Settings
        self.screen_width = WIDTH
        self.screen_height = HEIGHT
        self.bg_color = (COLOR_X, COLOR_Y, COLOR_Z)

        # Ship Settings
        self.ship_speed = SHIP_SPEED
        
        # Bullet settings
        self.bullet_speed = BULLET_SPEED
        self.bullet_width = BULLET_WIDTH
        self.bullet_height = BULLET_HEIGHT
        self.bullet_color = (BULLET_COLOR_X, BULLET_COLOR_Y, BULLET_COLOR_Z)
        self.bullets_allowed = BULLETS_ALLOWED

