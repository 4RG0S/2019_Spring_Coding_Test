def arrayManipulation(n, queries):
    list = [0] * (n + 1)

    for query in queries:
        a, b, k = query
        list[a] += k
        if (b + 1) <= n:
            list[b + 1] -= k

    max = 0
    current = 0

    for value in list:
        current += value
        if current > max:
            max = current

    return max

def main():
    n = 5
    queries = [[1, 2, 100],
               [2, 5, 100],
               [3, 4, 100]]

    result = arrayManipulation(n, queries)

    print(result)

if __name__=='__main__':
    main()