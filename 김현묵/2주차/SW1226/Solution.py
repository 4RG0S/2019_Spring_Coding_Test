# 미로의 구조를 담아 둘 Matrix 2차원 배열을 선언해 줍시다.
Matrix = [[0] * 16 for t in range(16)]

# 재귀를 돌릴 함수입니다.
def recursion(i, j):
    l = 0
    u = 0
    r = 0
    d = 0

    # 이미 자기 자신은 검사를 한 것이므로 다시 돌 필요가 없습니다. '1'로 만들어 줍시다.
    Matrix[i][j] = 1

    # 도착지를 찾습니다. 찾으면 1로 리턴을 시킵니다.
    if Matrix[i][j] == 3 or Matrix[i - 1][j] == 3 or Matrix[i][j - 1] == 3 or Matrix[i][j + 1] == 3 or Matrix[i+1][j] == 3:
        return 1

    # 위, 아래, 오른쪽, 왼쪽 길이 있으면 찾아줍시다.
    if Matrix[i + 1][j] == 0:
        r = recursion(i + 1, j)
    if Matrix[i][j + 1] == 0:
        d = recursion(i, j + 1)
    if Matrix[i - 1][j] == 0:
        l = recursion(i - 1, j)
    if Matrix[i][j - 1] == 0:
        u = recursion(i, j - 1)
    if ( r== 1 or d ==1 or l ==1 or u ==1 ):
        return 1
    else:
        return 0



for i in range(10):
    caseNum = (input().strip())
    for z in range(16):
        oneline = input().strip()
        # onelineRev = list(map(int, oneline))
        for j in range(16):
            if (int)(oneline[j]) == 2:
                starting = z
                finishing = j
            Matrix[z][j] = (int)(oneline[j])

    # 출발점으로부터 시작해 재귀를 돌려 1을 리턴할 수 있는지 확인해봅시다.
    finish = recursion(starting,finishing)

    # 각 테스트 별로 출력을 해줍니다.
    print('#{0} {1}'.format(i+1, finish))







