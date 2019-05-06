[SW Expert Academy 1233](<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV141176AIwCFAYD&categoryId=AV141176AIwCFAYD&categoryType=CODE>). 

Problem : 사칙연산 유효성 검사 **D4**

Flow :

1. 총 노드의 개수는 200개를 넘지 않음.
2. 트리는 완전 이진 트리 형식으로 주어짐.
3. 노드당 하나의 연산자 또는 숫자만 저장할 수 있음.



Solution :

1. 전체 노드수를 2로 나눈 뒤 리프노드와 리프노드가 아닌 것으로 값을 설정
2. 리프 노드를 제외하고 숫자가 있으면 안되기 때문에 check함수로 확인
3. 리프 노드에 숫자 이외에 연산자가 있어도 안되기 때문에 확인