import numpy as np

def part1():
    with open("input.txt") as file:
        lines = []
        for line in file:
            lines.append(list(line.strip()))
        grid = np.array(lines)
        start = np.where(grid == '^')
        posX = start[0][0]
        posY = start[1][0]
        grid[posX][posY] = 1
        direction = "up"

        loop = True
        flagV = True
        while loop:
            if direction == "up" and loop:
                while grid[posX-1][posY] != '#' and posX-1 > 0:
                    posX -= 1
                    grid[posX][posY] = 1
                if grid[posX-1][posY] == '#':
                    direction = "right"
                elif posX-1 == 0:
                    loop = False
            if direction == "right" and loop:
                while grid[posX][posY+1] != '#' and posY+1 != len(grid[0])-1:
                    posY += 1
                    grid[posX][posY] = 1
                if grid[posX][posY+1] == '#':
                    direction = "down"
                elif posY+1 == len(grid[0])-1:
                    loop = False
            if direction == "down" and loop:
                while grid[posX+1][posY] != '#' and posX+1 != len(grid) - 1:
                    posX += 1
                    grid[posX][posY] = 1
                if grid[posX+1][posY] == '#':
                    direction = "left"
                elif posX+1 == len(grid)-1:
                    loop = False
            if direction == "left" and loop:
                while grid[posX][posY-1] != '#' and posY-1 > 0:
                    posY -= 1
                    grid[posX][posY] = 1
                if grid[posX][posY-1] == '#':
                    direction = "up"
                elif posY-1 == 0:
                    loop = False

        print(len(np.where(grid == '1')[0])+1)



part1()
