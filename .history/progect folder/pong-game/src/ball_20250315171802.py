import pygame

class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, paddle):
        if (self.x - self.radius < paddle.x + paddle.width and
            self.x + self.radius > paddle.x and
            self.y - self.radius < paddle.y + paddle.height and
            self.y + self.radius > paddle.y):
            self.speed_x = -self.speed_x

    def check_wall_collision(self, screen_height):
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = -self.speed_y