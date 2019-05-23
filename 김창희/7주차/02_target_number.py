# 문제 url -> https://programmers.co.kr/learn/courses/30/lessons/43165
class Tree:
    def __init__(self, target_number):
        self.tree_body = [0]
        self.target_number = target_number
        self.count = 1    # 이진 트리 만들때 사용

    # 이진 트리 만들기    
    def make_tree(self, numbers):
        for number in numbers:
            for i in range(0, self.count):
                self.tree_body.append(number)
                self.tree_body.append(-number)
                
            self.count = self.count * 2
            
    # dfs 탐색
    def dfs(self, now_index, now_sum):
        now_sum = now_sum + self.tree_body[now_index]
    
        left_index = 2 * now_index + 1
        right_index = 2 * now_index + 2
    
        # now_index가 리프노드
        # 모든 노드의 자식이 0 또는 2이므로, left만 검사해도 됨
        if len(self.tree_body) - 1 < left_index:
            if now_sum == self.target_number:
                return 1
            else:
                return 0
        
        
        left = self.dfs(left_index, now_sum)
        right = self.dfs(right_index, now_sum)
            
        return left + right
    


def solution(numbers, target):
    tree = Tree(target)
    tree.make_tree(numbers)
    
    answer = tree.dfs(0, 0)
    
    return answer