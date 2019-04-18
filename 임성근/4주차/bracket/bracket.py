def solution():
    f = open('bracket_input.txt', 'r')

    problem_number = 1
    while True:
        index = f.readline()
        data = f.readline()
        if not index:
            break

        array = []
        for k in range(int(index)):
            array.append(data[k])

        a1 = a2 = a3 = a4 = a5 = a6 = a7 = a8 = 0

        for i in range(len(array)):
            if array[i] == '{':
                a1 += 1
            elif array[i] == '[':
                a2 += 1
            elif array[i] == '(':
                a3 += 1
            elif array[i] == '<':
                a4 += 1
            elif array[i] == '}':
                a5 += 1
            elif array[i] == ']':
                a6 += 1
            elif array[i] == ')':
                a7 += 1
            elif array[i] == '>':
                a8 += 1
        #print(a1, a2, a3, a4, a5, a6, a7, a8)

        if a1 == a5 and a2 == a6 and a3 == a7 and a4 == a8:
            print('#' + str(problem_number), 1)
        else:
            print('#' + str(problem_number), 0)

        problem_number += 1


if __name__ == "__main__":
    solution()