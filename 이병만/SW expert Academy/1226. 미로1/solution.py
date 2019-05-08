def solution(arr, i, j):
    left = 0
    right = 0
    up = 0
    down = 0
    
    # 도착 지점인지 확인하기
    if arr[i][j] == 3 or arr[i][j-1] == 3 or arr[i][j+1] == 3 or arr[i-1][j] == 3 or arr[i+1][j] == 3:
        return 1

    # 현재 위치로 부터 왼, 오른, 위, 아래 보기
    if arr[i][j-1] == 0:
        maze[i][j] = 1
        left = solution(arr, i, j-1)

    if arr[i][j+1] == 0:
        maze[i][j] = 1
        right = solution(arr, i, j+1)

    if arr[i-1][j] == 0:
        maze[i][j] = 1
        up = solution(arr, i-1, j)

    if arr[i+1][j] == 0:
        maze[i][j] = 1
        down = solution(arr, i+1, j)

    if left == 1 or right == 1 or up == 1 or down == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    # 테스트 케이스 10번
    for i in range(10):
        # 미로를 저장하는 배열
        maze = []

        # case 번호
        num = list(map(int, (input().strip())))
        
        # 미로 한 줄씩 받기
        for lines in range(16):
            maze_line = list((input().strip()))
            int_to_arr = [int(i) for i in maze_line]
            maze.append(int_to_arr)

        # 시작점을 위한 변수
        start_row = 1
        start_col = 1

        # 출발 지점 찾기
        for j in range(1, 16):
            if maze[1][j] == 2:
                start_col = j
                break

        print("#" + str(i+1) + " " + str(solution(maze, start_row, start_col)))
