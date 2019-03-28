def solution():
    f = open('input1.txt', 'r')
    g = open('output1.txt', 'w')
    j = 1
    while True:
        index = f.readline()
        line = f.readline()
        if not index or not line:
            break
        array = []
        for i in range(int(index)):
            array.append(int(line.split(' ')[i]))
        print(array)
        count = 0
        for i in range(len(array)):
            if i-2 >= 0 and i+2 <= len(array): #i가 범위내에있음
                if array[i] > array[i-1] and array[i] > array[i-2] and array[i] > array[i+1] and array[i] > array[i+2]:
                    count += array[i] - max(array[i-1], array[i - 2], array[i + 1], array[i + 2])
        print(count)

        g.write('#' + str(j) + ' ' + str(count) + '\n')
        j += 1
    g.close()
    f.close()


if __name__ == "__main__":
    solution()
