from collections import deque

if __name__ == '__main__':
   # f = open("input.txt", 'r')

    for i in range(0, 10):
        path = [0 for _ in range(100)]
        path2 = [0 for _ in range(100)]
        queue = deque()

        tmp = input().strip()

        n = tmp.split(' ')[0]
        m = tmp.split(' ')[1]

        edge = input().strip()
        edge = edge.split()
        print(edge)

        for j in range(0, len(edge), 2):
            edge[j] = int(edge[j])
            edge[j+1] = int(edge[j+1])

            if path[edge[j]] == 0:
                path[edge[j]] = edge[j+1]

            else:
                path2[edge[j]] = edge[j+1]

        queue.append(0)

        while True:
            if len(queue) == 0:
                print("#"+str(n)+" 0")
                break

            v = queue.popleft()

            if path2[v] == 99 or path[v] == 99:
                print("#"+str(n)+" 1")
                break

            if path2[v] != 0:
                queue.append(path2[v])
                path2[v] = 0

            if path[v] != 0:
                queue.append(path[v])
                path[v] = 0
