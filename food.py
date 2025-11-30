import pygame
import random

class Food:
    def __init__(self, grid_width, grid_height):
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = (0, 0)
        self.randomize_position([])

    def randomize_position(self, snake_body):
        while True:
            self.position = (random.randint(0, self.grid_width - 1),
                             random.randint(0, self.grid_height - 1))
            if self.position not in snake_body:
                break

    def draw(self, screen, grid_size):
        x, y = self.position
        rect = pygame.Rect(x * grid_size, y * grid_size, grid_size, grid_size)
        pygame.draw.rect(screen, (255, 0, 0), rect)