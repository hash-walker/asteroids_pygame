# this allows us to use code from
# the open-source pygame library
# throughout this file
import pygame
from constants import *
from player import *
from asteroid import *
from asteroidfield import *
import sys
from buttons import *

def game_loop(screen, clock):

    asteroids = pygame.sprite.Group()
    shots = pygame.sprite.Group()
    updatables = pygame.sprite.Group()
    drawables = pygame.sprite.Group()

    Shot.containers = (shots, updatables, drawables)
    Player.containers = (updatables, drawables)
    Asteroid.containers = (asteroids, updatables, drawables)
    AsteroidField.containers = updatables
    asteroidFieldObj = AsteroidField()

    player = Player(x=SCREEN_WIDTH / 2, y=SCREEN_HEIGHT / 2)

    dt = 0

    while True:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return False
            
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            return True
        
        for updatable in updatables:
            updatable.update(dt)
        
        for asteroid in asteroids:
            if asteroid.checkcollisions(player):
                print("Game Over!")
                return False
        
        for asteroid in asteroids:
            for bullet in shots:
                if asteroid.checkcollisions(bullet):
                    bullet.kill()
                    asteroid.split()

        # Render screen
        screen.fill("black")
        for drawable in drawables:
            drawable.draw(screen)

        # Draw score
        score = str(Asteroid.count)
        score_card = f"Score: {score}"
        button(screen, position_x = - (SCREEN_WIDTH - 200)  / 2, position_y= - (SCREEN_HEIGHT - 50) /2, button_text= score_card , button_color= (0, 0, 0, 0), button_width= 200, button_height= 50, font_size= 36, font_color= "white")

        pygame.display.flip()
        dt = clock.tick(60) / 1000
        

def main_menu(screen, clock):

        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return False
                
            screen.fill("white")

            start_button = button(screen, position_x = 0, position_y= 0, button_text= "Start Game", button_color= "black", button_width= 200, button_height= 50, font_size= 36, font_color= "white")
            exit_button = button(screen, position_x = 0, position_y= 70, button_text= "Exit", button_color= "black", button_width= 200, button_height= 50, font_size= 36, font_color= "white")

            
            mouse_pos = pygame.mouse.get_pos()
            
            if start_button.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    return True
                
            elif exit_button.collidepoint(mouse_pos):
                if pygame.mouse.get_pressed()[0]:
                    return False

            pygame.display.flip()
            dt = clock.tick(60) / 1000

def main():

    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()

    while True:

        if not main_menu(screen, clock):
            break

        if not game_loop(screen, clock):
            break

        
if __name__ == "__main__":
    main()