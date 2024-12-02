def main():
    with open('input.txt') as f:
        input = tuple(int(num) for line in f for num in line.split())

    left_list = input[0::2] 
    right_list = input[1::2] 

    counts = []
    for number_l in left_list:
        right_count = 0
        for number_r in right_list:
            if number_r == number_l:
                right_count += 1
        counts.append(number_l * right_count)

    print(sum(counts))

if __name__ == '__main__':
    main()
