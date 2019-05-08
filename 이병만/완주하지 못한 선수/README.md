[Programmers](<https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3>). 

Problem : 완주하지 못한 선수 **해시**

Flow :

1. completion의 길이는 participant의 길이보다 1 작습니다.
2. 참가자 중에는 동명이인이 있을 수 있다.



Solution :

1. 각 배열을 정렬한다.
2. 반복문을 돌면서 각 배열의 같은 인덱스에 있는 값을 비교한다
3. 다르면 answer를 저장하고 flag를 True로 해주고 반환해준다.
4. 만약 flag가 False이면 마지막의 값을 저장하고 반환해준다.
