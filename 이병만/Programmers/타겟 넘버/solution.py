cnt = 0


def func(numbers, target, curr, idx):
    global cnt
    if idx == len(numbers):
        if curr == target:
            cnt += 1
        return
    else:
        func(numbers, target, curr + numbers[idx], idx+1)
        func(numbers, target, curr - numbers[idx], idx+1)


def solution(numbers, target):
    global cnt
    func(numbers, target, 0, 0)
    answer = cnt
    return answer

if __name__ == '__main__':
    solution([1, 1, 1, 1, 1], 3)
