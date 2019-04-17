# -*- coding: utf-8 -*-
import queue

# queue.LifoQueue() 는 stack 입니다.
stack= queue.LifoQueue()


# 수행하게 될 함수입니다.
def stacking( barrierCom ):

    # stack을 초기화 시켜줍니다.
    stack.__init__()

    # 들어오는 괄호들의 갯수를 의미합니다.
    barrierSize = len(barrierCom)

    # 각 괄호들의 케이스를 나눠서 써줍니다.
    # 왼쪽괄호일 시 stack 에 넣어주고
    #  오른쪽 괄호일시 stack에 마지막에 넣어준 요소가 자신의 왼쪽 짝 괄호인지 확인합니다
    for j in range(barrierSize):
        if barrierCom[j] == '{':
            stack.put('{')
        elif barrierCom[j] == '[':
            stack.put('[')
        elif barrierCom[j] == '<':
            stack.put('<')
        elif barrierCom[j] == '(':
            stack.put('(')
        elif (stack.qsize() != 0) & (barrierCom[j] == '}'):
            compare = stack.get()
            if compare == '{':
                continue
            else:
                return 0
        elif (stack.qsize() != 0) & (barrierCom[j] == ']'):
            compare = stack.get()
            if compare == '[':
                continue
            else:
                return 0
        elif (stack.qsize() != 0) & (barrierCom[j] == '>'):
            compare = stack.get()
            if compare == '<':
                continue
            else:
                return 0
        elif (stack.qsize() != 0) & (barrierCom[j] == ')'):
            compare = stack.get()
            if compare == '(':
                continue
            else:
                return 0
        else:
            return 0

    # for문을 다 돌고, stack이 비었으면 조건을 통과한 것이므로 1을 리턴해줍시다
    if stack.qsize() == 0:
        return 1




# 10번의 테스트 케이스를 돌립니다
for i in range(10):

    # 입력 양식입니다
    listNum = input().strip()
    listNum = int(listNum)
    barrier = input().strip()

    finish = stacking(barrier)


    # 각 테스트 별로 출력을 해줍니다.
    print('#{0} {1}'.format(i+1, finish))



