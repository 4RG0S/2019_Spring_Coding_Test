# Problem URL -> https://programmers.co.kr/learn/courses/30/lessons/42576
def solution(participant, completion):
    completion_dict = dict()  # 완주자 딕셔너리 (해시맵)

    # 완주자 딕셔너리 완성하는 코드 (참가자명 : 동명이인 수) 로 완성됨
    # 참가자 리스트 뿐만아니라, 완주자 리스트에도 동명이인이 포함될 수 있음
    for completion_person in completion:
        completion_dict[completion_person] = completion_dict.get(completion_person, 0) + 1

    for person in participant:
        if person not in completion_dict or completion_dict[person] < 1:
            return person
        else:  # 동명이인 case를 고려
            completion_dict[person] = completion_dict[person] - 1