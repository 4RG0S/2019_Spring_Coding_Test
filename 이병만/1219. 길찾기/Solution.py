def solution(arr1, arr2, i):
    sol_one = 0
    sol_two = 0

    if arr1[i] == 99 or arr2[i] == 99:
        return 1

    if arr1[i] != 100:
        next_direction = arr1[i]
        arr1[i] = 100
        sol_one = solution(arr1, arr2, next_direction)

    if arr2[i] != 100:
        next_direction = arr2[i]
        arr2[i] = 100
        sol_two = solution(arr1, arr2, next_direction)

    if sol_one == 1 or sol_two == 1:
        return 1
    else:
        return 0


if __name__ == '__main__':
    for i in range(10):
        path_1 = [100 for j in range(100)]
        path_2 = [100 for j in range(100)]

        num = (input().strip().split())
        num = list(map(int, num))
        size = num[1]

        load = (input().strip().split())
        load = list(map(int, load))

        for index in range(0, size * 2, 2):
            if path_1[load[index]] == 100:
                path_1[load[index]] = load[index + 1]
            else:
                path_2[load[index]] = load[index + 1]

        print("#" + str(i+1) + " " + str(solution(path_1, path_2, 0)))
