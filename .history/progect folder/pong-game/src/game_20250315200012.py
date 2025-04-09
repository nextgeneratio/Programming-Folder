import pygame
from paddle import Paddle
from ball import Ball

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

        keys = pygame.key.get_pressed()
        if keys[pygame.K_w]:  # Move paddle1 up
            self.paddle1.move(up=True)
        if keys[pygame.K_s]:  # Move paddle1 down
            self.paddle1.move(up=False)
        if keys[pygame.K_UP]:  # Move paddle2 up
            self.paddle2.move(up=True)
        if keys[pygame.K_DOWN]:  # Move paddle2 down
            self.paddle2.move(up=False)

    def update(self):
        self.ball.update()
        self.ball.check_collision(self.paddle1)
        self.ball.check_collision(self.paddle2)
        self.ball.check_wall_collision(self.height)

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
        pygame.diplay.quit()
