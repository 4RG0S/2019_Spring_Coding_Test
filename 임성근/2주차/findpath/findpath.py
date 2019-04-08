def solution():
    f = open('findpath_input.txt', 'r')
    while True:
        index = f.readline()
        path = f.readline()
        if not index:
            break
        array = [-1 for i in range(100)]
        array2 = [-1] * 100

        path_length = int(index.split(' ')[1])
        for i in range(path_length):
            if array[int(path.split(' ')[2*i])] == -1:
                array[int(path.split(' ')[2*i])] = int(path.split(' ')[2*i+1])
            elif array2[int(path.split(' ')[2*i])] == -1:
                array2[int(path.split(' ')[2*i])] = int(path.split(' ')[2*i+1])

        path = 0
        find = node()

        recursive(array, array2, path, find)
        print(index.split(' ')[0], find.data)

    f.close()


class node:
    def __init__(self):
        self.data = 0


def recursive(array, array2, path, find):
    if find == 1:
        return

    if array[path] == 99 or array2[path] == 99:
        find.data = 1

    if array[path] != -1:
        recursive(array, array2, array[path], find)
    if array2[path] != -1:
        recursive(array, array2, array2[path], find)


if __name__ == "__main__":
    solution()
