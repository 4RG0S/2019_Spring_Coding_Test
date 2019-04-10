if __name__ == '__main__':
   # f = open("input.txt", 'r')
    for n in range(10):
        maze = [0*16 for i in range(16)]
        input().strip()

        for i in range(16):
            tmp = input().strip()
            tmp = tmp[:-1]
            maze[i] = list(tmp)

        # X, Y 축
        stack = [1, 1]
        maze[1][1] = "1"

        while True:
            if len(stack) == 0:
                print("#"+str(n+1)+" 0")
                break

            x = stack.pop()
            y = stack.pop()
            maze[x][y] = "1"

            if maze[x][y+1] == "3" or maze[x][y-1] == "3" or maze[x+1][y] == "3" or maze[x-1][y] == "3":
                print("#"+str(n+1)+" 1")
                break

            if maze[x][y+1] == "0":         #right
                stack.append(y+1)
                stack.append(x)

            if maze[x][y-1] == "0":         #left
                stack.append(y-1)
                stack.append(x)

            if maze[x+1][y] == "0":        #down
                stack.append(y)
                stack.append(x+1)

            if maze[x-1][y] == "0":        #up
                stack.append(y)
                stack.append(x-1)
