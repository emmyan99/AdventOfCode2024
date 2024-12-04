import re

def main():
    with open('input.txt') as f:
        input = f.read()
    #print(input)

    dont_index = input.find("don't()")
    do_index = input.find("do()")


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
