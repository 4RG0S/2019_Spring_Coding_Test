def compare_route(route1, route2):
    len_1 = len(route1)
    len_2 = len(route2)

    if len_1 < len_2:
        length = len_1
    else:
        length = len_2

    result = 1

    for i in range(length):
        if route1[len_1 - 1 - i] != route2[len_2 - 1 - i]:
            result = route1[len_1 - i]
            break

    return result


def build(dict, node):
    current = node
    route = []
    while current != 1:
        route.append(dict[current])
        current = dict[current]

    return route


def subtree_size(dict, node):
    size = 0

    stack = [node]

    while len(stack) != 0:
        current = stack.pop()
        size += 1

        count_check_child = 0
        for child, mother in dict.items():
            if mother == current:
                stack.append(child)
                count_check_child += 1
                if count_check_child == 2:
                    break

    return size


if __name__ == '__main__':
    # number of case
    case = int(input())

    for n in range(1, 11):
        tmp = list(map(int, input().strip().split()))
        vertex, edge, node_1, node_2 = tmp[0], tmp[1], tmp[2], tmp[3]

        tmp = list(map(int, input().strip().split()))

        dict = {1: 0}

        for i in range(0, edge * 2, 2):
            dict[tmp[i + 1]] = tmp[i]

        print(dict)
        route1 = build(dict, node_1)
        route2 = build(dict, node_2)

        result_node = compare_route(route1, route2)

        print("#" + str(n) + " " + str(result_node) + " " + str(subtree_size(dict, result_node)))



