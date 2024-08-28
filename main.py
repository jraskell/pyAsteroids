import pygame
from constants import *
from player import Player
from asteroid import Asteroid
from asteroidfield import AsteroidField

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    dt = 0

    updateable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroid_group = pygame.sprite.Group()

    Player.containers = (updateable, drawable)
    Asteroid.containers = (asteroid_group, updateable, drawable)
    AsteroidField.containers = (updateable)
    
    player = Player(SCREEN_WIDTH/2, SCREEN_HEIGHT/2)
    field = AsteroidField()

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return
        for entity in updateable:
            entity.update(dt)
        screen.fill((0,0,0))

        for entity in drawable:
            entity.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    main()