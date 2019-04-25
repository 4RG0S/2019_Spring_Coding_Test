q = list(map(int, input().rstrip().split()))

count = 0
is_chaotic = False

for i in range(len(q) - 1, 0, -1):
    if q[i] == i+1:
        continue
    elif q[i-1] == i+1:
        tmp = q[i-1]
        q[i-1] = q[i]
        q[i] = tmp
        count += 1
    elif q[i-2] == i+1:
        tmp = q[i-2]
        q[i-2] = q[i-1]
        q[i-1] = q[i]
        q[i] = tmp
        count += 2
    else:
        is_chaotic = True
        print(i, q[i-10:])
        break

if is_chaotic is True:
    print('Too chaotic')
else:
    print(count)
