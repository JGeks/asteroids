# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import Player

def main():
    pygame.init()

    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    clock = pygame.time.Clock()
    dt = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # Groups for objects
    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updateable, drawable)

    # Create player ONCE, outside the game loop
    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)
    # The game is running
    running = True

    while running:
        for event in pygame.event.get():
            #Closing window stops program
            if event.type == pygame.QUIT:
                return

        #Create black screen
        screen.fill((0, 0, 0))

        updateable.update(dt)
        drawable.draw(screen)

        pygame.display.flip()

        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()