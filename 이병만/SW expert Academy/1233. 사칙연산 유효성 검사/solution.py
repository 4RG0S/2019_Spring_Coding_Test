def check(operator):
    return operator == "+" or operator == "-" or operator == "*" or operator == "/"


if __name__ == '__main__':
    for n in range(1, 11):
        node = int(input())

        # 부모 노드, 자식 노드
        parent_node = int(node / 2)
        leaf_node = node - parent_node
        result = 1

        # 리프 노드를 제외하고 숫자가 있는지 확인
        for i in range(parent_node):
            node_info = input().strip().split()
            node_value = node_info[1]
            if not check(node_value):
                result = 0

        for i in range(leaf_node):
            node_info = input().strip().split()
            node_value = node_info[1]
            if check(node_value):
                result = 0

        print('#' + str(n) + " " + str(result))
