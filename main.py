import pygame
from constants import *

def main():
    pygame.init

    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Initialize screen

    print("Starting Asteroids!") 
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    while True: # infinite while loop
        for event in pygame.event.get(): # Can close screen now
            if event.type == pygame.QUIT:
                return

        pygame.Surface.fill(screen, color=(0,0,0)) # black screen
        pygame.display.flip() # refresh
    


if __name__ == "__main__":
    main()