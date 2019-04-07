from collections import deque
import time


# BFS
def solution(arr, visit, start):
    queue = deque()
    queue.append([start, 0])
    visit[start] = True
    max_result = []

    while queue:
        n = queue.popleft()
        max_result.append(n)

        # find adjacent values
        for index in range(len(arr)):
            if arr[index][0] == n[0] and not visit[arr[index][1]]:
                # putin queue
                queue.append([arr[index][1], n[1] + 1])
                visit[arr[index][1]] = True

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

        # data = [[0] * 100 for k in range(100)]
        data = []
        visited = [False] * (max(contact) + 1)

        # data setting
        for j in range(0, len(contact), 2):
            data.append([contact[j], contact[j+1]])
            # data[contact[j] - 1][contact[j+1] - 1] = contact[j+1]

        # print(solution(data, visited, start_point))
        print("#" + str(i + 1) + " " + str(solution(data, visited, start_point)))

        print("start_time", start_time)  # 출력해보면, 시간형식이 사람이 읽기 힘든 일련번호형식입니다.
        print("--- %s seconds ---" % (time.time() - start_time))

