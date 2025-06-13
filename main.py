import pygame
from constants import *
from player import Player

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT)) # Initialize screen
    clock = pygame.time.Clock() # Create clock
    dt = 0 
    # initialize groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True: # infinite while loop
        for event in pygame.event.get(): # Can close screen now
            if event.type == pygame.QUIT:
                return
        
        updatable.update(dt)

        screen.fill("black") # black screen

        for object in drawable:
            object.draw(screen)
        
        pygame.display.flip() # refresh
        dt = clock.tick(60) / 1000 # Update dt and 60 fps

if __name__ == "__main__":
    main()