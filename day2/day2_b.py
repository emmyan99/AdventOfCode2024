#TODO:
    


def main():
    reports = list(word.split() for word in open('input.txt'))

    safeCount = 0
    #safeCount = sum(1 for report in reports if safetyCheck(report))
    for report in reports:  
        safetyCheck(report)
    #print(safeCount)

def safetyCheck(report):
    pass


    
if __name__ == '__main__':
    main()