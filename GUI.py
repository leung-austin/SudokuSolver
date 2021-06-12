import pygame
import sys
from solver import solve, is_safe, getBoard
from pygame.locals import *
from copy import deepcopy

pygame.font.init()
FPS = 60

grid = getBoard()
temp = deepcopy(grid)

# Creating screen and grid
SCREEN_SIZE = 90
SCREEN_MULTIPLIER = 5  # Modify this number to change screen size
SCREEN_WIDTH = SCREEN_SIZE * SCREEN_MULTIPLIER
SCREEN_HEIGHT = SCREEN_SIZE * SCREEN_MULTIPLIER
BOX_SIZE = (SCREEN_SIZE * SCREEN_MULTIPLIER) // 3
CELL_SIZE = BOX_SIZE // 3


# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_GRAY = (200, 200, 200)
RED = (255, 0, 0)

dif = SCREEN_WIDTH / 9
font1 = pygame.font.SysFont("comicsans", 40)
font2 = pygame.font.SysFont("comicsans", 20)


def solver(grid, i, j):

    while grid[i][j] != 0:
        if i < 8:
            i += 1
        elif i == 8 and j < 8:
            i = 0
            j += 1
        elif i == 8 and j == 8:
            return True
    pygame.event.pump()
    for it in range(1, 10):
        if is_safe(grid, (i, j), it) == True:
            grid[i][j] = it
            global x_coord, y_coord
            x_coord = i
            y_coord = j
            # white color background
            SCREEN.fill((255, 255, 255))
            draw()
            draw_box(0)
            pygame.display.update()
            pygame.time.delay(20)
            if solver(grid, i, j) == 1:
                return True
            else:
                grid[i][j] = 0
            # white color background
            SCREEN.fill((255, 255, 255))

            draw()
            draw_box(0)
            pygame.display.update()
            pygame.time.delay(50)
    return False


def draw_box(color):
    if color == 0:
        for i in range(2):
            pygame.draw.line(SCREEN, (RED), (y_coord * dif-3,
                                             (x_coord + i)*dif), (y_coord * dif + dif + 3, (x_coord + i)*dif), 4)
            pygame.draw.line(SCREEN, (RED), ((y_coord + i) * dif,
                                             x_coord * dif), ((y_coord + i) * dif, x_coord * dif + dif), 4)
        selected = 0
    else:
        for i in range(2):
            pygame.draw.line(SCREEN, (WHITE), (y_coord * dif-3,
                                               (x_coord + i)*dif), (y_coord * dif + dif + 3, (x_coord + i)*dif), 4)
            pygame.draw.line(SCREEN, (WHITE), ((y_coord + i) * dif,
                                               x_coord * dif), ((y_coord + i) * dif, x_coord * dif + dif), 4)


def draw():
    # Draw the lines

    for i in range(9):
        for j in range(9):
            if grid[i][j] != 0:
                # Fill blue color in already numbered grid
                pygame.draw.rect(SCREEN, LIGHT_GRAY,
                                 (j * dif, i * dif, dif + 1, dif + 1))

                # Fill grid with default numbers specified
                text1 = font1.render(str(grid[i][j]), 1, BLACK)
                SCREEN.blit(text1, (j * dif + 15, i * dif + 15))

    # Draw lines horizontally and verticallyto form grid
    for i in range(10):
        if i % 3 == 0:
            thick = 7
        else:
            thick = 1
        pygame.draw.line(SCREEN, (0, 0, 0), (0, i * dif),
                         (500, i * dif), thick)
        pygame.draw.line(SCREEN, (0, 0, 0), (i * dif, 0),
                         (i * dif, 500), thick)


def get_coord(pos):
    global x_coord, y_coord
    y_coord = pos[0] // dif
    x_coord = pos[1] // dif


def draw_val(val):
    pygame.draw.rect(SCREEN, WHITE,
                     (y_coord * dif, x_coord * dif, dif + 1, dif + 1))
    text1 = font1.render(str(val), 1, (0, 0, 0))
    SCREEN.blit(text1, (y_coord * dif + 15, x_coord * dif + 15))


def draw_grid():
    # Draw minor lines
    for x in range(0, SCREEN_WIDTH, CELL_SIZE):
        pygame.draw.line(SCREEN, LIGHT_GRAY, (x, 0), (x, SCREEN_HEIGHT))
    for y in range(0, SCREEN_HEIGHT, CELL_SIZE):
        pygame.draw.line(SCREEN, LIGHT_GRAY, (0, y), (SCREEN_WIDTH, y))

    # Draw major lines
    for x in range(0, SCREEN_WIDTH, BOX_SIZE):
        pygame.draw.line(SCREEN, BLACK, (x, 0), (x, SCREEN_HEIGHT), 4)
    for y in range(0, SCREEN_HEIGHT, BOX_SIZE):
        pygame.draw.line(SCREEN, BLACK, (0, y), (SCREEN_WIDTH, y), 4)


def main():
    global SCREEN, CLOCK
    pygame.init()
    val = 0
    selected = 0
    solution = 0
    flag2 = 0
    CLOCK = pygame.time.Clock()
    SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption('Sudoku w/ Solver')

    SCREEN.fill(WHITE)

    draw()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                val = 0
                if selected == 1:
                    draw_box(1)
                pos = pygame.mouse.get_pos()
                selected = 1
                get_coord(pos)
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    val = 1
                if event.key == pygame.K_2:
                    val = 2
                if event.key == pygame.K_3:
                    val = 3
                if event.key == pygame.K_4:
                    val = 4
                if event.key == pygame.K_5:
                    val = 5
                if event.key == pygame.K_6:
                    val = 6
                if event.key == pygame.K_7:
                    val = 7
                if event.key == pygame.K_8:
                    val = 8
                if event.key == pygame.K_9:
                    val = 9
                if event.key == pygame.K_RETURN:
                    flag2 = 1

        if flag2 == 1:
            if solver(grid, 0, 0) == False:
                error = 1
            flag2 = 0

        if val != 0 and grid[int(x_coord)][int(y_coord)] == 0:
            draw_val(val)

            if is_safe(grid, (int(x_coord), int(y_coord)), val):
                solution = solve(temp)
                if solution:
                    grid[int(x_coord)][int(y_coord)] = val
                    if grid[int(x_coord)][int(y_coord)] == temp[int(x_coord)][int(y_coord)]:
                        draw_box(1)
                    else:
                        grid[int(x_coord)][int(y_coord)] = 0
                        val = 0

        draw()
        if selected == 1 and grid[int(x_coord)][int(y_coord)] == 0:
            draw_box(0)

        pygame.display.update()
        CLOCK.tick(FPS)


if __name__ == '__main__':
    main()
