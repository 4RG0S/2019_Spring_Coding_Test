f = open("input.txt", 'r')
b = []
final_result = 0
num = 1
while True:
    line = f.readline()
    if not line:
        break
    a = line
    line = f.readline()
    b = line.split(' ')
    i = 0
    print('#', num)
    num = num + 1
    for i in range(2, int(a)-2):
        c = min(int(int(b[i]) - int(b[i - 2])), int(int(b[i]) - int(b[i - 1])), int(int(b[i]) - int(b[i + 1])), int(int(b[i]) - int(b[i + 2])))
        if c > 0:
            final_result = final_result + c
            i = i+2
    print(final_result)
    final_result = 0


f.close()
