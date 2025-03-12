import pygame
from circleshape import CircleShape
from constants import PLAYER_RADIUS
from constants import PLAYER_TURN_SPEED
from constants import PLAYER_SPEED

class Player(CircleShape):

    def __init__(self, x, y):
        
        # Call the parent constructor with the required parameters
        super().__init__(x, y, PLAYER_RADIUS)

        # Initialize rotation
        self.rotation = 0

    
    def draw(self, screen):
        pygame.draw.polygon(screen, (255, 255, 255), self.triangle(), 2)

    def rotate(self, dt):
        self.rotation += PLAYER_TURN_SPEED * dt

    def update(self, dt):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_a]:
            #print("A pressed")
            self.rotate(-dt)

        if keys[pygame.K_d]:
            #print("D pressed")
            self.rotate(dt)

        if keys[pygame.K_w]:
            #print("W pressed")
            self.move(dt)

        if keys[pygame.K_s]:
            #print("S pressed")
            self.move(-dt)

    def move(self, dt):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        self.position += forward * PLAYER_SPEED * dt  
    
    def triangle(self):
        forward = pygame.Vector2(0, 1).rotate(self.rotation)
        right = pygame.Vector2(0, 1).rotate(self.rotation + 90) * self.radius / 1.5
        a = self.position + forward * self.radius
        b = self.position - forward * self.radius - right
        c = self.position - forward * self.radius + right

        return [a, b, c]