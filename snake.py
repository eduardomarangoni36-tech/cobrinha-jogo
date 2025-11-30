import pygame

class Snake:
    def __init__(self, x, y):
        self.body = [(x, y)]
        self.direction = "RIGHT"
        self.grow_pending = False

    def get_head_position(self):
        return self.body[0]

    def change_direction(self, new_direction):
        if new_direction == "UP" and self.direction != "DOWN":
            self.direction = new_direction
        elif new_direction == "DOWN" and self.direction != "UP":
            self.direction = new_direction
        elif new_direction == "LEFT" and self.direction != "RIGHT":
            self.direction = new_direction
        elif new_direction == "RIGHT" and self.direction != "LEFT":
            self.direction = new_direction

    def move(self):
        head_x, head_y = self.get_head_position()

        if self.direction == "UP":
            head_y -= 1
        elif self.direction == "DOWN":
            head_y += 1
        elif self.direction == "LEFT":
            head_x -= 1
        elif self.direction == "RIGHT":
            head_x += 1

        new_head = (head_x, head_y)
        self.body.insert(0, new_head)

        if self.grow_pending:
            self.grow_pending = False
        else:
            self.body.pop()

    def grow(self):
        self.grow_pending = True

    def collides_with_self(self):
        return self.get_head_position() in self.body[1:]

    def draw(self, screen, grid_size):
        for segment in self.body:
            x, y = segment
            rect = pygame.Rect(x * grid_size, y * grid_size, grid_size, grid_size)
            pygame.draw.rect(screen, (0, 255, 0), rect)