def solution(num, _from, _by, _to):
    if num == 1:
        print('{} {} moved.'.format(_from, _to))
        return
    else:
        solution(num-1, _from, _to, _by)
        print('{} {} moved.'.format(_from, _to))
        solution(num-1, _by, _from, _to)


if __name__ == "__main__":
    while True:
        a = int(input())
        if a == 0:
            break
        solution(a, 1, 2, 3)
