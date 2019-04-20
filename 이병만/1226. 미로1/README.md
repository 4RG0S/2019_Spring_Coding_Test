[SW Expert Academy 1226](<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14vXUqAGMCFAYD>). 

Problem : 미로1 **D4**

Flow :

1. 16 * 16 행렬의 형태로 만들어진 미로가 있다.
2. 주어진 미로의 출발점으로부터 도착지점까지 갈 수 있는 길이 있는지 판단하는 프로그램 작성



Solution :

1. 미로를 저장하는 배열 세팅
2. 미로의 출발 지점을 찾기 위해 첫번째 줄에서 '2'을 찾는다.
3. 왼쪽, 오른쪽, 위, 아래를 나타낼 변수 선언
4. 도착 지점인지 확인한다. (값이 3인 것을 찾는다.) 도착 지점이면 1을 반환한다. *** Termial condition ***
5. 현재 위치로부터 왼, 오른, 위, 아래를 본다. 
6. 0 이면 현재 위치를 1로 바꿔주고 재귀함수를 호출한다.
7. 각 방향의 값이 1이면 막힌 방향이므로 1을 반환한다.
8. 그렇지 않으면 0을 반환해서 계속 해당 방향으로 나아간다.