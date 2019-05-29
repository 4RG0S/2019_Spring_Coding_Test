class Tree:
    def __init__(self, num):
        self.value = num
        self.children = []


def child_index(children, num):
    for i in range(len(children)):
        if children[i].value == num:
            return i

    return -1

def check(tree, phone_number):
    # 1. 숫자열 끝까지 돌았는데 뒤에 노드가 남아있다 ==> True
    # 2. 숫자열 중간에 리프노드를 만났다 ==> True
    current = tree
    count = 0
    flag = True
    for num in phone_number:
        if (len(current.children) == 0) and (flag == True):
            return True
        elif (len(current.children) == 0) and (flag == False):
            current.children.append(Tree(num))
            current = current.children[0]
        elif (len(current.children) != 0):
            index = child_index(current.children, num)
            if index == -1:
                flag = False
                current.children.append(Tree(num))
                current = current.children[len(current.children) - 1]
            else:
                current = current.children[index]
                if (count == (len(phone_number)-1)) and (len(current.children) != 0):
                    return True

        count += 1

    return False

def solution(phone_book):
    root = Tree(-1)
    root.children = [Tree(-1)]

    for phone_number in phone_book:
        if check(root, phone_number) == True:
            return False

    return True

phone_book = ["12", "123", "1235"]
print(solution(phone_book))