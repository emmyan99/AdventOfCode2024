def main():
    reports = list(word.split() for word in open('input.txt'))

    safeCount = 0
    # safeCount = sum(1 for report in reports if safetyCheck(report))
    failed_checks = []
    for report in reports:  
        safety_check(report, failed_checks)
    # print(failed_checks)
    safe_count = len(reports) - len(failed_checks)
    # print(safeCount)
    print(failed_checks)

    #count = make_safe(failed_checks)
    #safe_count += count

    

def safety_check(report, failed_checks):
    differences = []
    for i in range(len(report)-1):
        differences.append(int(report[i]) - int(report[i+1]))
    
    #print(differences)
    res = (all(abs(difference) <= 3 for difference in differences)) and (all(difference > 0 for difference in differences) or all(difference < 0 for difference in differences))
    if not(res):
        failed_checks.append((differences, report))


def make_safe(failed_checks):
    for check in failed_checks:
        pass  


# if only one number is >3
# if only one number is negative while all other pos
# if only one number pos while all other negative 
    
if __name__ == '__main__':
    main()
