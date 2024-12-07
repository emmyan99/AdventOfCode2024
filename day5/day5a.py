def main():
    puzzle_input = []
    with open('input.txt') as f:
        for line in f:
            puzzle_input.append(line)

    newline_index = puzzle_input.index('\n')
            
    rules = puzzle_input[:newline_index] 
    updates = puzzle_input[newline_index+1:]

    rules = [rule.strip().split("|") for rule in rules]
    updates = [update.strip() for update in updates]
    for i in range(len(updates)):
        updates[i] = updates[i].replace(",", "")

    correct_order = []
    correct_order = handle_updates(updates, rules, correct_order)

    print(rules)
    print('\n')
    print(updates)

def handle_updates(updates, rules, correct_order): 

    for line in updates:
        start = 0
        end = 2

        while len(line) > start:
            #print(line[start:end])
            for rule in rules:
                if line[start:end] == rule[0]:
                    print(line[start:end] + " must come before " + rule[1])
                    if line.find(rule[1]) != -1:
                        print(rule[1], "is also in the list!")
                        line = handle_rule(line, rule[0], rule[1])
            start += 2
            end += 2


    return correct_order


def handle_rule(line, before, after):
    print(line)
    before_index = line.index(before)
    after_index = line.index(after)

    #if after_index < before_index:


    print(before_index, after_index)

    
if __name__ == '__main__':
    main()
