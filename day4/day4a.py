def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(list(line.strip()))
        print(input)

    #word counter
    wc = 0

    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == "X":
                amount_found = check_neighbours(row, col)
                wc += amount_found

    print(wc)


def check_neighbours(row, col):
    # ugly and hard coded for corner X for now >:(
    if input[row][col+1] == "M":
        print("yipii")
    if input[row+1][col] == "M":
        pass
    if input[row+1][col+1] == "M":
        pass
    return 0


if __name__ == '__main__':
    main()
