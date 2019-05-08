[SW Expert Academy 1218](<https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV14eWb6AAkCFAYD&>). 

Problem : 괄호 짝짓기 **D4**

Flow :

1. 4 종류의 괄호문자들 '()', '[]', '{}', '<>' 로 이루어진 문자열이 주어짐.
2. 이 문자열에 사용된 괄호들의 짝이 모두 맞는지 판별하는 프로그램 작성

<br>

Solution :

스택을 사용해서 여는 괄호에 해당하는 숫자를 스택에 넣어주고 닫는 괄호가 만나면 스택에서 꺼내서 같으면 1 다르면 0을 반환

1. 데이터를 읽고 리스트를 solution함수에 넘겨준다.
2. stack을 사용하기 위한 list, 비교를 위한 변수 선언.
3. 여는 괄호('{', '[', '(', '< ')를 만나면 각 괄호에 해당하는 숫자(0, 1, 2, 3)을 스택에 넣어준다.
4. 만약 닫는 괄호를 만나면 compare 변수에 각 괄호에 해당하는 숫자(0, 1, 2, 3)을 저장한다.
5. compare 변수와 스택에서 pop한 값을 비교한다.
6. 같으면 result의 값을 1
7. 하나라도 다르면 유효하지 않는 것이기 때문에 0을 바로 반환한다.