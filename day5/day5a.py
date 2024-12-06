def main():
    rules = []
    updates = []
    puzzle_input = []
    with open('input.txt') as f:
        for line in f:
            puzzle_input.append(line)

    newline_index = puzzle_input.index('\n')
            
    rules_list = puzzle_input[:newline_index] 
    updates = puzzle_input[newline_index+1:]  

    rules_list = [rule.strip() for rule in rules_list]
    updates = [update.strip() for update in updates]
    
    rules = {}
    for i in range(len(rules_list)):
        rules_list[i] = rules_list[i].split("|")
        rules[rules_list[i][0]] = rules_list[i][1]
        #print(rules_list[i][0] + " must come before " + rules_list[i][1])

    correct_order = []
    correct_order = handle_updates(updates, rules, correct_order)


def handle_updates(updates, rules, correct_order): 

    for line in updates:
        start = 0
        end = 2

        while len(line) > end:
            line = ''.join(char for char in line if char != ',')
            #print(line)
            print(line[start:end])
            start += 2
            end += 2

            
    
if __name__ == '__main__':
    main()
