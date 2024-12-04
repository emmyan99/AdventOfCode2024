import re

def main():
    with open('input.txt') as f:
        input = f.read()
    print(input)

    # do a while loop that slices out do/dont strips removes or sends to mulFunc
    dont_index = input.find("don't")
    print(dont_index)

    toSum = []
    toSum = mulFunc(input[:20], toSum)
    print(input[:20])
    print(toSum)


def mulFunc(input_, toSum):
    x = re.findall("mul[\(\[]\d+,\d+[\)]", input_)
    print(x)

    for expr in x:
        expr = expr[3:]
        expr = expr.split(",")
        expr[0] = expr[0][1:]
        expr[1] = expr[1][:-1]
        toSum.append(int(expr[0]) * int(expr[1]))
    
    return toSum

if __name__ == '__main__':
    main()
