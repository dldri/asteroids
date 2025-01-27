# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from player import *
from constants import *

def main():
    # initialise pygame
    pygame.init()

    # FPS components
    clock = pygame.time.Clock() 
    dt = 0

    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # new GUI window
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # spawn player
    x = SCREEN_WIDTH / 2
    y = SCREEN_HEIGHT / 2
    player_1 = Player(x, y)

    colour = (0,0,0)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        screen.fill(colour)
        player_1.draw(screen)
        pygame.display.flip()
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    main()