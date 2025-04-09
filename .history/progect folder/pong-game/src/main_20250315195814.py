import pygame
from game import PongGame

def main():
    pygame.init()
    
    # Create a game instance
    game = PongGame()

    # Run the game loop
    game.run()

    pygame.display.quit()

if __name__ == "__main__":
    main()
