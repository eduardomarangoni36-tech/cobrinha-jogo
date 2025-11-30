import pygame
import sys
from snake import Snake
from food import Food

# Screen dimensions
WIDTH, HEIGHT = 640, 480
GRID_SIZE = 20
GRID_WIDTH = WIDTH // GRID_SIZE
GRID_HEIGHT = HEIGHT // GRID_SIZE

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption("Snake Game")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, 36)
        self.snake = Snake(GRID_WIDTH // 2, GRID_HEIGHT // 2)
        self.food = Food(GRID_WIDTH, GRID_HEIGHT)
        self.score = 0
        self.game_over = False

        # Adiciona o mixer e carrega o som
        pygame.mixer.init()
        self.eat_sound = pygame.mixer.Sound("Sound.mp3")

    def run(self):
        while not self.game_over:
            self.handle_events()
            self.update()
            self.draw()
            self.clock.tick(10) # Game speed

        self.show_game_over_screen()
        pygame.quit()
        sys.exit()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.game_over = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.snake.change_direction("UP")
                elif event.key == pygame.K_DOWN:
                    self.snake.change_direction("DOWN")
                elif event.key == pygame.K_LEFT:
                    self.snake.change_direction("LEFT")
                elif event.key == pygame.K_RIGHT:
                    self.snake.change_direction("RIGHT")

    def update(self):
        self.snake.move()

        # Check for collision with food
        if self.snake.get_head_position() == self.food.position:
            self.snake.grow()
            self.food.randomize_position(self.snake.body)
            self.score += 1
            self.eat_sound.play()  # Toca o som quando pega a comida

        # Check for collision with walls
        head_x, head_y = self.snake.get_head_position()
        if not (0 <= head_x < GRID_WIDTH and 0 <= head_y < GRID_HEIGHT):
            self.game_over = True

        # Check for collision with self
        if self.snake.collides_with_self():
            self.game_over = True

    def draw(self):
        self.screen.fill(BLACK)
        self.snake.draw(self.screen, GRID_SIZE)
        self.food.draw(self.screen, GRID_SIZE)
        self.draw_score()
        pygame.display.flip()

    def draw_score(self):
        score_text = self.font.render(f"Score: {self.score}", True, WHITE)
        self.screen.blit(score_text, (10, 10))

    def show_game_over_screen(self):
        self.screen.fill(BLACK)
        game_over_text = self.font.render("Game Over", True, RED)
        score_text = self.font.render(f"Final Score: {self.score}", True, WHITE)
        restart_text = self.font.render("Press any key to play again", True, WHITE)

        self.screen.blit(game_over_text, (WIDTH // 2 - game_over_text.get_width() // 2, HEIGHT // 4))
        self.screen.blit(score_text, (WIDTH // 2 - score_text.get_width() // 2, HEIGHT // 2))
        self.screen.blit(restart_text, (WIDTH // 2 - restart_text.get_width() // 2, HEIGHT * 3 // 4))
        pygame.display.flip()

        waiting_for_key = True
        while waiting_for_key:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    waiting_for_key = False
                    self.game_over = True # To exit the main loop
                if event.type == pygame.KEYDOWN:
                    waiting_for_key = False
                    game = Game()
                    game.run()

if __name__ == "__main__":
    game = Game()
    game.run()