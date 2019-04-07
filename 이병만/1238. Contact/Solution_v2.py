from collections import deque
import time


# BFS
def solution(arr, start):
    queue = deque()
    queue.append([start, 0])
    visited = [start]
    max_result = []

    while queue:
        n = queue.popleft()
        max_result.append(n)

        # find adjacent values
        for index in range(len(arr)):
            if arr[n[0]-1][index] != 0 and arr[n[0]-1][index] not in visited:
                # putin queue
                queue.append([arr[n[0]-1][index], n[1] + 1])
                visited.append(arr[n[0]-1][index])

    max_result.sort(key=lambda x: (x[1], x[0]))

    return max_result[-1][0]


if __name__ == '__main__':

    # Test case
    for i in range(10):
        # data length , start point
        data_len, start_point = map(int, input().strip().split())

        # contact data
        contact = list(map(int, input().strip().split()))

        start_time = time.time()

        # data setting
        data = [[0] * 100 for k in range(100)]
        for j in range(0, len(contact), 2):
            data[contact[j] - 1][contact[j+1] - 1] = contact[j+1]

        # print(solution(data, visited, start_point))
        print("#" + str(i + 1) + " " + str(solution(data, start_point)))

        print("start_time", start_time)  # 출력해보면, 시간형식이 사람이 읽기 힘든 일련번호형식입니다.
        print("--- %s seconds ---" % (time.time() - start_time))
