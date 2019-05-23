# 프로그래머스 '완주하지 못한 선수' 문제
# 문제링크 : https://programmers.co.kr/learn/courses/30/lessons/42576


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

# def solution(participant, completion):
#     for completionHuman in completion:
#         participant.remove(completionHuman)
#
#
#     answer = participant[0]
#     return answer




# 세번째 풀이입니다.

# 정확성 : 50
# 효율성 : 50

# 효율성의 문제로 해쉬를 써야 합니다.
# 리스트로 비교하며 remove 하는 과정은 O(n) 의 시간복잡도를 지니므로
# 해쉬로 key를 줘서 직접 찾는 O(1) 를 사용해야 효율성이 증가합니다.

# 파이썬에서 해쉬는 딕셔너리로 사용가능합니다.
# 참가자 이름을 key로 하여 딕셔너리를 만듭니다.
# value는 key의 이름을 가진 사람의 수입니다.[동명이인이 존재할 경우 2 이상]

def solution(participant, completion):

    partDict = dict()

    # 참가자 리스트에서 참가자 이름 수 만큼 딕셔너리의 value를 설정합니다.
    for part in participant:
        if part not in partDict:
            partDict[part] = 1
        else:
            partDict[part] = partDict[part] + 1

    # 완주자 목록 리스트를 key로 하여 value를 1씩 줄여줍니다.
    for comp in completion:
        partDict[comp] = partDict[comp] -1

    # 그러면 value를 1로 가지는 key가 답이 됩니다.
    for key, value in partDict.items():
        if value == 1:
            return key
