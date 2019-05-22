# 프로그래머스 타겟넘버
# 문제링크 : https://programmers.co.kr/learn/courses/30/lessons/43165

# 정확성 : 100

# 이 문제는 주어진 리스트의 숫자들를 적절히 더하거나 빼서 타겟넘버를 만드는 문제입니다.
# 더하고 빼는 과정이 복잡해서 리스트의 모든 수를 더하고 그 값에서 타겟넘버만큼 도달하기 위해
# 주어진 숫자들을 2씩 곱해서 빼보면서 살펴보았습니다.
# 리스트를 내림차순으로 정렬하여 큰 수부터 빼보며 비교하는 것이 편하여 내림차순으로 정렬하였습니다.


# answer는 주어진 리스트로 더하거나 빼서 타겟넘버를 만들 수 있는 경우의 수입니다.
answer = 0


def looping(starting, standardNum, numbers):

    global answer

    # 리스트의 starting 요소부터 for문을 돌립니다.
    for forNum in range(starting, len(numbers)):
        # standardNum에서 forNum에 위치한 리스트의 요소에 2를 곱해서 뺐을 때 0보다 작다면,
        if (standardNum - (2 * numbers[forNum])) < 0:
            # continue로 다음 리스트의 요소로 넘깁니다.
            continue
        # standardNum에서 forNum에 위치한 리스트의 요소에 2를 곱해서 뺐을 때 0이 나왔다면, target 숫자를 만든 경우입니다.
        elif (standardNum - (2 * numbers[forNum])) == 0:
            # 경우를 1가지 늘려줍니다.
            answer = answer + 1
        # standardNum에서 forNum에 위치한 리스트의 요소에 2를 곱해서 뺐을 때 0보다 크다면,
        # 이것은 다음 요소를 확인해야 합니다.
        else:
            # standardNum에서 forNum에 위치한 리스트의 요소에 2를 곱한 값을 newStandardNum으로 지정합니다.
            newStandardNum = standardNum - (2 * numbers[forNum])
            # forNum+1 를 새로운 리스트의 시작점으로 주고, newStandardNum을 기준으로 줍니다.
            looping(forNum+1,newStandardNum, numbers)


def solution(numbers, target):

    sumOfNumbers = 0
    # 리스트에 있는 숫자들을 내림차순으로 정렬합니다.
    numbers.sort(reverse=True)

    # 리스트의 모든 숫자들의 합을 구합니다.
    for num in numbers:
        sumOfNumbers = sumOfNumbers + num

    # 모든 숫자들의 합에서 타겟넘버를 뺀 결과를 standardNum이라고 지정합니다.
    standardNum = sumOfNumbers - target

    # 루프함수를 돌려줍니다.
    looping(0, standardNum, numbers)

    # 결과를 리턴합니다.
    return answer