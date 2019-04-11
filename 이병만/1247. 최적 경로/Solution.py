import itertools
import sys


def data_setting():
    # number of client
    clients = int(input().strip())

    # input location
    input_location = list(map(int, input().strip().split()))

    # variable
    location = []
    company = (input_location[0], input_location[1])
    home = (input_location[2], input_location[3])

    # data setting
    for j in range(4, len(input_location), 2):
        location.append((input_location[j], input_location[j + 1]))

    min_value = create_permutation(company, location, home)

    return min_value


def create_permutation(arr1, arr2, arr3):
    min_distance = sys.maxsize
    for i in itertools.permutations(arr2):
        # At the beginning and end of each route, the coord of the company and the house are placed behind it.
        path = [arr1, *list(i), arr3]

        # Finds the distance from each path.
        distance = 0
        for idx in range(0, len(path) - 1):
            distance += abs(path[idx][0] - path[idx + 1][0]) + abs(path[idx][1] - path[idx + 1][1])

        if distance < min_distance:
            min_distance = distance
        else:
            pass

    return min_distance


if __name__ == '__main__':
    test_num = int(input().strip())

    # Test case
    for i in range(test_num):
        print("#" + str(i + 1) + " " + str(data_setting()))
