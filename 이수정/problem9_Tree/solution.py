if __name__ == '__main__':
  #  f = open("input.txt", "r")
    N = input().strip()

    for test_case in range(1, int(N)+1):
        tmp = input().strip().split()
        V = int(tmp[0])                         # 정점 수
        E = tmp[1]                              # 간선 수

        V1 = tmp[2]                             # 정점1
        V2 = tmp[3]                             # 정점2
  
        Tree = [0]*(V+1)                          # Child - Parent
        R_Tree = [[] for _ in range(V+1)]         # Parent 0 Child

        Edge = input().strip().split()            

        for j in range(0, int(E)*2, 2):
            Tree[int(Edge[j+1])] = int(Edge[j])
            R_Tree[int(Edge[j])].append(int(Edge[j+1]))

        P1 = Tree[int(V1)]
        P2 = Tree[int(V2)]

        stack = []
        stack2 = []

        while P1 != 0:
            stack.append(P1)
            P1 = Tree[P1]

        while P2 != 0:
            stack2.append(P2)
            P2 = Tree[P2]

        Root1 = stack.pop()
        Root2 = stack2.pop()

        result = Root1

        while Root1 == Root2 and len(stack) > 0 and len(stack2) > 0:
            result = Root1
            Root1 = stack.pop()
            Root2 = stack2.pop()

        sub_tree = []
        sub_tree.append(R_Tree[result][0])
        sub_tree.append(R_Tree[result][1])
        count = 1

        while len(sub_tree) != 0:
            node = sub_tree.pop()
            if len(R_Tree[node]) > 1:
                sub_tree.append(R_Tree[node][0])
                sub_tree.append(R_Tree[node][1])
                count = count+1
                continue

            elif len(R_Tree[node]) == 1:
                sub_tree.append(R_Tree[node][0])
                count = count+1
                continue
            else:
                count = count+1
        print("#"+str(test_case)+" "+str(result)+" "+str(count))
