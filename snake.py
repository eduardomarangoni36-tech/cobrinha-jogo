class Snake:
    def __init__(self, x, y, block_size):
        self.block_size = block_size
        self.x_change = 0
        self.y_change = 0
        self.head = [x, y]
        self.body = [self.head]
        self.length = 1
        self.direction = ''

    def change_direction(self, new_direction):
        if new_direction == 'LEFT' and self.direction != 'RIGHT':
            self.x_change = -self.block_size
            self.y_change = 0
            self.direction = new_direction
        elif new_direction == 'RIGHT' and self.direction != 'LEFT':
            self.x_change = self.block_size
            self.y_change = 0
            self.direction = new_direction
        elif new_direction == 'UP' and self.direction != 'DOWN':
            self.y_change = -self.block_size
            self.x_change = 0
            self.direction = new_direction
        elif new_direction == 'DOWN' and self.direction != 'UP':
            self.y_change = self.block_size
            self.x_change = 0
            self.direction = new_direction

    def move(self, width, height):
        new_head = [self.head[0] + self.x_change, self.head[1] + self.y_change]

        if new_head[0] >= width or new_head[0] < 0 or new_head[1] >= height or new_head[1] < 0:
            return True  # Game Over

        self.head = new_head
        self.body.append(self.head)
        if len(self.body) > self.length:
            del self.body[0]

        for segment in self.body[:-1]:
            if segment == self.head:
                return True # Game Over

        return False

    def grow(self):
        self.length += 1

    def draw(self, screen, pygame, color):
        for segment in self.body:
            pygame.draw.rect(screen, color, [segment[0], segment[1], self.block_size, self.block_size])

    def get_head_position(self):
        return self.head