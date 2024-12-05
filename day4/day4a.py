def main():
    input = []
    with open('input.txt') as f:
        for line in f:
            input.append(list(line.strip()))
        print(input)

    word = "xmas"
    #word counter
    wc = 0

    for row in range(len(input)):
        for col in range(len(input[0])):
            if input[row][col] == "X":
                amount_found = check_neighbours(row, col, "M")
                wc += amount_found

    print(wc)

#need2 catch outisde of index error
def check_neighbours(row, col, nletter):
    amount_found = 0 #unsure
    # ugly and hard coded for corner X for now >:(
    if input[row][col+1] == nletter:
        #use word[next letter to find] recursively
        print("yipii")
    if input[row+1][col] == nletter:
        pass
    if input[row+1][col+1] == nletter:
        pass
    return amount_found
# once S is found, amount_found can be incremented? 


if __name__ == '__main__':
    main()
