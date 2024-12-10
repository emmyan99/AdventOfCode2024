def main():

    rules_list = []
    puzzle_input = []
    with open('input.txt') as f:
        for line in f:
            puzzle_input.append(line)

    newline_index = puzzle_input.index('\n')
            
    rules_list  = puzzle_input[:newline_index] 
    updates = puzzle_input[newline_index+1:]

    rules_list  = [rule.strip().split("|") for rule in rules_list ]
    updates = [update.strip() for update in updates]
    updates = [list(map(int, update.split(','))) for update in updates]

    rules = {}
    for i in range(len(rules_list)):
        if rules_list[i][0] not in rules:
            rules[rules_list[i][0]] = [rules_list[i][1]]
        else:
            rules[rules_list[i][0]].append(rules_list[i][1])
    rules = convert_rules_to_int(rules)
        
    mid_numbers = []
    mid_numbers = handle_updates(updates, rules, mid_numbers)

    print(sum(mid_numbers))


def handle_updates(updates, rules, mid_numbers):
    for line in updates:
        corrected = False
        
        while not (check_order(line, rules)):   
            line = correct_order(line, rules)
            corrected = True
        
        if corrected:
            mid_numbers.append(line[len(line)//2])
            #print(mid_numbers)

    return mid_numbers


def correct_order(line, rules):
    for update_value in line:
        if update_value in rules:
            
            for value in rules[update_value]:
                if value in line:

                    rule_index = line.index(update_value)
                    value_index = line.index(value)

                    if rule_index > value_index:
                        line[rule_index] = value
                        line[value_index] = update_value
                        
    return line


def check_order(line, rules):
    #print("I will check line: "+ str(line) + " for value " + str(rule_key) + "\n" + "  Rule values are" + str(rules[rule_key]))
    for update_value in line:
        if update_value in rules:
            
            for value in rules[update_value]:
                if value in line:

                    rule_index = line.index(update_value)
                    value_index = line.index(value)

                    if rule_index > value_index:
                        return False
    return True


def convert_rules_to_int(rules):
    int_rules = {}
    for key, value in rules.items():
        int_rules[int(key)] = [int(val) for val in value]
    return int_rules


if __name__ == '__main__':
    main()
