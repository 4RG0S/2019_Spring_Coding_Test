# 프로그래머스 '더 맵게' 문제
# 문제링크 : https://programmers.co.kr/learn/courses/30/lessons/42626


# 정확성 : 76.2
# 효율성 : 23.8

# 이 문제는 heap 자료구조를 사용해서 최소값에 주목해야 합니다.
# category가 heap 이라서 알아냈지, 그것이 아니었다면 틀렸을 겁니다.
import heapq

# scoville의 모든 요소가 K 이상이 되어야 합니다.[최소값이 K 이상이면 된다.]
# 그렇지 않다면, 연산 : [최소값 + ( 2 * 최소에서 2번째 값 )] 을 계산해서 다시 리스트에 넣어 비교합니다.
def solution(scoville, K):

    # answer는 최소값이 K 이상이 되게 하기 위해 필요한 연산의 수를 뜻합니다.
    answer = 0

    # scoville 를 오름차순으로 정렬합니다.
    scoville.sort()
    # heapq.heapify(scoville)

    # 리스트의 최소값이 K 이상인지 확인하고, 그렇지 않다면 연산을 하고 연산한 값을 다시 리스트에 넣어줍니다.
    # 최소값이 K 이상이 될 때까지 반복합니다.
    # 이 때, 리스트는 항상 최소 heap의 구조를 유지해야 합니다.
    while True:
        if scoville[0] < K:

            # 리스트의 최소값이 K보다 작을 때 요소가 1개 뿐이면 이것은 최소값이 K 보다 커질 수 없는 경우입니다.
            # 이럴 때는 answer를 -1로 만들어 주고 while문을 빠져나가 줍시다.
            if len(scoville) == 1:
                answer = -1
                break

            # 연산의 수가 1번 더 추가됩니다.
            answer = answer + 1
            # 최소값과 그 다음 최소값을 리스트에서 빼내어 연산 후에 새로운 값을 넣어줍니다.
            firstElement = heapq.heappop(scoville)
            secondElement = heapq.heappop(scoville)
            newElement = firstElement + ( 2 * secondElement)
            heapq.heappush(scoville, newElement)

        # 최소값이 K 보다 크다면 while문을 빠져나가 줍시다.
        else:
            break

    # 연산의 수를 return 해줍니다.
    return answer