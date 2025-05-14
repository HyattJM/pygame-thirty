import pygame

class Brick:
    def __init__(self, x, y, width=60, height=20, color=(100, 200, 255)):
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.alive = True

    def draw(self, screen):
        if self.alive:
            pygame.draw.rect(screen, self.color, self.rect)
            pygame.draw.rect(screen, (0, 0, 0), self.rect, 2)  # border

    def hit(self):
        self.alive = False
