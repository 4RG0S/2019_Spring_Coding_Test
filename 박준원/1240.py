def convert_to_number(code):
    if code == '0001101':
        return 0
    elif code =='0011001':
        return 1
    elif code == '0010011':
        return 2
    elif code == '0111101':
        return 3
    elif code == '0100011':
        return 4
    elif code == '0110001':
        return 5
    elif code == '0101111':
        return 6
    elif code == '0111011':
        return 7
    elif code == '0110111':
        return 8
    elif code == '0001011':
        return 9
    else:
        return -1

def find_code_location(matrix, height, weight):
    start_index = 0
    start_row = 0

    for i in range(0, height):
        row = matrix[i]
        start_row = i
        for k in range(weight - 1, -1, -1):
            if row[k] is '1':
                start_index = k - 56 + 1
                break
            if k < 55:
                break

        if start_index is not 0:
            break

    return start_row, start_index

def extract_code(matrix, height, weight):
    start_row, start_index = find_code_location(matrix, height, weight)

    return matrix[start_row][start_index:start_index+56]

def result(code):
    num = []
    for i in range(0, 8):
        tmp = code[i*7:i*7+7]
        num.append((convert_to_number(tmp)))

    tmp = (num[0] + num[2] + num[4] + num[6]) * 3 + num[1] + num[3] + num[5] + num[7]
    if tmp % 10 == 0:
        return sum(num)
    else:
        return 0


case = int(input())
for p in range(0, case):
    tmp = list(map(int, input().strip().split()))
    height, weight = tmp[0], tmp[1]

    matrix = []

    for i in range(0, height):
        row = input()
        matrix.append(row)

    code = extract_code(matrix, height, weight)

    print('#{} {}'.format(p + 1, result(code)))