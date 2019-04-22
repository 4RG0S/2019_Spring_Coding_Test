def compare_route(route1, route2):
    length = len(route1) if len(route1) < len(route2) else len(route2)

    result = 1

    for i in range(length):
        if route1[len(route1)-1-i] != route2[len(route2)-1-i]:
            result = route1[len(route1)-i]
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

    return size;

def main():
    case = int(input())

    for n in range(case):
        tmp = list(map(int, input().strip().split()))

        count_vertex, count_edge, node1, node2 = tmp[0], tmp[1], tmp[2], tmp[3]

        tmp = list(map(int, input().strip().split()))

        dict = {1: 0}

        for i in range(0, count_edge * 2, 2):
            dict[tmp[i + 1]] = tmp[i]

        route1 = build(dict, node1)
        route2 = build(dict, node2)

        result_node = compare_route(route1, route2)

        print('#{} {} {}'.format(n + 1, result_node, subtree_size(dict, result_node)))

if __name__ =="__main__":
    main()