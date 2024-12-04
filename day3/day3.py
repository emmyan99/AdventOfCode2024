import re

def main():
    with open('input.txt') as f:
        input = f.read()

    x = re.findall("mul[\(\[]\d+,\d+[\)]", input)
    print(x)
    
    toSum = []
    for expr in x:
        expr = expr[3:] 
        expr = expr.split(",")
        expr[0] = expr[0][1:]
        expr[1] = expr[1][:-1]          
        toSum.append(int(expr[0]) * int(expr[1]))
        print(toSum)

    sum_ = 0
    sum_ = sum(toSum)
    print(sum_)


if __name__ == '__main__':
    main()



