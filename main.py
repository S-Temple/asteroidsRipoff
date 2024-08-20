import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *

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

    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    Player.containers = (updatable, drawable)

    asteroids = pygame.sprite.Group()
    Asteroid.containers = (asteroids, updatable, drawable)
    AsteroidField.containers = updatable

    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    asteroid_field = AsteroidField()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        
        #game loop
        screen.fill("black")
        for obj in updatable:
            obj.update(delta)

        for astroid in asteroids:
            if player.collides(astroid):
                print("Game Over!")
                quit()

        for obj in drawable:
            obj.draw(screen)
        pygame.display.flip()


        # end of loop
        delta = clock.tick(60)/1000


if __name__ == "__main__":
    main()
