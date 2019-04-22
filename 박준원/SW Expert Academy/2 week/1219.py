# 김현묵 코드 참고

def recursion(i, m1, m2):
    one = 0
    two = 0

    if (m1[i] == 99) or (m2[i] == 99):
        return 1

    if m1[i] != 100:
        des1 = m1[i]
        m1[i] = 100
        one = recursion(des1)
    if m2[i] != 100:
        des2 = m2[i]
        m2[i] = 100
        two = recursion(des2)

    if (one == 1 or two == 1):
        return 1
    else:
        return 0

def main():
    m1 = []
    m2 = []

    for i in range(10):
        caseNum = (input().strip().split())
        caseNum = list(map(int, caseNum))
        couple = caseNum[1]

        oneline = input().strip().split()
        oneline = list(map(int, oneline))

        for t in range(100):
            m1[t] = 100
            m2[t] = 100

        for z in range(0, couple * 2, 2):
            if m1[oneline[z]] == 100:
                m1[oneline[z]] = oneline[z + 1]
            else:
                m2[oneline[z]] = oneline[z + 1]

        finish = recursion(0, m1, m2)

        print('#{0} {1}'.format(i + 1, finish))