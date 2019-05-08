[SW Expert Academy 1248](<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD&categoryId=AV15PTkqAPYCFAYD&categoryType=CODE>). 

Problem : 공통조상 **D5**

임의의 이진 트리가 주어지고, 두 정점이 명시될 때 이들의 공통 조상 중 이들에  가장 가까운 정점을 찾고, 그 정점을 루트로 하는 서브 트리의 크기를 알아내는 프로그램 작성

Flow :

1. 두 정점이 서로 조상과 자손 관계인 경우는 없다.
2. 각 케이스의 첫줄에는 트리의 정점의 총 수 V와 간선의 총 수 E, 공통 조상을 찾는 두 개의 정점 번호가 주어짐 (정점의 수 V는 10 <= V <= 10000)



Solution :

1. 두 정점에 대해서 거꾸로 루트까지 경로를 구함
2. 두 경로를 비교하여 가장 가까운 정점을 구함



1. 모든 정점의 부모를 저장
2. 주어진 두 정점에 대해서 거꾸로 루트까지 경로 탐색
3. 구해진 두 경로의 루트부터 다를 때까지 타고 내려간다.
4. 다르면 마지막에 방문한 정점을 반환