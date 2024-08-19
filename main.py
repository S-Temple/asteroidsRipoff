import pygame
from constants import *

def main():
    pygame.init()
    if pygame.get_init():
        screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        quit(1)
    if not pygame.display.get_init():
        quit(1)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        #game loop
        screen.fill((0,0,0),)
        pygame.display.flip()


if __name__ == "__main__":
    main()
