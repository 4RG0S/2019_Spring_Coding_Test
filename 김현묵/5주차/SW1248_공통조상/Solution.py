# 각 index의 번호가 노드번호가 되는 listStore 두개를 선언합니다.
# 내용물은 자식의 번호를 뜻합니다.[이중트리이므로 리스트는 2개 생성한것]
listStore = []
listStore2 = []

# 공통조상을 루트로 하는 서브트리의 사이즈를 뜻하는 sizeit 입니다.
sizeIt = 1

# 공통조상을 찾을 두개의 특정 노드를 인자로 넣어주는 함수입니다.
def findParent(start1, start2):

    # 각 start 점별로 자신의 조상을 거슬러 올라가 모든 조상을 리스트로 저장하는 리스트를 선언합니다.
    findParentList1 = []
    findParentList2 = []

    findParentOfStart1 = start1
    findParentOfStart2 = start2


    # 아래 while문의 코드는 각 점별로 리스트 내에서의 인덱스 위치를 찾는 과정을 반복시킵니다.

    # start1 의 모든 조상을 찾는 코드입니다.
    while 1 not in findParentList1:
        if findParentOfStart1 in listStore:
            indexOfParent = listStore.index(findParentOfStart1)
            findParentList1.append(indexOfParent)
            findParentOfStart1 = indexOfParent
        if findParentOfStart1 in listStore2:
            indexOfParent = listStore2.index(findParentOfStart1)
            findParentList1.append(indexOfParent)
            findParentOfStart1 = indexOfParent

    # start2 의 모든 조상을 찾는 코드입니다.
    while 1 not in findParentList2:
        if findParentOfStart2 in listStore:
            indexOfParent2 = listStore.index(findParentOfStart2)
            findParentList2.append(indexOfParent2)
            findParentOfStart2 = indexOfParent2
        if findParentOfStart2 in listStore2:
            indexOfParent2 = listStore2.index(findParentOfStart2)
            findParentList2.append(indexOfParent2)
            findParentOfStart2 = indexOfParent2


    # 각 점별로 조상을 찾은 리스트에서 앞에서 부터 비교하며 공통되는 최초의 점을 찾습니다.
    # 그 점이 두 점으로부터 가장 가까운 공통조상입니다.
    breakpoint = 0
    for i in findParentList1:
        for j in findParentList2:
            if i == j:
                sameParent = i
                breakpoint = 1
                break
        if breakpoint == 1:
            break

    # 공통조상을 리턴해줍니다.
    return sameParent



# 공통조상을 루트로 하는 서브트리의 사이즈를 구하기 위한 함수입니다.
def findSize(parent):

    global sizeIt

    # 공통조상을 시작으로 listStore와 listStore2 를 자식으로 쭉 내려갑니다.
    # 각 자식을 통과할 때마다 사이즈를 1씩 증가시킵니다.
    # 더 이상 자식이 없을 때까지 진행합니다.
    if listStore[parent] != 0:
        sizeIt = sizeIt + 1
        findSize(listStore[parent])
    if listStore2[parent] != 0:
        sizeIt = sizeIt + 1
        findSize(listStore2[parent])



# 테스트케이스의 수를 입력으로 받습니다.
listNum = input().strip()
listNum = int(listNum)

# 입력받은 개수만큼의 테스트 케이스를 돌립니다
for i in range(listNum):

    sizeIt = 1

    # 정점의 수, 간선의 수, 공통조상을 찾을 점1과 점2 를 입력으로 받습니다.
    form = input().strip().split()
    form = list(map(int, form))

    vertex = form[0]
    edge = form[1]
    start1 = form[2]
    start2 = form[3]

    listStore.clear()
    listStore2.clear()

    for w in range(vertex+1):
        listStore.append(0)
        listStore2.append(0)

    edgeList = input().strip().split()
    edgeList = list(map(int, edgeList))

    # listStore와 listStore2 에 각 노드가 가지는 자식의 숫자를 넣어줍니다.
    # 이중트리이므로 리스트는 두개를 씁니다.
    for j in range(0,edge*2,2):
        if listStore[edgeList[j]] == 0:
            listStore[edgeList[j]] = edgeList[j+1]
        else:
            listStore2[edgeList[j]] = edgeList[j+1]

    # 공통조상을 찾기위한 점1, 점2를 인자로 넣어주는 findParent 함수를 호출합니다.
    findIt = findParent(start1, start2)

    # 공통조상을 루트로 하는 서브트리의 사이즈를 구하는 함수를 호출합니다.
    findSize(findIt)



    # 각 테스트 별로 출력을 해줍니다.
    print('#{0} {1} {2}'.format(i+1, findIt, sizeIt))