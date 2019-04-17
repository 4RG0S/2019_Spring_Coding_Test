if __name__ == '__main__':
   # f = open("input.txt", 'r')

    for test_case in range(10):
        N = input().strip()
        bracket = list(input().strip())

        bracket1 = 0
        bracket2 = 0
        bracket3 = 0
        bracket4 = 0

        for i in range(int(N)):
            if bracket[i] == '(':
                bracket1 = bracket1+1
            elif bracket[i] == ')':
                bracket1 = bracket1-1
            elif bracket[i] == '[':
                bracket2 = bracket2+1
            elif bracket[i] == ']':
                bracket2 = bracket2-1
            elif bracket[i] == '{':
                bracket3 = bracket3+1
            elif bracket[i] == '}':
                bracket3 = bracket3-1
            elif bracket[i] == '<':
                bracket4 = bracket4+1
            elif bracket[i] == '>':
                bracket4 = bracket4-1

        if bracket1 == 0 and bracket2 == 0 and bracket3 == 0 and bracket4 == 0:
            print("#"+str(test_case+1)+" 1")
        else:
            print("#"+str(test_case+1)+" 0")
