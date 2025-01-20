# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys

import pygame



def main():

    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    #initiate asteroids

    asteroids = pygame.sprite.Group()
    asteroidfield = pygame.sprite.Group()
    
    # initiate player

    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroidFieldObj = AsteroidField()

    player = Player(x = SCREEN_WIDTH / 2 , y = SCREEN_HEIGHT / 2)

    dt = 0 

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 
        
        for updatable in updatables:
            updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.checkcollisions(player):
                print("Game Over!")
                return 
        
        screen.fill("black")

        for drawable in drawables:
            drawable.draw(screen)

        pygame.display.flip()
        dt = clock.tick(60) / 1000

        


if __name__ == "__main__":
    main()