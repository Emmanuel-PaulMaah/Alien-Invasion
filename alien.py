import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """ A class to represent a single alien in the fleet"""

    def  __init__(self, ai_game):
        """Initialize alien and set starting pos"""

        super().__init__()
        self.screen = ai_game.screen
        self.setttings = ai_game.settings

        # Load alien image and set its rect attribute.
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Start each new alien near top left of screen

        self.rect.x = self.rect.width
        self.rect.y = self.rect.width

        # Store alien's exact horiz. pos
        self.x = float(self.rect.x)

    def check_edges(self):
        """ Return True if alien is at edge of screen."""
        screen_rect = self.screen.get_rect()
        return (self.rect.right >= screen_rect.right) or (self.rect.left <= 0)

    def update(self):
        """ Move aliens right or left"""
        self.x += self.setttings.alien_speed * self.setttings.fleet_direction
        self.rect.x = self.x
