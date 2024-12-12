from enum import Enum
import numpy as np

class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

class Step:
    UP = np.array([-1, 0])
    DOWN = np.array([1, 0])
    LEFT = np.array([0, -1])
    RIGHT = np.array([0, 1])

def main ():
    map_ = []
    with open ('input.txt') as f:
        for line in f:
            map_.append(list(line.strip()))

    row, column, direction = find_guard(map_)
    print("Guard is at " +str(row) +", "+ str(column))

    steps = 0
    while not out_of_bounds(row, column, map_):
        steps, direction, row, column = take_step(row, column, map_, direction, steps)

    #print(sum(steps))

def find_guard(map_):
    for row in range(len(map_)):
        for column in range(len(map_[row])):
            if map_[row][column] == Direction.UP.value:
                return row, column, Direction.UP
            elif map_[row][column] == Direction.DOWN.value:
                return row, column, Direction.DOWN
            elif map_[row][column] == Direction.RIGHT.value:
                return row, column, Direction.RIGHT
            elif map_[row][column] == Direction.LEFT.value:
                return row, column, Direction.LEFT
            
            
def take_step(row, column, map_, direction, steps):
    OBSTACLE = "#"

    current_location = np.array([row, column])
    
    if direction == Direction.UP:
        new_location = current_location + Step.UP
        row, col = new_location
        if map_[row][col] == OBSTACLE:
            return steps, Direction.DOWN, column, row
        if out_of_bounds:
            return steps, Direction.UP, column, row
        else:
            steps += 1
            return steps, Direction.UP, column, (row+1)

    #if direction == Direction.DOWN:
    #if direction == Direction.LEFT:
    #if direction == Direction.RIGHT:

def out_of_bounds(row, col, map_):
    if row > len(map_) or row < 0 or col > len(map_[row]) or col < 0:
        return True
    return False



                



if __name__ == '__main__':
    main()