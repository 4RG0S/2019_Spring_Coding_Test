# 각 위치에서 경로를 담아둘 Matrix, Matrix2 배열 2개를 선언해줍시다.
Matrix= []
Matrix2 = []

# 각 배열을 초기화 시켜줍니다. 0[시작점] ~ 99[도착점]
# 100으로 초기화 시키는 건 갈 수 있는 경로가 없다는 뜻입니다!
for i in range(100):
    Matrix.append(100)
    Matrix2.append(100)



# 재귀를 돌릴 함수입니다.
def recursion( i ):

    one = 0
    two = 0


    # 도착지를 찾습니다. 찾으면 1로 리턴을 시킵니다.
    if (Matrix[i] == 99) or (Matrix2[i] == 99):
        return 1

    # 갈 수 있는 경로가 있다면 그 경로로 가서 찾아줍니다. 재귀를 이용합니다.
    if Matrix[i] != 100:
        des = Matrix[i]
        Matrix[i] = 100
        one = recursion(des)
    if Matrix2[i] != 100:
        des2 = Matrix2[i]
        Matrix2[i] = 100
        two = recursion(des2)

    # 목적지를 찾았다면 1을 리턴 받으므로 역시 이 함수도 1을 리턴해줍니다
    if ( one == 1 or two == 1):
        return 1
    else:
        return 0


for i in range(10):

    caseNum = (input().strip().split())
    caseNum = list(map(int,caseNum))
    couple = caseNum[1]

    oneline =  input().strip().split()
    oneline = list(map(int,oneline))

    # 매 테스트 케이스를 할 때마다 다시 100으로 모두 초기화 시켜줍니다.
    for t in range(100):
        Matrix[t] = 100
        Matrix2[t] = 100

    # 순서쌍을 이용하기 위해 2씩 증가시켜 Matrix에 경로를 저장해줍니다.
    for z in range(0, couple*2, 2):
        if Matrix[oneline[z]] == 100:
            Matrix[oneline[z]] = oneline[z+1]
        else:
            Matrix2[oneline[z]]= oneline[z+1]


    # 출발점으로부터 시작해 재귀를 돌려 1을 리턴할 수 있는지 확인해봅시다.
    finish = recursion(0)

    # 각 테스트 별로 출력을 해줍니다.
    print('#{0} {1}'.format(i+1, finish))






