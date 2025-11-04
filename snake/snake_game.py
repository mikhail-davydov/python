import random

import pygame

# Инициализация Pygame
pygame.init()

# Цвета
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Размер окна
dis_width = 600
dis_height = 400

# Создание игрового окна
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Игра змейка')
clock = pygame.time.Clock()

snake_block = 10
snake_speed = 5

font_size = 25
score_size = 35
game_over_message_font = pygame.font.SysFont("bahnschrift", font_size)
score_font = pygame.font.SysFont("comicsansms", score_size)

def score(score):
    value = score_font.render("Ваш счёт: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

def snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def game_over_message():
    message_text = "Вы проиграли!\nНажмите Q для выхода или C для продолжения."
    lines = message_text.split("\n")
    line_size = game_over_message_font.get_linesize()

    for idx, line in enumerate(lines):
        message = game_over_message_font.render(line, True, red)

        # Получение прямоугольника текста
        text_rect = message.get_rect()

        # Центруем текст относительно центра экрана
        text_rect.center = (dis_width // 2, dis_height // 2 + (idx * line_size))
        dis.blit(message, text_rect)


def win_message():
    message_text = "Вы выиграли!\nНажмите Q для выхода или C для продолжения."
    lines = message_text.split("\n")
    line_size = game_over_message_font.get_linesize()

    for idx, line in enumerate(lines):
        message = game_over_message_font.render(line, True, green)

        # Получение прямоугольника текста
        text_rect = message.get_rect()

        # Центруем текст относительно центра экрана
        text_rect.center = (dis_width // 2, dis_height // 2 + (idx * line_size))
        dis.blit(message, text_rect)


def game_loop(snake_speed: int):
    win = False
    game_over = False
    game_close = False
    initial_snake_speed = snake_speed

    # Начальная позиция змеи
    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    length_of_snake = 1

    food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    while not game_over:

        while game_close:
            dis.fill(blue)
            win_message() if win else game_over_message()
            score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop(initial_snake_speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)
        pygame.draw.rect(dis, green, [food_x, food_y, snake_block, snake_block])
        snake_head = [x1, y1]
        snake_list.append(snake_head)
        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        snake(snake_block, snake_list)
        score(length_of_snake - 1)

        pygame.display.update()

        if x1 == food_x and y1 == food_y:
            food_x = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            food_y = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            length_of_snake += 1
            if length_of_snake == 21:
                win = True
                game_close = True
            if snake_speed <= 15:
                snake_speed += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

game_loop(snake_speed)