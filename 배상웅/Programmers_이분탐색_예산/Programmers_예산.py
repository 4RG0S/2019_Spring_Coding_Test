// runtime 오류 해결 못함...
def caculate(templist, mid):
    for i in range(0, len(templist)):
        if templist[i] > mid:
            templist[i] = mid
    return sum(templist)


def solution(budgets, M):
    answer = 0
    result = []
    result1 = []
    i = 0
    total_average = int(sum(budgets) / len(budgets))
    M_average = int(M / len(budgets))
    mid = total_average - int((total_average - M_average) / 2)

    while i < total_average - M_average:
        templist = list(budgets)
        temp = caculate(templist, mid)
        result.append(temp)
        result1.append(mid)
        if temp == M:
            answer = mid
            break
        elif temp > M:
            mid = int(mid - ((mid - M_average) / 2))
        elif temp < M:
            mid = int(total_average - ((total_average - mid) / 2))
        i = i + 1
    print(result)
    result_answer = []
    for i in range(0, len(result)):
        if M - result[i] > 0:
            result_answer.append(result1[i])

    answer = max(result_answer)
    1

    return answer