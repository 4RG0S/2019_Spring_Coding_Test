#   Input : Binary
#   Output : Crypto Code
#   function : Receive binary and return crypto code
def convert_code(data):
    if data == '0001101':
        return 0
    if data == '0011001':
        return 1
    if data == '0010011':
        return 2
    if data == '0111101':
        return 3
    if data == '0100011':
        return 4
    if data == '0110001':
        return 5
    if data == '0101111':
        return 6
    if data == '0111011':
        return 7
    if data == '0110111':
        return 8
    if data == '0001011':
        return 9


# 2. Survey from the back and returns the index of the first 1 that appears.
def find_1(find_arr):
    # Verify that there is a 1 from the back in that row.
    for find_idx in reversed(range(len(find_arr))):
        # Existing.
        if find_arr[find_idx] == '1':
            return find_idx


# 4. Save the code crypto by separating seven digits from the start index.
def find_code(find_pass, i, j):
    arr = []
    new_arr = find_pass[i:j]

    # 7 digits separated and stored in code
    for i in range(8):
        code = ''.join(new_arr[i * 7:i * 7 + 7])
        convert = convert_code(code)
        arr.append(convert)

    result = (arr[0] + arr[2] + arr[4] + arr[6]) * 3 + arr[1] + arr[3] + arr[5] + arr[7]

    # if it's a multiple of ten
    if result % 10 == 0:
        return sum(arr)
    else:
        return 0


def solution(matrix):
    # 행...
    for i in range(len(matrix)):
        #   3. Calculate start index and end index.
        start_index = 0
        end_index = find_1(matrix[i])

        if end_index is None:
            continue
        else:
            start_index = int(end_index) - 56 + 1

        return find_code(matrix[i], start_index, int(end_index) + 1)


if __name__ == '__main__':
    case_len = int(input().strip())

    for i in range(case_len):
        a = []
        row, col = map(int, input().strip().split())

        # 1. Array Setting
        for row_idx in range(row):
            input_data = list(input().strip())
            a.append(input_data)

        print("#" + str(i + 1) + " " + str(solution(a)))
