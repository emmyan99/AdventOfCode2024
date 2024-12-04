import re

#misunderstood instructions :(

def main():
    with open('input.txt') as f:
        input = f.read()
    #print(input)

    #instructions enabled at start, until the first don't is find
    dont_index = input.find("don't")
    #print(dont_index)

    to_sum = []
    #complete all instructions until dont index
    to_sum = mulFunc(input[:dont_index], to_sum)
    #remove completed instructions, until and including 'don't'
    input = input[dont_index+5:]


    while(instructionsLeft(input)):
        dont_index = input.find("don't")
        do_index = input.find("do")
        #if index is same, don't has been found
        if do_index == dont_index:
            #keep instructions from dont to end 
            input = input[dont_index+5:]
        elif do_index != dont_index and do_index > 0:
            #keep instructions from do to end
            input = input[do_index+2:]
            if dont_index != -1:
                to_sum = mulFunc(input[:dont_index], to_sum)
                input = input[dont_index+5:]
            else:
                to_sum = mulFunc(input, to_sum)
        else:
            input = ""


    print(sum(to_sum))


def instructionsLeft(input):
    dont_index = input.find("don't")
    do_index = input.find("do")

    if dont_index == -1 and do_index == -1:
        return False
    else:
        return True


def mulFunc(input, to_sum):
    x = re.findall("mul[\(\[]\d+,\d+[\)]", input)
    #print(x)

    for expr in x:
        expr = expr[3:]
        expr = expr.split(",")
        expr[0] = expr[0][1:]
        expr[1] = expr[1][:-1]
        to_sum.append(int(expr[0]) * int(expr[1]))
    
    return to_sum

if __name__ == '__main__':
    main()
