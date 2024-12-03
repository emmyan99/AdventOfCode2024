import re

def main():
    with open('input.txt') as f:
        input = f.read()
    print(input)

    x = re.findall("mul[\(\[]\d+,\d+[\)]", input)
    print(x)
    
    toSum = []
    for expr in x:
        expr = expr[3:]
        #UHHHHHHHHHHHHHHHHHHHHHH
        print(toSum)


    print(sum(toSum))

    


if __name__ == '__main__':
    main()



