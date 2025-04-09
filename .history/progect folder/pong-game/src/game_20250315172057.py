# filepath: pong-game/src/game.py

import pygame
from paddle import Paddle
from ball import Ball

class Paddle:
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.rect = pygame.Rect(x, y, width, height)

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.top > 0:
            self.rect.y -= 5
        if keys[pygame.K_s] and self.rect.bottom < 600:
            self.rect.y += 5

class PongGame:
    def __init__(self, width=800, height=600):
        self.width = width
        self.height = height
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Pong Game")
        self.clock = pygame.time.Clock()
        self.running = True
        self.paddle1 = Paddle(30, self.height // 2 - 60, 10, 120, (255, 255, 255))
        self.paddle2 = Paddle(self.width - 40, self.height // 2 - 60, 10, 120, (255, 255, 255))
        self.ball = Ball(self.width // 2, self.height // 2, 10, (255, 255, 255), 5, 5)
        self.score1 = 0
        self.score2 = 0

    def run(self):
        while self.running:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(60)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False

    def update(self):
        self.paddle1.update()
        self.paddle2.update()
        self.ball.update(self.paddle1, self.paddle2)

        if self.ball.x < 0:
            self.score2 += 1
            self.ball.reset()
        elif self.ball.x > self.width:
            self.score1 += 1
            self.ball.reset()

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.paddle1.draw(self.screen)
        self.paddle2.draw(self.screen)
        self.ball.draw(self.screen)
        self.display_score()
        pygame.display.flip()

    def display_score(self):
        font = pygame.font.Font(None, 36)
        score_text = f"{self.score1} - {self.score2}"
        text = font.render(score_text, True, (255, 255, 255))
        self.screen.blit(text, (self.width // 2 - text.get_width() // 2, 20))

    def quit(self):
        pygame.quit()