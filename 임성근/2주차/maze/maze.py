import numpy as np


def solution():
    f = open('maze_input.txt', 'r')
    g = open('maze_output.txt', 'w')

    while True:
        array = np.zeros(shape=(16, 16)) # 16x16 배열 생성
        index = f.readline() # 한줄 읽음(테스트케이스)
        if not index:
            break
        for i in range(16): # 다음 16줄 읽어서 저장
            maze = f.readline()
            if not maze:
                break
            for j in range(16):
                array[i][j] = maze[j]
        start_x = 1
        start_y = 1
        recursive(index, array, start_x, start_y)

    g.close()
    f.close()


def recursive(index, array, start_x, start_y):
    if array[start_x][start_y] == 3:
        print("#" + str(index) + "1")
        return
    array[start_x][start_y] = -1
    if available(array, start_x + 1, start_y):
        recursive(index, array, start_x + 1, start_y)
    if available(array, start_x, start_y + 1):
        recursive(index, array, start_x, start_y + 1)
    if available(array, start_x - 1, start_y):
        recursive(index, array, start_x - 1, start_y)
    if available(array, start_x, start_y - 1):
        recursive(index, array, start_x, start_y - 1)


def available(array, x, y):
    if array[x][y] != 1 and array[x][y] != -1:
        return True
    else:
        return False


if __name__ == "__main__":
    solution()
