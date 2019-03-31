N = int(input())

print("이동 횟수 : ",2**N-1)

first = 1
second = 2
third = 3


def hanoi_tower(N,first,second,third):
    if N > 20:
        print("원판 갯수는 20개까지 가능")
    if N == 1:
        print(first,third," ")
        return;
    hanoi_tower(N-1, first, second, third)
    print(first, third, " ")
    hanoi_tower(N-1, second, third, first)



hanoi_tower(N, first, second, third)
