from collections import deque

if __name__ == '__main__':
    #f = open("input.txt", 'r')
    for i in range(10):
        tmp = input().strip()
        edge = input().strip().split()

        path = [[] for _ in range(101)]

        queue = deque()
        visited = []
        last = []

        n = tmp.split(' ')[0]
        start = tmp.split(' ')[1]

        for j in range(0, int(n), 2):
            edge[j] = int(edge[j])
            edge[j+1] = int(edge[j+1])

            path[edge[j]].append(edge[j+1])

        queue.append([int(start), 1])
        visited.append(int(start))

        #가장 깊은 곳을 찾아야함
        deepest = 1         
      
        #찾기
        while len(queue) > 0:
            tmp = queue.popleft()
            vertex = tmp[0]
            depth = tmp[1]

            count = 0
            for j in range(len(path[vertex])):
                if not(path[vertex][j] in visited):
                    count = 1
                    queue.append([path[vertex][j], depth+1])
                    visited.append(path[vertex][j])

            if count == 0:
                last.append([vertex, depth])

            deepest = depth
            
        #result에 최하위 연락  저장됨
        result = []
        for j in range(len(last)):
            if last[j][1] == deepest:
                result.append(last[j][0])

        print("#"+str(i+1),max(result))
