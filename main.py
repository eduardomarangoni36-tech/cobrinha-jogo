import pygame
import sys
from snake import Snake
from food import Food
import random

# Inicializando o Pygame
pygame.init()

# Configurações da tela
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Jogo da Cobrinha")

# Cores
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)

# Clock para controlar a velocidade do jogo
clock = pygame.time.Clock()
snake_speed = 15

# Tamanho do bloco
snake_block = 10

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)

def Your_score(score):
    value = score_font.render("Sua Pontuação: " + str(score), True, green)
    screen.blit(value, [0, 0])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    screen.blit(mesg, [width / 6, height / 3])

def gameLoop():
    game_over = False
    game_close = False

    snake = Snake(width / 2, height / 2, snake_block)
    food = Food(width, height, snake_block)

    while not game_over:

        while game_close:
            screen.fill(black)
            message("Você Perdeu! Pressione Q-Sair ou C-Jogar Novamente", red)
            Your_score(snake.length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.change_direction('LEFT')
                elif event.key == pygame.K_RIGHT:
                    snake.change_direction('RIGHT')
                elif event.key == pygame.K_UP:
                    snake.change_direction('UP')
                elif event.key == pygame.K_DOWN:
                    snake.change_direction('DOWN')

        if snake.move(width, height):
            game_close = True

        screen.fill(black)
        food.draw(screen, pygame)
        snake.draw(screen, pygame, white)
        Your_score(snake.length - 1)

        pygame.display.update()

        if snake.get_head_position() == food.position:
            food.respawn(width, height)
            snake.grow()

        clock.tick(snake_speed)

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    gameLoop()