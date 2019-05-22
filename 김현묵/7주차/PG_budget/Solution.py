# 프로그래머스 예산 문제
# 문제링크 : https://programmers.co.kr/learn/courses/30/lessons/43237

# 정확성 : 30
# 효율성 : 10


def solution(budgets, M):

    plusNum = 0

    # 주어진 budgets 리스트 안의 숫자들의 총합을 구합니다.
    for i in budgets:
        plusNum = plusNum + i

    # 각 지방들이 요구하는 예산의 총합을 현재 배정될 수 있는 예산의 총액과 비교합니다.
    # 만약 예산의 총합보다 작다면 요구하는 예산 중 가장 큰 값이 answer가 됩니다.
    if plusNum <= M:
        answer = budgets(max)

    # 각 지방들이 요구하는 예산의 총합이 현재 배정될 수 있는 예산의 총액보다 큰 경우 입니다.
    else:
        # 각 지방들의 수로 배정될 수 있는 예산 총합을 나눕니다.
        budgets.sort(reverse=True)
        budgetNum = len(budgets)
        divideNum = int(M / budgetNum)

        # 나눈 후에 수를 비교해서 지방들의 요구하는 예산 중 n등분 한 값보다 작다면
        # 그 값은 배정될 수 있는 예산의 총액에서 빼주고, 그 요구하는 예산은 리스트에서 빼줍니다.
        for num in budgets[::-1]:
            if num < divideNum:
                M = M - num
                budgets.pop()
            else:
                break

    # n등분 한 배정될 수 있는 총액보다 작은 요구하는 예산이 없을 경우입니다.
    # 이럴 때는 n등분 한 배정될 수 있는 예산보다 어느 요구하는 예산도 크지 않은 경우입니다.
    # 그럴 때는 모두 각 지방들이 요구하는 예산이 자신의 n등분 한 경우보다 큰 경우이기 때문에,
    # 현재 n등분한 기준값을 answer로 만들면 됩니다.
    if budgetNum == len(budgets):
        answer = divideNum

    # n등분한 배정될 수 있는 예산보다 작은 지방이 요구하는 예산이 있는 경우입니다.
    # 이런 경우는 이 과정을 다시 반복시킵니다.
    # 배정될 수 있는 예산은 값이 줄었고 각 지방들이 요구하는 예산의 수도 줄은 상태로 다시 함수를 돌려 answer를 얻어냅니다.
    # 배정될 수 있는 예산보다 지방들이 요구하는 예산의 총합이 큰 경우,
    # 배정될 수 있는 예산을 n등분한 값과 각 지방들이 요구하는 예산을 비교했을 때 각 지방들이 요구하는 예산이 큰 경우가 있을 때까지 이 함수는 진행됩니다.
    else:
        answer = solution(budgets, M)


    # answer를 return 합니다
    return answer