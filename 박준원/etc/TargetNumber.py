class Node:
    def __init__(self, num):
        self.value = num
        self.left = None
        self.right = None

def buildTree(node, num):
    if node.left == None and node.right == None:
        node.left = Node(num)
        node.right = Node(-num)
        return

    buildTree(node.left, num)
    buildTree(node.right, num)

def count(node, sum, target):
    if node.left == None and node.right == None:
        temp = sum + node.value
        if temp == target:
            return 1
        else:
            return 0

    return count(node.left, node.value + sum, target) + count(node.right, node.value + sum, target)


numbers = [1, 2, 3, 4, 5]
target = 15

root = Node(0)

for num in numbers:
    buildTree(root, num)

print(count(root, 0, target))