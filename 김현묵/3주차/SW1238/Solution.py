import queue

# queue 를 이용해 선입선출로 Graph 탐색을 시행한다
queueUse= queue.Queue()
# 이미 Graph 에서 탐색을 했는지 여부를 저장하는 세트
already = set()
# key, value 로 현재 상태에서 갈 수 있는 상태가 매칭되어있는 딕셔너리
dictionary = {}
# 현재 단계에서 답이 될 수 있는 상태값들이 들어있는 리스트
solutionList = []


# 수행하게 될 함수입니다.
def queueing( i ):

    # 함수의 argument 로 들어온 인자 i 개수만큼 queue에서 값을 빼내어 읽습니다.
    # 이것은 현재 상태에 있는 상태값들을 다 빼내고 다음 상태로 넘어가게 할 수 있게 합니다.
    for w in range(i):
        variable = queueUse.get()
        # 일단 현재 queue에서 뽑아낸 상태값은 현재 이 상태가 마지막일 수도 있으니 답 후보군에 넣어둡니다.
        solutionList.append(variable)

        # variable 이 dictionary의 key가 될 텐데, 만약 value가 없으면 더 할 게 없습니다.
        # variable 이 dictionary에서 value를 가질 때 수행하는 과정입니다.
        if variable in dictionary:

            # dictionary 의 key 로 variable을 넣었을 때 나오는 dicValue 는 set 형식입니다.
            dicValue = dictionary[variable]

            # set의 값의 개수만큼 돌리는 for문입니다.
            for j in range(len(dicValue)):
                dicValueOne = dicValue.pop()

                # 아래 과정은 이미 value set 의 한 값이 이미 탐색이 된 곳이면 다시 탐색을 안 시키기 위해 조사하는 과정입니다.
                alreadyLen = len(already)
                already.add(dicValueOne)
                alreadyLen2 = len(already)

                # 아직 탐색을 안했다면 queue 에 집어넣어 줍니다.
                if alreadyLen != alreadyLen2:
                    queueUse.put(dicValueOne)

    # 현재 queue 에 들어가 있는 값이 없다면 마지막 탐색이었을 테고, 아니라면 다시 solutionList 를 초기화하고 queueing 함수를 현재 queue 의 사이즈만큼 돌립니다.
    soonPop = queueUse.qsize()
    if soonPop != 0:
        solutionList.clear()
        queueing(soonPop)



# 10번의 테스트 케이스를 돌립니다
for i in range(10):

    # 각 케이스마다 리스트, 딕셔너리 등을 초기화 시키고 시작합니다
    solutionList.clear()
    dictionary.clear()
    already.clear()

    # 입력 양식입니다
    precondition = (input().strip().split())
    precondition = list(map(int,precondition))
    caseNum = precondition[0]
    startingDot = int(precondition[1])

    graph =  input().strip().split()
    graph = list(map(int, graph))

    # 그래프 생성 과정입니다.
    for z in range(0, int(caseNum), 2):
        key = graph[z]
        value = graph[z+1]
        value = set([value])

        # key, value 로 현재 상태에서 갈 수 있는 상태들을 저장합니다.
        # 1개의 상태에서 여러개의 상태로 갈 수 있으며, 중복체크도 해야하므로 value 형식으로는 세트를 씁니다,
        if key in dictionary:
            dictionary[key] = dictionary[key] | value
        else:
            dictionary[key] = value


    # 시작점을 queue 에 넣고 시작합니다.
    queueUse.put(startingDot)
    # 시작점은 이미 상태를 돌았다는 표시로 already set에 넣어줍니다.
    already.add(startingDot)

    firstSet = dictionary[startingDot]

    if len(firstSet) != 0:
        # queueing 함수는 현재 queue 에 들어가 있는 상태 개수로 시행합니다. 그래야 단계별로 진행시킬 수 있습니다.
        queueing(1)
        # queueing 함수를 모두 돌고 난 후, solutionList 에 들어가 있는 상태값들을 내림차순으로 정렬합니다.
        solutionList.sort(reverse=True);
        # 내림차순으로 정렬된 solutionList 에서 맨 첫번째 값을 빼내면 그것이 답이 됩니다.
        finish = solutionList[0]

    # 시작점에서 갈 수 있는 상태가 없으면 그냥 시작점이 결과입니다
    else:
        finish = startingDot


    # 각 테스트 별로 출력을 해줍니다.
    print('#{0} {1}'.format(i+1, finish))






