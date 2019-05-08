def solution(arr):
    count = 0
    for i in range(2, len(arr) - 2):
        current_height = arr[i]
        # 왼쪽 2개 빌딩 중 가장 큰 거
        left = max(arr[i - 2:i])
        # 현재 빌딩보다 왼쪽이 크면 다음 빌딩으로
        if current_height < left:
            continue
        # 오른쪽 2개 빌딩 중 가장 큰 거
        right = max(arr[i + 1:i + 3])
        # 현재 빌딩보다 왼쪽이 크면 다음 빌딩으로
        if current_height < right:
            continue

        # 왼쪽, 오른쪽에서 가장 큰 빌딩 고르기
        max_height = max(left, right)
        # 현재의 빌딩 높이에서 가장 큰 높이를 가진 빌딩 빼기
        count += current_height - max_height
    return count


if __name__ == '__main__':
    for i in range(10):
        size = int(input().strip())
        arr = input().strip().split(" ")
        int_to_arr = [int(i) for i in arr]
        print("#" + str(i + 1) + " " + str(solution(int_to_arr)))
