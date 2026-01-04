import sys
import pygame
from time import sleep
from settings import Settings
from game_stats import GameStats
from ship import Ship
from bullet import Bullet
from alien import Alien
from button import Button

FRAME_RATE = 60
MSG_BUTTON = "Play"

class AlienInvasion:
    """Overall class to manage game assets and behavior."""

    def __init__(self):
        """Initialize the game, and create game resources."""
        pygame.init()
        self.clock = pygame.time.Clock()
        self.settings = Settings()
        # Create an instance to store game statistics.
        self.stats = GameStats(self)

        self.screen = pygame.display.set_mode(
            (self.settings.screen_width,
             self.settings.screen_height)
        )
        
        pygame.display.set_caption("Alien Invasion")
        
        self.ship = Ship(self)
        self.bullets = pygame.sprite.Group()
        self.aliens = pygame.sprite.Group()

        self._create_fleet()
        self.game_active = False
        
        # Make play button
        self.play_button = Button(self, MSG_BUTTON)


    def run_game(self):
        """Start the main loop for the game."""
        while True:
            self._check_events()

            if (self.game_active):
                self.ship.update()
                self._update_bullets()
                self._update_aliens()

            self._update_screen()
            self.clock.tick(FRAME_RATE)
    
    def _check_events(self):
        """Respond to keypresses and mouse events."""

        # Watch for keyboard and mouse events.
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                sys.exit()
            elif (event.type == pygame.KEYDOWN):
                self._check_keydown_events(event)
            elif (event.type == pygame.KEYUP):
                self._check_keyup_events(event)
            elif (event.type == pygame.MOUSEBUTTONDOWN):
                mouse_pos = pygame.mouse.get_pos()
                self._check_play_button(mouse_pos)

    def _check_play_button(self, mouse_position):
        """Check's if play button is pressed."""
        button_clicked = self.play_button.rect.collidepoint(mouse_position)
        if (button_clicked and not self.game_active):
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()

    def _check_keydown_events(self, event):
        """Respond to keypresses."""
        if (event.key == pygame.K_RIGHT):
            self.ship.moving_right = True
        elif (event.key == pygame.K_LEFT):
            self.ship.moving_left = True
        elif (event.key == pygame.K_q):
            sys.exit()
        elif (event.key == pygame.K_p):
            self.stats.reset_stats()
            self.game_active = True

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship.
            self._create_fleet()
            self.ship.center_ship()
            
        elif (event.key == pygame.K_SPACE):
            self._fire_bullet()
    
    def _check_keyup_events(self, event):
        """Respond to key releases."""
        if (event.key == pygame.K_RIGHT):
            self.ship.moving_right = False
        elif (event.key == pygame.K_LEFT):
                self.ship.moving_left = False
    
    def _fire_bullet(self):
        """Create a new bullet and add it to the bullets group."""
        if (len(self.bullets) < self.settings.bullets_allowed):
            new_bullet = Bullet(self)
            self.bullets.add(new_bullet)

    def _create_fleet(self):
        """Create the fleet of aliens."""
        alien = Alien(self)
        current_x, current_y = alien_width, alien_height = alien.rect.size
        
        # Spacing between aliens is one alien width and one alien height.
        while (current_y < (self.settings.screen_height - (3 * alien_height))):
            while (current_x < (self.settings.screen_width - (2 * alien_width))):
                self._create_alien(current_x, current_y)
                current_x += (2 * alien_width)
            # Finished a row; reset x value, and increment y value.
            current_x = alien_width
            current_y += (2 * alien_height)
        
    def _create_alien(self, x_position, y_position):
        """Create an alien and place it in the row."""
        new_alien = Alien(self)
        new_alien.x = x_position
        new_alien.rect.x = x_position
        new_alien.rect.y = y_position
        self.aliens.add(new_alien)

    def _check_fleet_edges(self):
        """Respond appropriately if any aliens have reached an edge."""
        for alien in self.aliens.sprites():
            if (alien.check_edges()):
                self._change_fleet_direction()
                break

    def _change_fleet_direction(self):
        """Drop the entire fleet and change the fleet's direction."""
        for alien in self.aliens.sprites():
            alien.rect.y += self.settings.fleet_drop_speed
        
        self.settings.fleet_direction *= -1
    
    def _check_bullet_aliens_collision(self):
        """Respond to bullet-alien collisions"""
        
        # Collision: check for any bullets that have hit aliens.
        # If so, get rid of the bullet and the alien.
        collisions = pygame.sprite.groupcollide(
            self.bullets, self.aliens, True, True
        )

        if (not self.aliens):
            # Destroy existing bullets and create new fleet.
            self.bullets.empty()
            self._create_fleet()
    
    def _check_aliens_bottom(self):
        """Check if any aliens have reached to the bottom of the screen."""
        for alien in self.aliens.sprites():
            if (alien.rect.bottom >= self.settings.screen_height):
                # Treat this same as if the ship got hit.
                self._ship_hit()
                break

    def _ship_hit(self):
        """Respond to the ship being hit by an alien."""
        # Decrement ship_left.
        if (self.stats.ships_left > 0):
            self.stats.ships_left -= 1

            # Get rid of any remaining bullets and aliens.
            self.bullets.empty()
            self.aliens.empty()

            # Create a new fleet and center the ship
            self._create_fleet()
            self.ship.center_ship() 

            # Pause
            sleep(0.5)
        else:
            self.game_active = False

    def _remove_bullets(self):
        """Remove bullets that get to the top of the screen."""
        self.bullets.update()

        # Get rid of bullets that have disappeared.
        for bullet in self.bullets.copy():
            if (bullet.rect.bottom <= 0):
                self.bullets.remove(bullet)

    def _update_bullets(self):
        """Update position of bullets and get rid of old bullets."""
        self._remove_bullets()
        self._check_bullet_aliens_collision()
        
    def _update_aliens(self):
        """Check if the fleet is at an edge, then update positions.""" 
        self._check_fleet_edges()
        self.aliens.update()

        # Look for alien-ship collisions.
        if pygame.sprite.spritecollideany(self.ship, self.aliens):
            self._ship_hit()
        
        # Look for aliens hitting the bottom of the screen
        self._check_aliens_bottom()

    def _update_screen(self):
        """Update images on the screen, and flip to the new screen."""
        # Redraw the screen during each pass through the loop.
        self.screen.fill(self.settings.bg_color)

        # Draw the play button if the game is inactive.
        if (not self.game_active):
            self.play_button.draw_button()
            # Make the most recently drawn screen visible
            pygame.display.flip()

        else:
            for bullet in self.bullets.sprites():
                bullet.draw_bullet()

            self.aliens.draw(self.screen)
            self.ship.blitme()
            # Make the most recently drawn screen visible
            pygame.display.flip()




if __name__ == "__main__":
    # Make a instance, and run the game.
    ai = AlienInvasion()
    ai.run_game()
