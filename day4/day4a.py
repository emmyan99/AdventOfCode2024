def main():
    puzzle_input = []
    with open('input.txt') as f:
        for line in f:
            puzzle_input.append(list(line.strip()))
        print(puzzle_input)

    #word counter
    wc = 0

    for row in range(len(puzzle_input)):
        for col in range(len(puzzle_input[0])):
            if puzzle_input[row][col] == "X":
                wc = check_neighbours(puzzle_input, row, col, wc)

    print(wc)

#need2 catch outisde of index error
def check_neighbours(puzzle_input, row, col, wc):

    # go down
    if len(puzzle_input) > row+3: 
        if puzzle_input[row+1][col] == "M":
            if puzzle_input[row+2][col] == "A":
                if puzzle_input[row+3][col] == "S":
                    wc += 1

        # go right down diagonal
        if len(puzzle_input[0]) > col+3:
            if puzzle_input[row+1][col+1] == "M":
                if puzzle_input[row+2][col+2] == "A":
                    if puzzle_input[row+3][col+3] == "S":
                        wc += 1

        # go left down diagonal
        if col-3 > -1:
            if puzzle_input[row+1][col-1] == "M":
                if puzzle_input[row+2][col-2] == "A":
                    if puzzle_input[row+3][col-3] == "S":
                        wc += 1


                
    # go up
    if row-3 >= 0:
        if puzzle_input[row-1][col] == "M":
            if puzzle_input[row-2][col] == "A":
                if puzzle_input[row-3][col] == "S":
                    wc += 1
        
        # go up right diagonal
        if len(puzzle_input) > col+3:
            if puzzle_input[row-1][col+1] == "M":
                if puzzle_input[row-2][col+2] == "A":
                    if puzzle_input[row-3][col+3] == "S":
                        wc += 1

        # go up left diagonal
        if col-3 >= 0:
            if puzzle_input[row-1][col-1] == "M":
                if puzzle_input[row-2][col-2] == "A":
                    if puzzle_input[row-3][col-3] == "S":
                        wc += 1



    # go right
    if len(puzzle_input[0]) > col+3:
        if puzzle_input[row][col+1] == "M":
            if puzzle_input[row][col+2] == "A":
                if puzzle_input[row][col+3] == "S":
                    wc += 1

    # go left
    if col-3 >= 0:
        if puzzle_input[row][col-1] == "M":
            if puzzle_input[row][col-2] == "A":
                if puzzle_input[row][col-3] == "S":
                    wc += 1
                
    return wc 


    
if __name__ == '__main__':
    main()
