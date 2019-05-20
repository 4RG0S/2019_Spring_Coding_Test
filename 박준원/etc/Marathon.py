def solution(participant, completion):
    answer = ''

    d = {}
    for c in completion:
        if c in d:
            d[c] += 1
        else:
            d[c] = 1

    for p in participant:
        if p in d:
            if d[p] == 0:
                answer = p
                break
            else:
                d[p] -= 1

        elif p not in d:
            answer = p
            break

    return answer

def main():
    p, c = ["mislav", "stanko", "mislav", "ana"], ["stanko", "ana", "mislav"]
    print(solution(p, c))


main()