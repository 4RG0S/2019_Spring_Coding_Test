def is_operator(value):
    return value == '+' or value == '-' or value == '*' or value == '/'

def main():
    for n in range(10):
        count_of_node = int(input())

        count_internal_node = int(count_of_node / 2)
        count_external_node = count_of_node - count_internal_node

        result = 1

        for i in range(count_internal_node):
            node_info = input().strip().split()
            node_value = node_info[1]

            if is_operator(node_value) == False:
                result = 0

        for i in range(count_external_node):
            node_info = input().strip().split()
            node_value = node_info[1]

            if is_operator(node_value) == True:
                result = 0

        print('#{} {}'.format(n + 1, result))


if __name__ =="__main__":
    main()