import pygame
from circleshape import CircleShape

class Asteroid(CircleShape):

    def __init__(self, x, y, radius):
        # Call the parent CircleShape constructor
        super().__init__(x, y, radius)
        
        # Add to container groups
        self.add(self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt