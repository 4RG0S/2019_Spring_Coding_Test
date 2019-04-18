def solution():
    f = open('binary_password_input.txt', 'r')
    question_length = f.readline()

    question_number = 1
    while True:
        index = f.readline()
        if not index:
            break
        row = int((index.split(' ')[0]))
        column = int((index.split(' ')[1]))

        find = ''

        for i in range(row):
            data = f.readline()
            for j in range(len(data)-1, 0, -1):
                if data[j] == '1':
                    for k in range(j, j-56, -1):
                        find = data[k] + find
                    break

        test = []
        for o in range(56):
            test.append(find[o])
        #print(test)

        answer = []

        for a in range(len(test)):
            if a % 7 == 0:
                answer.append(test[a:a+7])
        #print(answer)

        final = ''
        for b in range(len(answer)):
            binary_data = ''.join(answer[b])
            # print(binary_data)
            if binary_data == '0001101':
                final += '0'
            elif binary_data == '0011001':
                final += '1'
            elif binary_data == '0010011':
                final += '2'
            elif binary_data == '0111101':
                final += '3'
            elif binary_data == '0100011':
                final += '4'
            elif binary_data == '0110001':
                final += '5'
            elif binary_data == '0101111':
                final += '6'
            elif binary_data == '0111011':
                final += '7'
            elif binary_data == '0110111':
                final += '8'
            elif binary_data == '0001011':
                final += '9'
            else:
                final = 'undefined'
        #print(final)
        final_answer = 0
        if ((int(final[0]) + int(final[2]) + int(final[4]) + int(final[6])) * 3 + int(final[1]) + int(final[3]) + int(final[5]) + int(final[7])) % 10 == 0:
            for i in range(len(final)):
                final_answer += int(final[i])
            print('#' + str(question_number), final_answer)
        else:
            print('#' + str(question_number), 0)
        question_number += 1


    f.close()


if __name__ == "__main__":
    solution()
