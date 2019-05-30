import heapq


def solution(scoville, K):
    answer = 0

    scoville.sort()

    while scoville[0] < K:
        if len(scoville) == 1:
            answer = -1
            break

        first = heapq.heappop(scoville)
        second = heapq.heappop(scoville)
        new = first + (second * 2)
        heapq.heappush(scoville, new)
        answer += 1

    return answer
