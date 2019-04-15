f = open("input.txt", 'r')

testcase = f.readline()

# '0001101' = 0
# '0011001' : 1'
# '0010011' : 2'
# '0111101' : 3'
# '0100011' : 4'
# '0110001' : 5'
# '0101111' : 6'
# '0111011' : 7'
# '0110111' : 8'
# '0001011' : 9'

def solving_crypto(tempp):
    str1 = ""
    for i2 in range(0, len(tempp)):
        str1 += tempp[i2]
    if str1 == '0001101':
        result.append(0)
    elif str1 == '0011001':
        result.append(1)
    elif str1 == '0010011':
        result.append(2)
    elif str1 == '0111101':
        result.append(3)
    elif str1 == '0100011':
        result.append(4)
    elif str1 == '0110001':
        result.append(5)
    elif str1 == '0101111':
        result.append(6)
    elif str1 == '0111011':
        result.append(7)
    elif str1 == '0110111':
        result.append(8)
    elif str1 == '0001011':
        result.append(9)
    else:
        print("error")
    check_crypto(result)


# (홀수 자리의 합 x 3) + 짝수 자리의 합 + 검증 코드” 가 10의 배수가 되어야 한다.
def check_crypto(result):
    global no_check_code
    hol_sum = 0
    jak_sum = 0
    for i3 in range(0, len(result)-1, 2):
        hol_sum += result[i3]
        jak_sum += result[i3+1]
    no_check_code = hol_sum*3 + jak_sum



def solved_result(no_code):
    if no_code % 10 != 0:
        print("result is", 0)
    else:
        print("result is", sum(result, 0))



def divide_line(line):
    for i1 in range(0, len(line), 7):
        tempp = line[i1:i1+7]
        solving_crypto(tempp)


while True:
    line = f.readline()
    if not line:
        break
    line = line.split(' ')
    row = int(line[0])
    col = int(line[1])

    temp = 0
    line = f.readline()
    line = line.replace("\n", "")
    line = list(line)
    i = col
    count = 0
    while True:
        i -= 1
        if int(line[i]) == 1:
            temp = i
            break
        if i == len(line)-56:
            count += 1
            line = f.readline()
            line = line.replace("\n", "")
            line = list(line)
            i = col
    line = line[temp-55:temp+1]
    result = []
    no_check_code = -1
    divide_line(line)
    solved_result(no_check_code)

    for ii in range(0, row-count-1):
        line = f.readline()
