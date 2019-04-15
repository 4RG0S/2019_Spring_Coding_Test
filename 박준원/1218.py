def isOpen(ch):
    return ch == '(' or ch == '[' or ch == '{' or ch == '<'

def isMatch(ch1, ch2):
    if ch1 == '(' and ch2 == ')':
        return True
    elif ch1 == '[' and ch2 == ']':
        return True
    elif ch1 == '{' and ch2 == '}':
        return True
    elif ch1 == '<' and ch2 == '>':
        return True
    else:
        return False

def main():
    for n in range(0, 10):
        length = int(input())
        str = input()

        stack = []
        result = 1

        for i in range(0, length):
            ch = str[i]

            if isOpen(ch):
                stack.append(ch)
            else:
                if isMatch(stack[-1], ch):
                    stack.pop()
                else:
                    result = 0
                    break

        if len(stack) != 0:
            result = 0

        print('#{} {}'.format(n + 1, result))

if __name__ =="__main__":
    main()

