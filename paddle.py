import pygame

class Paddle:
    def __init__(self, x, y, width=100, height=20, speed=6):
        self.rect = pygame.Rect(x, y, width, height)
        self.speed = speed

    def move(self, keys, screen_width):
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT] and self.rect.right < screen_width:
            self.rect.x += self.speed

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)
