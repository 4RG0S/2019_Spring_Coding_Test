import sys
sys.setrecursionlimit(10000)
temp = 0
temp1 = 0


def recursive_find(ii):
    global temp1
    for i1 in range(0, len(d)):
        if c[i1] == ii and flag[i1] == False:
            temp1 = d[i1]
            flag[i1] = True
            if temp1 == 99:
                print("done")
                return exit
            recursive_find(temp1)


f = open("input.txt", 'r')


while True:

    flag = []
    c = []
    d = []
    temp = temp+1

    counting = 0
    line = f.readline()

    if not line:
        break
    print(temp)
    a = line.split(' ')
    length = int(a[1])*2
    half = int(length/2)
    line = f.readline()
    b = line.split(' ')
    b[length-1] = b[length-1][:-1]  # 마지막에 \n제거

    for i in range(0, half):
        c.append(int(b[2*i]))
        d.append(int(b[2*i+1]))
        flag.append(False)

    print(c)
    print(d)

    for i in range(0, 2):
        recursive_find(d[i])


