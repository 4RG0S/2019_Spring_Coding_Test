def solution(arr):
    # variable
    stack = []
    compare = 0
    result = 0

    for idx in range(len(arr)):
        # If opening parentheses, push from stack
        if arr[idx] == '{':
            stack.append(0)
        elif arr[idx] == '[':
            stack.append(1)
        elif arr[idx] == '(':
            stack.append(2)
        elif arr[idx] == '<':
            stack.append(3)

        # If closing parentheses, pop from stack
        if arr[idx] == '}' or arr[idx] == ']' or arr[idx] == ')' or arr[idx] == '>':
            if arr[idx] == '}':
                compare = 0
            elif arr[idx] == ']':
                compare = 1
            elif arr[idx] == ')':
                compare = 2
            elif arr[idx] == '>':
                compare = 3

            # If the value of the parentheses is the same as the value of pop
            # result is 1
            if compare == stack.pop():
                result = 1
            else:
                return 0

    return result


if __name__ == '__main__':
    for i in range(10):
        case_len = int(input().strip())
        data = list(input().strip())
        print("#" + str(i + 1) + " " + str(solution(data)))
