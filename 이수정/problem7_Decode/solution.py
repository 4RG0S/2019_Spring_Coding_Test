def check_code(code):
    if code == '0001101':
        return 0
    elif code == '0011001':
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


if __name__ == '__main__':
    N = int(input().strip())+1
    
    for test_case in range(1, N):
        tmp = input().stript()
        x = tmp.split(' ')[0]
        y = tmp.split(' ')[1]

        for n in range(int(x)):
            stream = list(input().strip())
            code = []
            i = int(y) - 1

            while i >= 55:
                if stream[i] == '1':
                    break
                i = i-1

            if i < 55:
                continue

            start = i-55

            while start <= i:
                code.append("".join(stream[start:start+7]))
                start = start+7

            flag = 0
            for j in range(8):
                code[j] = check_code(code[j])
                if code[j] == -1:
                    flag = 1
                    break

            if flag == 1:
                print("#" + str(test_case) + " 0")
                break

            decode = (code[0] + code[2] + code[4] + code[6])*3 + code[1] + code[3] + code[5] + code[7]

            if decode % 10 == 0:
                print("#"+str(test_case)+" "+str((code[0]+code[1]+code[2]+code[3]+code[4]+code[5]+code[6]+code[7])))
                while n < int(x)-1:
                    input().strip()
                    n = n+1
                break
            else:
                print("#"+str(test_case)+" 0")
                while n < int(x) - 1:
                    input().strip()
                    n = n + 1
                break
