# Brian's Brain in Pygame
# Code not written by me, I just made it brian's brain.


# 0 = Dead cell
# 1 = Wire
# 2 = Header
# 3 = Tail

# A - Run simulation
# S - Advance 1 frame


import sys
import pygame
import random

YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (30, 144, 255)
BLACK = (0, 0, 0)
GREY = (20, 20, 20)

size = (width, height) = 1200, 750

pygame.init()

win = pygame.display.set_mode(size)
clock = pygame.time.Clock()

s = 15
cols, rows = int(win.get_width()/s), int(win.get_height()/s)

grid = []
for i in range(rows):
    arr = []
    for j in range(cols):
        arr.append(0)
    grid.append(arr)


def count(grid, x, y):
    c = 0
    isAlive = False
    for i in range(-1, 2):
        for j in range(-1, 2):
            col = (y+j+cols) % cols
            row = (x+i+rows) % rows
            if grid[row][col] == 2:
                c += 1
    return c


while True:

    nextFrame = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            tile = int(
                pygame.mouse.get_pos()[0]/s), int(pygame.mouse.get_pos()[1]/s)
            if event.button == 1:
                grid[tile[1]][tile[0]] = 1
            elif event.button == 2:
                grid[tile[1]][tile[0]] = 2
            elif event.button == 3:
                grid[tile[1]][tile[0]] = 0
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_s:
                nextFrame = True

    win.fill((BLACK))

    # DRAWING CODE
    for i in range(cols):
        for j in range(rows):
            x = i * s
            y = j * s
            if grid[j][i] == 3:
                pygame.draw.rect(win, BLUE, (x, y, s, s))
            elif grid[j][i] == 2:
                pygame.draw.rect(win, RED, (x, y, s, s))
            elif grid[j][i] == 1:
                pygame.draw.rect(win, YELLOW, (x, y, s, s))
            elif grid[j][i] == 0:
                pygame.draw.rect(win, BLACK, (x, y, s, s))
            pygame.draw.line(win, GREY, (x, y), (x, height))
            pygame.draw.line(win, GREY, (x, y), (width, y))

    #  Makes new_grid old_grid
    new_grid = []
    for i in range(rows):
        arr = []
        for j in range(cols):
            arr.append(0)
        new_grid.append(arr)

    for i in range(cols):
        for j in range(rows):
            neighbors = count(grid, j, i)
            state = grid[j][i]
            if state == 0:
                new_grid[j][i] = 0
            if state == 2:
                new_grid[j][i] = 2
            if state == 3:
                new_grid[j][i] = 3
            if state == 1 and (neighbors == 1 or neighbors == 2):
                new_grid[j][i] = 1
            elif state == 1:
                new_grid[j][i] = 1

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a] or nextFrame is True:
        # Cellular atomate logic
        for i in range(cols):
            for j in range(rows):
                neighbors = count(grid, j, i)
                state = grid[j][i]

                if state == 0:
                    new_grid[j][i] = 0
                if state == 2:
                    new_grid[j][i] = 3
                if state == 3:
                    new_grid[j][i] = 1
                if state == 1 and (neighbors == 1 or neighbors == 2):
                    new_grid[j][i] = 2
                elif state == 1:
                    new_grid[j][i] = 1

    grid = new_grid
    clock.tick(15)
    pygame.display.flip()
