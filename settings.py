WIDTH = 1920
HEIGHT = 1080

COLOR_X = 230
COLOR_Y = 230
COLOR_Z = 230

BULLET_COLOR_X = 60
BULLET_COLOR_Y = 60
BULLET_COLOR_Z = 60

SHIP_SPEED = 1.5
SHIP_LIMIT = 3

BULLET_SPEED = 2.5
BULLET_WIDTH = 3
BULLET_HEIGHT = 15
BULLETS_ALLOWED = 10

ALIEN_SPEED = 1.0
ALIEN_POINTS = 50
DROP_SPEED = 10

SPEEDUP_SCALE = 1.1
SCORE_SCALE = 1.5

EASY_DIFFICULTY = "Easy"
NORMAL_DIFFICULTY = "Normal"
HARD_DIFFICULTY = "Hard"

class Settings:
    """A class to store all settings for Alien Invasion game."""
    def __init__(self):
        """Initialize game settings."""
        # Window Settings
        self.screen_width = WIDTH
        self.screen_height = HEIGHT
        self.bg_color = (COLOR_X, COLOR_Y, COLOR_Z)

        # Ship Settings
        self.ship_limit = SHIP_LIMIT
        
        # Bullet settings
        self.bullet_width = BULLET_WIDTH
        self.bullet_height = BULLET_HEIGHT
        self.bullet_color = (BULLET_COLOR_X, BULLET_COLOR_Y, BULLET_COLOR_Z)
        self.bullets_allowed = BULLETS_ALLOWED

        # Alien Settings
        self.fleet_drop_speed = DROP_SPEED

        # Difficulty
        self.difficulty = ""

        # How quickly the game speeds up
        self.speedup_scale = SPEEDUP_SCALE
        self.score_scale = SCORE_SCALE
        self.initialize_dynamic_settings()
    
    def initialize_dynamic_settings(self):
        """Initialize settings that change throughout the game."""
        if (self.difficulty == EASY_DIFFICULTY):
            self.ship_speed = SHIP_SPEED
            self.bullet_speed = BULLET_SPEED
            self.alien_speed = ALIEN_SPEED
        elif (self.difficulty == NORMAL_DIFFICULTY):
            self.ship_speed = SHIP_SPEED + 1
            self.bullet_speed = BULLET_SPEED
            self.alien_speed = ALIEN_SPEED + 0.5
        elif (self.difficulty == HARD_DIFFICULTY):
            self.ship_speed = SHIP_SPEED + 1.5
            self.bullet_speed = BULLET_SPEED
            self.alien_speed = ALIEN_SPEED + 1.0

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

        # Scoring points
        self.alien_points = ALIEN_POINTS
       
    def increase_speed(self):
        """Increase speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
