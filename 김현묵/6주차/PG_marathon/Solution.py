# 첫번재 풀이입니다. 효율성 : 0

# def solution(participant, completion):
#     for completionHuman in completion:
#         for participantHuman in participant:
#             if completionHuman == participantHuman:
#                 participant.remove(participantHuman)
#                 break
#
#     answer = participant[0]
#     return answer


# 두번재 풀이입니다. 효율성 : 0

def solution(participant, completion):
    for completionHuman in completion:
        if completionHuman in participant:
            participant.remove(completionHuman)


    answer = participant[0]
    return answer






# 파이썬 파일 실행 후 첫번재 줄에 마라톤 선수들의 이름을 입력합니다.
# 각 선수들 사이는 공백으로 구분합니다.
# 두번째 줄에는 완주한 선수들의 이름을 입력합니다.
# 각 선수들 사이는 공백으로 구분합니다.

athlete = input().strip().split()
success = input().strip().split()

athleteList = []
finishList = []

for human in athlete:
    athleteList.append(human)

for successHuman in success:
    finishList.append(successHuman)

failHuman = solution(athleteList, finishList)
print(failHuman)