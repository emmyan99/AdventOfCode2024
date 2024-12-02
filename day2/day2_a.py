def main():
    reports = list(word.split() for word in open('input.txt'))

    safeCount = 0
    safeCount = sum(1 for report in reports if safetyCheck(report))
    print(safeCount)

def safetyCheck(report):
    differences = []
    for i in range(len(report)-1):
        differences.append(int(report[i]) - int(report[i+1]))
    
    print(differences)
    res = (all(abs(difference) <= 3 for difference in differences)) and (all(difference > 0 for difference in differences) or all(difference < 0 for difference in differences))
    return res

if __name__ == '__main__':
    main()