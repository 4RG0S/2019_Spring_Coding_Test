import itertools

def build_list(list):
    temp = []
    for i in range(0, len(list)):
        if i % 2 == 0:
            temp.append((list[i], list[i+1]))

    return temp

def build_matrix(point_count, point_list):
    matrix = []
    for i in range(0, point_count+2):
        temp = []
        for j in range(0, point_count+2):
            temp.append(distance(point_list[i], point_list[j]))

        matrix.append(temp)

    return matrix

def distance(a, b):
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def find_min(array):
    min = 9999

    for num in array:
        if num < min:
            min = num

    return min

def main():
    index = int(input().strip())

    for i in range(0, index):
        point_count = int(input().strip())
        point_list = build_list(list(map(int, input().strip().split())))

        weight_matrix = build_matrix(point_count,point_list)

        number_of_cases = list(itertools.permutations(range(2, point_count+2), point_count))

        result_set = []

        for case in number_of_cases:
            distance = weight_matrix[0][case[0]]

            for j in range(0, point_count-1):
                distance += weight_matrix[case[j]][case[j+1]]

            distance += weight_matrix[case[point_count-1]][1]
            result_set.append(distance)

        print('#{0} {1}'.format(i + 1, min(result_set)))


if __name__ =="__main__":
    main()