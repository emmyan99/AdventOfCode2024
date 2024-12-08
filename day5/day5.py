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
    #print(rules)
    #print('\n')
    #print(updates)

def handle_updates(updates, rules, mid_numbers): 

    corrected_updates  = []   
    
    for line in updates:
        #valid_line = True # PART 1
        corrected = False
        for number in line:

            if number in rules:
                # PART 1:
                #if not check_order(line, number, rules):
                    #valid_line = False
                    #break
                
                while not (check_order(line, number, rules)):
                    corrected_line = correct_order(line, number, rules)
                    corrected = True
                
        if corrected:
            corrected_updates.append(corrected_line)
            print("corrected line: " + str(corrected_line))
            print("corrected updates: " + str(corrected_updates))
    
    print(f"Total corrected lines: {len(corrected_updates)}")
    for line in corrected_updates:
        mid_numbers.append(line[int(len(line)//2)])
        #print(mid_numbers)


        # PART 1:
        #if valid_line:
            #print("line" +  str(line) + " is valid ")
            #mid_numbers.append(line[int(len(line)/2)])
        print(mid_numbers)


    return mid_numbers

def correct_order(line, key, rules):
    print("handling line " + str(line))
    for value in rules[key]:
        if value in line:
            value_index = line.index(value)
            key_index = line.index(key)
            # print(str(value) + " is at " + str(value_index) + " in line " + str(line))
             
            # swap places
            if key_index > value_index:
                print("swapping " + str(value) + " and key: " + str(key))
                line[key_index] = value
                line[value_index] = key
    return line

def check_order(line, key, rules):
    for value in rules[key]:
        if value in line:
            value_index = line.index(value)
            key_index = line.index(key)

            # key should be before value
            if key_index > value_index:
                print(str(key) + " comes after " + str(value) + " in line " + str(line))
                return False
            
    return True

def convert_rules_to_int(rules):
    int_rules = {}
    for key, value in rules.items():
        int_rules[int(key)] = [int(val) for val in value]
    return int_rules

if __name__ == '__main__':
    main()
