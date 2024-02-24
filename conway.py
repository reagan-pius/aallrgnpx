#  Conway's game of life

import random, time, copy

WIDTH = 60
HEIGHT = 20

# list of list for the cells:

nextCells = []
for x in range(WIDTH):
    column = [] # creates a new column
    for y in range(HEIGHT):
        if random.randint(0,1) == 0:
            column.append("#")  # add a living cell
        else:
            column.append(" ")  # add a dead cell
    nextCells.append(column)    # nextCells is a list of column lists

#  main program loop 
while True:
    print("\n\n\n\n\n")     # separates each step with a newlines
    currentCells = copy.deepcopy(nextCells)

    # print currentCells on the screen:
    for y in range(HEIGHT):
        for x in range(WIDTH):
            # get neighbouring coordinates:
            # %WIDTH ensures lesftCoord is alwas between 0 and WIDTH - 1

            leftCoord = (x -1) % WIDTH
            rightCoord = (x + 1) % WIDTH
            aboveCoord = (y - 1) % HEIGHT
            belowCoord = (y + 1) % HEIGHT

            # count number of living neighbours:
            numNeighbours = 0
            if currentCells[leftCoord][aboveCoord] == "#":
                numNeighbours += 1   # top-left neighbout is alive
            if currentCells[x][aboveCoord] == '#':
                numNeighbours+= 1 # Top neighbor is alive.
            if currentCells[rightCoord][aboveCoord] == '#':
                numNeighbours += 1 # Top-right neighbor is alive.
            if currentCells[leftCoord][y] == '#':
                numNeighbours += 1 # Left neighbor is alive.
            if currentCells[rightCoord][y] == '#':
                numNeighbours += 1 # Right neighbor is alive.
            if currentCells[leftCoord][belowCoord] == '#':
                numNeighbours += 1 # Bottom-left neighbor is alive.
            if currentCells[x][belowCoord] == '#':
                numNeighbours += 1 # Bottom neighbor is alive.
            if currentCells[rightCoord][belowCoord] == '#':
                numNeighbours += 1 # Bottom-right neighbor is alive.
            # Set cell based on Conway's Game of Life rules:
            if currentCells[x][y] == '#' and (numNeighbours == 2 or numNeighbours == 3):
                # Living cells with 2 or 3 neighbors stay alive:
                nextCells[x][y] = '#'
            elif currentCells[x][y] == ' ' and numNeighbours == 3:
                # Dead cells with 3 neighbors become alive:
                nextCells[x][y] = '#'
            else:
                # Everything else dies or stays dead:
                nextCells[x][y] = ' '
    time.sleep(1) # Add a 1-second pause to reduce flickering.

def draw_map(width, height, entrance_pos, exit_pos, walls):
    for y in range(height):
        for x in range(width):
            if (x, y) == entrance_pos:
                print("E", end="")  # E for entrance
            elif (x, y) == exit_pos:
                print("X", end="")  # X for exit
            elif (x, y) in walls:
                print("#", end="")  # # for wall
            else:
                print(".", end="")  # . for empty space
        print()

def main():
    width = 10
    height = 5
    entrance_pos = (0, 0)
    exit_pos = (9, 4)
    walls = [(2, 1), (2, 2), (2, 3), (5, 3), (6, 3), (7, 3)]

    draw_map(width, height, entrance_pos, exit_pos, walls)

if __name__ == "__main__":
    main()
