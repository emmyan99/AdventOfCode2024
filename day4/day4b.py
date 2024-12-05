def main():
    puzzle_input = []
    with open('input.txt') as f:
        for line in f:
            puzzle_input.append(list(line.strip()))
        # print(puzzle_input)

    wc = 0

    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[0])):
            if puzzle_input[row][col] == "A":
                wc = check_neighbours(puzzle_input, row, col, wc)

    print(wc)

def check_neighbours(puzzle_input, row, col, wc):
    cross_neighbours = []

    # go down
    if len(puzzle_input) > row+1:
        if len(puzzle_input[0]) > col+1 and col-1 > -1:
            cross_neighbours.append(puzzle_input[row+1][col+1])
            cross_neighbours.append(puzzle_input[row+1][col-1])

    # go up
    if row-1 > -1:
        if len(puzzle_input[0]) > col+1 and col-1 > -1:
            cross_neighbours.append(puzzle_input[row-1][col-1])
            cross_neighbours.append(puzzle_input[row-1][col+1])
    
    if cross_neighbours == ['M', 'M', 'S', 'S'] or cross_neighbours == ['S', 'S', 'M', 'M'] or cross_neighbours == ['M', 'S', 'S', 'M'] or cross_neighbours == ['S', 'M', 'M', 'S']:
            wc += 1
    
        

    return wc



if __name__ == '__main__':
    main()
