import pygame
import sys

def load_image(filepath):
    """Load an image from the specified filepath."""
    try:
        image = pygame.image.load(filepath)
        return image
    except pygame.err as e:
        print(f"Unable to load image at {filepath}: {e}")
        return None

def handle_events():
    """Handle user input events."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            sys.exit()

def reset_game_settings():
    """Reset game settings to default."""
    return {
        'score': [0, 0],
        'paddle_speed': 10,
        'ball_speed': [5, 5],
    }
