import re

def main():
    with open('input.txt') as f:
        input = f.read()
    
    to_sum = []

    while(input):
        dont_index = input.find("don't()")

        if dont_index != -1:
            to_sum = mulFunc(input[:dont_index], to_sum)
            input = input[dont_index:]
            do_index = input.find("do()")
            if do_index != -1:
                input = input[do_index+len("do()"):]
            else:
                input = ""
        else:
            to_sum = mulFunc(input, to_sum)
            input = ""


    print(sum(to_sum))


def mulFunc(input, to_sum):
    x = re.findall("mul[\(\[]\d+,\d+[\)]", input)
    # print(x)

    for expr in x:
        expr = expr[3:]
        expr = expr.split(",")
        expr[0] = expr[0][1:]
        expr[1] = expr[1][:-1]
        to_sum.append(int(expr[0]) * int(expr[1]))
    
    return to_sum

if __name__ == '__main__':
    main()
