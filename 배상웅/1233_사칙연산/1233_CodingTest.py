f = open("input.txt", "r")

while True:
    total = f.readline()
    total = total.replace("\n", '')
    count = 0
    temp = 0
    result_flag = False

    if not total:
        break

    print("total", total)
    # 연산이 안되는 부분 찾기
    # 자식이 있는 부모 노드들 중에서 부모노드가 total 값이랑 같아지면
    # 이미 연산 부호는 다 나왔기 때문에, 연산 부분이 숫자면 안된다.
    while count <= int(total):
        count += 1
        line = f.readline()
        line = line.replace('\n', '')
        line = line.split(' ')
        # 만약 부모가 total값이랑 같은 번호에 있을 때, 더 찾아볼 필요없으므로 break
        if int(line[len(line)-1]) == int(total):
            temp = int(line[0])
            break
        # 위에 break 이전 부분을 탐색한다. 만약 연산부호 있는 부분이 숫자면 break
        elif int(line[len(line)-1]) < int(total):
            if line[1] != '-' and line[1] != '+' and line[1] != '/' and line[1] != '*':
                result_flag = True
                temp = int(line[0])
                break
    # 나머지 부분을 읽어준다.
    for i in range(0, int(total)-temp):
        line = f.readline()
    # 연산이 가능하면 1, 불가능하면 0
    if result_flag == True:
        print(0)
    else:
        print(1)
