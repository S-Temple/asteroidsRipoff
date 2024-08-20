import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        # change size rad size???
        super().__init__(x,y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "White", self.position, self.radius)

    def update(self, delta):
        self.position += delta * self.velocity

