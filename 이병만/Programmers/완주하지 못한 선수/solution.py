def solution(participant, completion):
    participant.sort()
    completion.sort()
    answer = ''
    flag = False

    for i in range(len(completion)):
        if participant[i] != completion[i]:
            answer = participant[i]
            flag = True
            break

        if not flag:
            answer = participant[-1]

    return answer
