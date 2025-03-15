import pygame
import random
from circleshape import CircleShape
from constants import ASTEROID_MIN_RADIUS

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

    def split(self):
        self.kill()
        # Check if smallest size and do not split
        if self.radius <= ASTEROID_MIN_RADIUS:
            return
        else:
            random_angle = random.uniform(20, 50)

            new_velocity_1 = self.velocity.rotate(random_angle)
            new_radius_1 = self.radius - ASTEROID_MIN_RADIUS
            asteroid1 = Asteroid(self.position.x, self.position.y, new_radius_1)
            asteroid1.velocity = new_velocity_1 * 1.2

            new_velocity_2 = self.velocity.rotate(-random_angle)
            new_radius_2 = self.radius - ASTEROID_MIN_RADIUS
            asteroid2 = Asteroid(self.position.x, self.position.y, new_radius_2)
            asteroid2.velocity = new_velocity_2 * 1.2






