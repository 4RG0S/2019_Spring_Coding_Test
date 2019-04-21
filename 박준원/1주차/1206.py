def max(a, b):
    return a if a > b else b


def min(a, b):
    return a if a < b else b


width = input()
array = input()

count = 0

for i in range(2, width - 2):
    left_max = max(array[i - 1], array[i - 2])
    left_result = array[i] - left_max

    right_max = max(array[i + 1], array[i + 2])
    right_result = array[i] - right_max

    result = min(left_result, right_result)

    if result > 0:
        count = count + result

print(count)