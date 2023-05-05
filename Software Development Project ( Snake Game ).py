import pygame
import time
import random

pygame.init()

white = (255,255,255)
black = (0,0,0)
green = (0,255,0)
yellow = (255,255,102)
red = (213,50,80)
blue = (50,153,213)

screen_width = 640
screen_height = 480

screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Snake Game by Team Academics")

clock = pygame.time.Clock()

snake_size = 10
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35)


def drawSNAKE (snake_size, snake_list):
    for z in snake_list :
        pygame.draw.rect( screen, red, [ z[0], z[1], snake_size, snake_size ])


def showTEXT (message, color):
    msg = font_style.render(message, True, color)
    screen.blit(msg, [screen_width / 6, screen_height / 3])


def showSCORE (score):
    value = score_font.render("SCORE : " + str(score), True, yellow)
    screen.blit(value, [0,0])


def drawFOOD (food_x, food_y):
    pygame.draw.rect(screen, green, [food_x, food_y, snake_size, snake_size])


def gameLOOP ():
    game_over = False
    game_close = False

    x = screen_width / 2
    y = screen_height / 2

    dx = 0
    dy = 0

    snake_list = []
    snake_length = 1

    food_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
    food_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0

    while not game_over :
        while game_close == True:
            screen.fill(blue)
            showTEXT("You Lost! Press C-Play Again or Q-Quit", red)
            showSCORE(snake_length - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLOOP()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    dx = - snake_size
                    dy = 0

                elif event.key == pygame.K_RIGHT:
                    dx = snake_size
                    dy = 0

                elif event.key == pygame.K_UP:
                    dx = 0
                    dy = - snake_size

                elif event.key == pygame.K_DOWN:
                    dx = 0
                    dy = snake_size

                else:
                    dx = 0
                    dy = 0

        if x >= screen_width or x < 0 or y >= screen_height or y < 0:
            game_close = True

        x += dx
        y += dy
        screen.fill(blue)

        drawFOOD(food_x, food_y)

        snake_head = []
        snake_head.append(x)
        snake_head.append(y)

        snake_list.append(snake_head)

        if len(snake_list) > snake_length:
            del snake_list[0]

        for p in snake_list [:-1] :
            if p == snake_head :
                game_close = True

        drawSNAKE (snake_size, snake_list)
        showSCORE (snake_length - 1)

        pygame.display.update()

        if x == food_x and y == food_y :
            food_x = round(random.randrange(0, screen_width - snake_size) / 10.0) * 10.0
            food_y = round(random.randrange(0, screen_height - snake_size) / 10.0) * 10.0
            snake_length += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLOOP()




