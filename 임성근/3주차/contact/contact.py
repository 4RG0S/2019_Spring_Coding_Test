from collections import deque


def solution():
    f = open('contact_input.txt', 'r')
    problem_index = 1
    while True:
        index = f.readline()
        data = f.readline()
        if not index:
            break

        start_index = int(index.split(' ')[1])
        last_index = int(int(index.split(' ')[0])/2)

        all_array = []
        array = []
        node_array = []
        head_node = Node(start_index)
        for i in range(last_index): #headnode가 첫번째에 있지 않을 수 있으니 돌면서 찾아줌
            from_index = int(data.split(' ')[2*i])
            to_index = int(data.split(' ')[2*i+1])
            all_array.append(from_index)
            all_array.append(to_index)
            new_node = Node(from_index)
            new_node.set_child(to_index)
            if from_index not in array:
                array.append(from_index)
            node_array.append(new_node)
            if from_index == start_index: #headnode에 child를 넣어줌
                head_node.set_child(to_index)

        index_tree = []
        queue = deque(maxlen=30)
        queue.append(start_index)
        index_tree.append(start_index)
        result = 0
        while is_not_empty(queue):
            length = len(queue)
            for i in range(len(queue)): #모든원소에 대해 검사
                if queue[i] in array: #처음부터 해당 값이 시작점일때(자식이 있을때)
                    for j in range(len(node_array)):# 모든 노드에서
                        if queue[i] == node_array[j].get_index(): #해당 노드와 같으면
                            for k in range(len(node_array[j].get_child())): #해당 노드의 모든자식을
                                if node_array[j].get_child()[k] not in index_tree: #순환이 아닌경우
                                    queue.append(node_array[j].get_child()[k]) #큐에 넣는다.
                                    index_tree.append(node_array[j].get_child()[k]) #순환검사를 위한 인덱스트리에 삽입.

            for l in range(length):
                queue.popleft()

            if is_not_empty(queue):
                result = max(queue)
        print('#' + str(problem_index), result)
        problem_index += 1







    f.close()


def is_not_empty(queue):
    if len(queue) == 0:
        return False
    else:
        return True


class Node:
    def __init__(self, index):
        self._index = index
        self._child = []
        self._depth = 0

    def set_index(self, index):
        self._index = index

    def get_index(self):
        return self._index

    def set_child(self, child):
        self._child.append(child)

    def get_child(self):
        return self._child

    def set_parent(self, depth):
        self._depth = depth

    def get_parent(self):
        return self._depth

    def get_info(self):
        return self._index, self._child, self._depth


if __name__ == "__main__":
    solution()
