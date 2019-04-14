f = open("input.txt", 'r')
# 이 방식으로 하면.. 모두 검사해야 되는 단점이있음
# 만약 스택을 이용해서 괄호짝짓기가 실패를 했을때 바로 뽑으면 더 효율적임
def count_all(list):
    global count_1, count_2, count_3, count_4
    for i in range(0, len(list)):
        if list[i] == '(':
            count_1 += 1
        elif list[i] == '{':
            count_2 += 1
        elif list[i] == '[':
            count_3 += 1
        elif list[i] == '<':
            count_4 += 1

        elif list[i] == ')':
            count_1 -= 1
        elif list[i] == '}':
            count_2 -= 1
        elif list[i] == ']':
            count_3 -= 1
        elif list[i] == '>':
            count_4 -= 1
    if count_1 == 0 and count_2 == 0 and count_3 == 0 and count_4 == 0:
        print(1)
    else:
        print(0)

while True:
    count_1 = 0     # ()
    count_2 = 0     # {}
    count_3 = 0     # []
    count_4 = 0     # <>
    total = f.readline()
    line = f.readline()
    line = list(line)
    if not line:
        break
    print(line)
    count_all(line)
