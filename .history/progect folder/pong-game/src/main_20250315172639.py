import pygame
from game import Game

def main():
    pygame.init()
    
    # Set up the game window
    screen_width = 800
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Pong Game")
    
    # Create a Game instance
    game = Game(screen)
    
    # Main game loop
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        game.update()
        game.draw()
        pygame.display.flip()
        pygame.time.Clock().tick(60)  # Limit to 60 frames per second
    
    pygame.quit()

if __name__ == "__main__":
    main()