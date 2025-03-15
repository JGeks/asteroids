import pygame
from circleshape import CircleShape
from constants import SHOT_RADIUS

class Shot(CircleShape):

    def __init__(self, x, y):
        # Call the parent CircleShape constructor
        super().__init__(x, y, SHOT_RADIUS)

        # Initialize velocity (will be set by Player.shoot())
        self.velocity = pygame.Vector2(0, 0)
        
        # Add to container groups
        self.add(self.containers)

    def draw(self, screen):
        pygame.draw.circle(screen, (255, 255, 255), self.position, self.radius, 2)

    def update(self, dt):
        self.position += self.velocity * dt