[Programmers](https://programmers.co.kr/learn/courses/30/lessons/42577). 

Problem : 전화번호 목록 **해시**

Flow :

1. 전화번호부에 적힌 전화번호 중, 한 번호가 다른 번호의 접두어인 경우가 있는지 확인하려 합니다.
2. 전화번호가 다음과 같을 경우, 구조대 전화번호는 영석이의 전화번호의 접두사입니다.



Solution :

1. 각 배열을 정렬한다.
2. 0번째 인덱스에 있는 값을 search로 저장한다.
3. 해당 배열을 반복문을 돌면서 0번째 인덱스와 같으면 배제시킨다.
4. search의 길이만큼 match의 0부터 검사해서, 같은게 있으면 False를 저장한다.
5. 반복문 종료
