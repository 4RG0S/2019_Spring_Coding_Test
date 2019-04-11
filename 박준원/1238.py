def data_setting():
    tmp = list(map(int, input().strip().split()))

    index = tmp[0]
    start = tmp[1]

    tmp = list(map(int, input().strip().split()))

    data_list = {}
    for i in range(0, len(tmp)):
        if i % 2 == 0:
            if tmp[i] in data_list:
                data_list[tmp[i]].append(tmp[i+1])
            else:
                data_list[tmp[i]] = [tmp[i+1]]

    return index, start, data_list

def there_is_next_node(node, data_list):
    return node in data_list


def main():
    for n in range(0, 10):
        index, start, data_list = data_setting()
        result = -1

        if start in data_list:
            q_list = data_list[start]
            visit_list = {}
            current_step = 1

            visit_list[start] = current_step
            current_step += 1
            for node in q_list:
                visit_list[node] = current_step

            while len(q_list) is not 0:
                previous_nodes_count = len(q_list)
                current_step += 1

                for i in range(0, previous_nodes_count):
                    node = q_list.pop(0)  # remove first node in queue

                    if there_is_next_node(node, data_list):
                        next_nodes = data_list[node]
                        for next_node in next_nodes:
                            if next_node not in visit_list:
                                q_list.append(next_node)
                                visit_list[next_node] = current_step

            for value in visit_list:
                if visit_list[value] is (current_step - 1):
                    result = value if value > result else result

        else:
            result = start

        print('#{0} {1}'.format(n + 1, result))


if __name__ =="__main__":
    main()