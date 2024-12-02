def main():
    with open('input.txt') as f:
        input = tuple(int(num) for line in f for num in line.split())

    left_list = []
    right_list = []
    index = 0
    for number in input:
        if index % 2 == 0:
            left_list.append(number)
            index += 1
        else:
            right_list.append(number)
            index += 1

    sorted_left = quicksort(left_list)
    sorted_right = quicksort(right_list)

    all_distances = []
    for left, right in zip(sorted_left, sorted_right):
        print(left, right, abs(left-right))
        all_distances.append(abs(left - right))

    print(sum(all_distances))

def quicksort(l:list):
    arr = l[::]
    if len(arr) <= 1:
        return arr
    l = [x for x in arr[1:] if x <= arr[0]]
    r = [x for x in arr[1:] if x > arr[0]]
    return quicksort(l) + arr[0:1] + quicksort(r)

if __name__ == '__main__':
    main()
