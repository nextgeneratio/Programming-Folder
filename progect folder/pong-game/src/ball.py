import pygame

class Ball:
    def __init__(self, x, y, radius, color, speed_x, speed_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.speed_x = speed_x
        self.speed_y = speed_y
        self.initial_position = (x, y)

    def update(self):
        self.x += self.speed_x
        self.y += self.speed_y

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

    def check_collision(self, paddle):
        if (self.x - self.radius < paddle.rect.right and
            self.x + self.radius > paddle.rect.left and
            self.y - self.radius < paddle.rect.bottom and
            self.y + self.radius > paddle.rect.top):
            self.speed_x = -self.speed_x

    def check_wall_collision(self, screen_height):
        if self.y - self.radius <= 0 or self.y + self.radius >= screen_height:
            self.speed_y = -self.speed_y

    def reset(self):
        self.x, self.y = self.initial_position
        self.speed_x *= -1  # Change direction
