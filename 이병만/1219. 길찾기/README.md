[SW Expert Academy 1219](<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14geLqABQCFAYD>). 

Problem : 길찾기 **D4**

Flow :

1. A와 B는 숫자 0과 99으로 고정.
2. 모든 길은 순서쌍으로 나타남. (2, 5) (2, 9)
3. 가는 길의 개수와 상관없이 한가지 길이라도 존재하면 길이 존재하는 것.
4. 단, 화살표 방향을 거슬러 돌아갈 수는 없다.



Solution :

1. path를 나타낼 두 개의 배열 세팅
2. 만약 값이 99이면 도착지이므로 1을 반환한다.
3. 100이 아니면 길이 있다는 것이므로 마킹을 하고 다음 방향으로 이동한다.
4. sol_one, sol_two는 길의 존재 유무를 판단하는 변수이다.
5. 이 두 변수 중 하나가 1이면 1을 반환하고 아니면 0을 반환한다.