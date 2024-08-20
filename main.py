import pygame
from constants import *
from player import *

def main():
    pygame.init()
    if pygame.get_init():
        screen = pygame.display.set_mode(size=(SCREEN_WIDTH, SCREEN_HEIGHT))
    else:
        quit(1)
    if not pygame.display.get_init():
        quit(1)
    clock = pygame.time.Clock()
    delta = 0

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #game loop
        screen.fill("black")
        player.draw(screen)
        pygame.display.flip()


        # end of loop
        dt = clock.tick(60)/1000


if __name__ == "__main__":
    main()
