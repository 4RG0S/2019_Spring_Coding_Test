# 숫자나 연산자를 저장하는 listStore
listStore = []

# 연산자와 숫자가 적절한 위치에 있는지 판단하는 함수
# 말단노드에는 숫자가 그 외에는 연산자가 들어가야 합니다!
def treeOper(size):

    halfsize = int(size/2)

    # 시작점부터 halfsize 까지는 연산자가 위치해야 한다. 아니라면 0 리턴
    for i in range(halfsize):
        if (listStore[i]).isdigit() == True:
            listStore.clear()
            return 0

    # halfsize 부터 마지막 까지는 숫자가 위치해야 한다. 아니라면 0 리턴
    for j in range(halfsize, size):
        if (listStore[j]).isdigit() == False:
            listStore.clear()
            return 0

    # 다 조건을 만족한다면 1을 리턴한다.
    listStore.clear()
    return 1


# 10번의 테스트 케이스를 돌립니다
for i in range(10):

    # 입력 양식입니다
    listNum = input().strip()
    listNum = int(listNum)


    # 숫자나 연산자르 리스트에 집어넣습니다.
    for j in range(listNum):
        storeNumorOper = input().strip().split()
        listStore.append(storeNumorOper[1])

    finish = treeOper(listNum)


    # 각 테스트 별로 출력을 해줍니다.
    print('#{0} {1}'.format(i+1, finish))



