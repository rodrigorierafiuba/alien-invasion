import pygame.font

WIDTH = 200
HEIGHT = 50

BUTTON_COLOR_X = 0
BUTTON_COLOR_Y = 135
BUTTON_COLOR_Z = 0

TEXT_COLOR_X = 255
TEXT_COLOR_Y = 255
TEXT_COLOR_Z = 255
TEXT_SIZE = 48
FONT = None # Default font of pygame.

class Button:
    """A class to build buttons for the game."""

    def __init__(self, ai_game, msg):
        """Initializes button attributes."""
        self.screen = ai_game.screen
        self.screen_rect = self.screen.get_rect()

        # Set the dimensions and properties of the button
        self.width, self.height = WIDTH, HEIGHT
        self.button_color = (BUTTON_COLOR_X, BUTTON_COLOR_Y, BUTTON_COLOR_Z)
        self.text_color = (TEXT_COLOR_X, TEXT_COLOR_Y, TEXT_COLOR_Z)
        self.font = pygame.font.SysFont(FONT, TEXT_SIZE)

        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0,
                                self.width,
                                self.height)
        self.rect.center = self.screen_rect.center

        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True,
                                          self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center
    
    def draw_button(self):
        """Draw blanck button and then draw message."""
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)
