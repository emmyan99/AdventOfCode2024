from enum import Enum
import numpy as np


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

    location, direction = find_guard(map_)
    print("Guard is at " +str(location[0]) +", "+ str(location[1]))

    steps = 1
    locations = []
    exited = False
    # run guard walk sim once, to find his path
    while not exited:
        steps, location, direction, exited, locations = take_step(steps, location, direction, exited, map_, locations)

    for possible_obstacle_location in locations:
        # create one map for each possible obstacle location (only placed on the path that the guard would walk usually)
        modified_map = map_.copy()
        modified_map[possible_obstacle_location[0]][possible_obstacle_location[1]] = '#'
        # take steps until duplicate locations found in locations or until exited
        # if exited -> not viable location for obstalce
        # if not exited -> viable location for obstacle

        
    # print(steps)


def find_guard(map_):
    for row in range(len(map_)):
        for column in range(len(map_[row])):
            if map_[row][column] == Direction.UP.value:
                location = np.array([row, column])
                direction = np.array([-1, 0])

            elif map_[row][column] == Direction.DOWN.value:
                location = np.array([row, column])
                direction = np.array([1, 0])

            elif map_[row][column] == Direction.RIGHT.value:
                location = np.array([row, column])
                direction = np.array([0, 1])

            elif map_[row][column] == Direction.LEFT.value:                        
                location = np.array([row, column])
                direction = np.array([0, -1])

    return location, direction
            
            
def take_step(steps, location, direction, exited, map_, locations):
    OBSTACLE = "#"

    locations.append(location)

    switchDir = {
        (-1,0) : (0,1), # up -> right
        (0,1) : (1,0), # right -> down
        (1,0) : (0,-1), # down -> left
        (0,-1) : (-1,0), # left -> up
    }

    new_location = location + direction

    if out_of_bounds(new_location, map_):
        exited = True
        return steps, location, direction, exited, locations
    elif map_[new_location[0]][new_location[1]] == OBSTACLE:
        #print("Obstacle found at " + str(new_location[0]) + " " + str(new_location[1]))
        dir_tuple = (direction[0], direction[1])
        new_dir = switchDir[dir_tuple]
        direction = np.array([new_dir[0], new_dir[1]])
        #print(direction)
    else:
        #print("inc step at " + str(new_location[0]) + " " + str(new_location[1]))
        visited = any(np.array_equal(arr, new_location) for arr in locations)
        if not visited: steps += 1
        location = new_location

    return steps, location, direction, exited, locations


def out_of_bounds(location, map_):
    if location[0] > (len(map_)-1) or location[0] < 0 or location[1] > (len(map_)-1) or location[1] < 0:
        return True
    return False


if __name__ == '__main__':
    main()
