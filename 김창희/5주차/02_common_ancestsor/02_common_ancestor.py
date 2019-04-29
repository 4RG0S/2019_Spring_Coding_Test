# Problem URL -> https://swexpertacademy.com/main/code/problem/problemDetail.do?contestProbId=AV15PTkqAPYCFAYD

class Vertex:
    def __init__(self):
        self.parent = None
        self.left_child = None
        self.right_child = None

    def set_parent(self, parent):
        self.parent = parent

    def set_left_child(self, left_chlid):
        self.left_child = left_chlid

    def set_right_child(self, right_child):
        self.right_child = right_child

    def get_parent(self):
        return self.parent

    def get_left_child(self):
        return self.left_child

    def get_right_child(self):
        return self.right_child


# 서브트리의 총 정점 개수 구하는 함수
def find_total_vertex(vertex_number, binary_tree_dict):
    if vertex_number is None:
        return 0

    vertex = binary_tree_dict[vertex_number]    # vertex_number에 대한 Vertex 인스턴스

    total_vertex_of_left_tree = find_total_vertex(vertex.get_left_child(), binary_tree_dict)
    total_vertex_of_right_tree = find_total_vertex(vertex.get_right_child(), binary_tree_dict)

    return total_vertex_of_left_tree + total_vertex_of_right_tree + 1


def main():
    with open('input.txt', 'r') as input_data:
        total_testcase = int(input_data.readline().strip())
        for testcase_num in range(1, total_testcase + 1):
            firstline_of_testcase = list(map(int, input_data.readline().strip().split(' ')))
            secondline_of_testcase = list(map(int, input_data.readline().strip().split(' ')))

            total_vertex = firstline_of_testcase[0]
            total_edge = firstline_of_testcase[1]
            ancestor_finder1 = firstline_of_testcase[2]
            ancestor_finder2 = firstline_of_testcase[3]

            binary_tree_dict = dict()

            for i in range(0, total_edge * 2, 2):
                parent = secondline_of_testcase[i]
                child = secondline_of_testcase[i + 1]

                # parent에 대한 처리
                if parent not in binary_tree_dict:        # 딕셔너리에 parent 정점이 저장되어 있지 않은 경우
                    binary_tree_dict[parent] = Vertex()
                    binary_tree_dict[parent].set_left_child(child)
                elif binary_tree_dict[parent].get_left_child() is None:     # 딕셔너리에 부모 정점이 이미 저장되어 있고, 자식이 없는 경우, child를 left_child로 설정
                    binary_tree_dict[parent].set_left_child(child)
                else:
                    binary_tree_dict[parent].set_right_child(child)   # 딕셔너리에 부모 정점이 이미 저장되어 있고, 자식이 있는 경우, child를 right_child로 설정

                # child에 대한 처리
                if child not in binary_tree_dict:         # 딕셔너리에 child 정점이 저장되어 있지 않은 경우
                    binary_tree_dict[child] = Vertex()
                    binary_tree_dict[child].set_parent(parent)
                else:                                     # 딕셔너리에 child 정점이 저장되어 있고, 부모가 없는 경우
                    binary_tree_dict[child].set_parent(parent)

            # finder1과 finder2의 조상 리스트
            ancestors_of_finder1 = list()
            ancestors_of_finder2 = list()

            # finder1과 finder2의 조상 리스트 완성하기
            track_parent = binary_tree_dict[ancestor_finder1].get_parent()
            while track_parent is not None:
                ancestors_of_finder1.append(track_parent)
                track_parent = binary_tree_dict[track_parent].get_parent()

            track_parent = binary_tree_dict[ancestor_finder2].get_parent()
            while track_parent is not None:
                ancestors_of_finder2.append(track_parent)
                track_parent = binary_tree_dict[track_parent].get_parent()

            result_vertex_number = [i for i in ancestors_of_finder1 if i in ancestors_of_finder2][0]
            total_vertex_of_subtree = find_total_vertex(result_vertex_number, binary_tree_dict)

            print('#{} {} {}'.format(testcase_num, result_vertex_number, total_vertex_of_subtree))

if __name__ == "__main__":
    main()