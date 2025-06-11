import pygame
from constants import *

def main():
    pygame.init
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Initialize screen
    clock = pygame.time.Clock() # Create clock
    dt = 0 

    while True: # infinite while loop
        for event in pygame.event.get(): # Can close screen now
            if event.type == pygame.QUIT:
                return
            
        screen.fill("black") # black screen
        pygame.display.flip() # refresh

        dt = clock.tick(60) / 1000 # Update dt and 60 fps

if __name__ == "__main__":
    main()