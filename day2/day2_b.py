def main():
    reports = list(word.split() for word in open('input.txt'))

    failed_reports = []
    for report in reports:  
        safety_check(report, failed_reports)
    safe_count = len(reports) - len(failed_reports)

    made_safe = 0
    for report in failed_reports:
        if make_safe(report):
            made_safe += 1
    safe_count += made_safe

    print(safe_count)

def safety_check(report, failed_reports):
    differences = []
    for i in range(len(report)-1):
        differences.append(int(report[i]) - int(report[i+1]))

    res = (all(abs(difference) <= 3 for difference in differences)) and (all(difference > 0 for difference in differences) or all(difference < 0 for difference in differences))
    if not(res):
        failed_reports.append(report)
    return res

def make_safe(report): 
    placeholder = []
    for index in range(len(report)):
        one_val_removed = report[:index] + report[index+1:]
        if safety_check(one_val_removed, placeholder):
            return True
    return False

if __name__ == '__main__':
    main()
