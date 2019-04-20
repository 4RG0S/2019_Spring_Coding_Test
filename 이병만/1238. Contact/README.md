[SW Expert Academy 1238](<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15B1cKAKwCFAYD&>). 

Problem : Contact **D4**

Flow :

1. 연락 인원 : 최대 100명, 부여될 수 있는 번호 1 ~ 100.
2. 단, 중간에 비어있는 번호가 있을 수 있음.
3. 연락이 퍼지는 속도는 항상 일정.
4. 같이 연락을 받을 수 없는 사람도 존재 가능.



Solution :

1. 배열 세팅
2. BFS를 이용하여 문제를 해결하려고 했다.
3. 큐로 사용하기 위해 deque를 선언, 방문한 노드를 체크하기 위한 배열을 선언한다.
4. 노드의 번호와 Depth를 같이 Queue에 넣어주었다.
5. 인접한 노드를 찾는다. 
6. 방문하지 않은 노드이면 큐와 방문 체크 배열에 값을 넣는다.
7. depth를 기준으로 오름차순으로 정렬한다.
8. 배열의 맨 뒤에 있는 값을 반환한다.