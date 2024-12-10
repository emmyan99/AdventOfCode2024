from enum import Enum

class Direction(Enum):
    UP = '^'
    DOWN = 'v'
    LEFT = '<'
    RIGHT = '>'

def main ():
    map_ = []
    with open ('input.txt') as f:
        for line in f:
            map_.append(list(line.strip()))

    row, column, direction = find_guard(map_)
    print("Guard is at " +str(row) +", "+ str(column))

    steps = 1
    amount = move_guard(row, column, map_, direction, steps)

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
            
            
def move_guard(row, column, map_, direction, steps):
    OBSTACLE = "#"

    if direction == Direction.UP:
        for i in range(row): # does ot include row 
            if map_[i][column] == OBSTACLE:
                print("obstacle found at " + str(i) +", "+ str(column))
                steps += row - (i+1)
                print(steps)



if __name__ == '__main__':
    main()