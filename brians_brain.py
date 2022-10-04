# Brian's Brain in Pygame
# Code not written by me, I just made it brian's brain.

import pygame
import sys
import random

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
        #arr.append(random.randint(0, 2))
        var1 = random.randint(0, 5)
        if var1 == 0:
            arr.append(2)
        else:
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
            else:
                c += 0
            #c += grid[row][col]
    if grid[x][y] == 2:
        c -= 2
    else:
        c -= 0
    #c -= grid[x][y]
    return c


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            # print(pygame.mouse.get_pos())
            tile = int(
                pygame.mouse.get_pos()[0]/s), int(pygame.mouse.get_pos()[1]/s)
            grid[tile[1]][tile[0]] = 2
    win.fill((0, 0, 0))

    # DRAWING CODE
    for i in range(cols):
        for j in range(rows):
            x = i * s
            y = j * s
            if grid[j][i] == 2:
                pygame.draw.rect(win, (0, 0, 255), (x, y, s, s))
            elif grid[j][i] == 1:
                pygame.draw.rect(win, (100, 100, 100), (x, y, s, s))
            elif grid[j][i] == 0:
                pygame.draw.rect(win, (0, 0, 0), (x, y, s, s))
            pygame.draw.line(win, (20, 20, 20), (x, y), (x, height))
            pygame.draw.line(win, (20, 20, 20), (x, y), (width, y))

    #  Makes new_grid old_grid
    new_grid = []
    for i in range(rows):
        arr = []
        for j in range(cols):
            arr.append(0)
        new_grid.append(arr)

    # Cellular atomate logic
    for i in range(cols):
        for j in range(rows):
            neighbors = count(grid, j, i)
            state = grid[j][i]
            if state == 2:
                new_grid[j][i] = 1
            elif state == 1:
                new_grid[j][i] = 0
            elif state == 0 and neighbors == 2:
                new_grid[j][i] = 2
            else:
                new_grid[j][i] = state

    grid = new_grid
    clock.tick(60)
    pygame.display.flip()
