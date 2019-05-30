[Programmers](https://programmers.co.kr/learn/courses/30/lessons/42626). 

Problem : 더 맵게 **힙(Heap)**

Flow :

1. 섞은 음식의 스코빌 지수 = 가장 맵지 않은 음식의 스코빌 지수 + (두 번째로 맵지 않은 음식의 스코빌 지수 * 2)
2. 주어질 때, 모든 음식의 스코빌 지수를 K 이상으로 만들기 위해 섞어야 하는 최소 횟수를 return 하도록 solution 함수를 작성해주세요.



Solution :

1. 각 배열을 정렬한다.
2. 힙을 사용하기 위해 import heapq를 한다.
3. 최소힙이기 때문에 루트 두 개의 값을 뽑아서 소크빌 지수를 계산한다.
4. 다시 힙에 넣어준다.
5. answer의 값을 1 더해준다.
6. 입력받은 스코빌 지수를 넘기면 answer의 값을 반환한다.
