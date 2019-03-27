# 1이면 왼쪽, 오른쪽에 1이 있는지 확인 있다면 왼쪽, 오른쪽으로 이동.
# 마지막 인덱스까지 가면 도착이므로 반복문 끝
# 값이 2라면 해당 i의 값 반환


def solution(array):
    # left = 0, right = 1, up = 2
    next_direction = 2
    end_point = 0

    # 맨 밑에 있는 줄에서 2를 먼저 찾는다.
    for k in range(100):
        if array[99][k] == 2:
            end_point = k

    start_row = 99
    start_col = end_point

    # 사다리 타고 올라가기
    while True:
        # 왼쪽
        if next_direction == 0:
            start_col -= 1
            # 현재의 위치에서 왼쪽이 0이나 끝부분이면 위로 이동
            if start_col < 0 or array[start_row][start_col - 1] == 0:
                next_direction = 2

        # 오른쪽
        elif next_direction == 1:
            start_col += 1
            # 현재의 위치에서 오른쪽이 0이나 끝부분이면 위로 이동
            if start_col == 99 or array[start_row][start_col + 1] == 0:
                next_direction = 2

        # 위쪽
        elif next_direction == 2:
            start_row -= 1

            # Terminate condition
            if start_row == 0:
                return start_col

            # 왼쪽 방향
            if start_col - 1 >= 0 and array[start_row][start_col - 1] == 1:
                next_direction = 0

            # 오른쪽 방향
            elif start_col + 1 <= 99 and array[start_row][start_col + 1] == 1:
                next_direction = 1


if __name__ == '__main__':
    line = []
    for i in range(10):
        num = input().strip()

        for lines in range(100):
            arr = input().strip().split(" ")
            int_to_arr = [int(i) for i in arr]
            line.append(int_to_arr)

        print("#" + str(1+i) + " " + str(solution(line)))
        line.clear()
