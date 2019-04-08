# 김현묵 코드 참고

def recursion(i, j, Matrix):
    l = 0
    u = 0
    r = 0
    d = 0

    Matrix[i][j] = 1

    if Matrix[i][j] == 3 or Matrix[i - 1][j] == 3 or Matrix[i][j - 1] == 3 or Matrix[i][j + 1] == 3 or Matrix[i+1][j] == 3:
        return 1

    if Matrix[i + 1][j] == 0:
        r = recursion(i + 1, j)
    if Matrix[i][j + 1] == 0:
        d = recursion(i, j + 1)
    if Matrix[i - 1][j] == 0:
        l = recursion(i - 1, j)
    if Matrix[i][j - 1] == 0:
        u = recursion(i, j - 1)
    if ( r== 1 or d ==1 or l ==1 or u ==1 ):
        return 1
    else:
        return 0


def main():
    Matrix = [[0] * 16 for t in range(16)]

    for i in range(10):
        caseNum = (input().strip())
        for z in range(16):
            oneline = input().strip()
            # onelineRev = list(map(int, oneline))
            for j in range(16):
                if (int)(oneline[j]) == 2:
                    starting = z
                    finishing = j
                Matrix[z][j] = (int)(oneline[j])

        finish = recursion(starting, finishing, Matrix)

        print('#{0} {1}'.format(i+1, finish))

if __name__ =="__main__":
    main()