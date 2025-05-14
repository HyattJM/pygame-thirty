import pygame
import random

class Ball:
    def __init__(self, x, y, radius=10, speed=5):
        self.x = x
        self.y = y
        self.radius = radius
        self.speed_x = speed * random.choice([-1, 1])
        self.speed_y = -speed
        self.color = (255, 100, 100)

    def move(self):
        self.x += self.speed_x
        self.y += self.speed_y

        # Bounce off left/right
        if self.x - self.radius <= 0 or self.x + self.radius >= 800:
            self.speed_x *= -1

        # Bounce off top
        if self.y - self.radius <= 0:
            self.speed_y *= -1

    def bounce_off_paddle(self, paddle_rect):
        if self.get_rect().colliderect(paddle_rect):
            self.speed_y *= -1
            self.y = paddle_rect.top - self.radius

    def get_rect(self):
        return pygame.Rect(self.x - self.radius, self.y - self.radius, self.radius*2, self.radius*2)

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, (self.x, self.y), self.radius)
