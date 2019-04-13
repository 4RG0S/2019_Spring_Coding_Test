f = open("input.txt", 'r')

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
