# 프로그래머스 '전화번호 목록' 문제
# 문제링크 : https://programmers.co.kr/learn/courses/30/lessons/42577


# 정확성 : 84.6
# 효율성 : 15.4


# 해쉬 카테고리에 있는 문제이지만 어떻게 해쉬로 하는지는 잘 모르겠습니다.
# 리스트에 있는 번호 중 다른 번호의 접두어인 경우가 있으면 False고 그렇지 않으면 True를 리턴합니다.
def solution(phone_book):

    # 답으로 리턴될 answer 입니다. 초기값은 True로 줍니다.
    answer = True

    # phone_book 리스트의 각 인덱스에 위치한 반호를 오름차순 길이로 정렬해줍니다.
    phone_book.sort(key=len)

    # 길이가 짧은 번호부터 for문을 돌려줍니다.
    # 2중 for문이 돌아갈텐데 내부의 for문의 번호들은 현재 기준이 되는 번호보다 길이가 같거나 긴 경우 입니다.
    # 내부 for문의 번호를 기준이 되는 번호길이만큼 앞 부분을 봐서 같으면 answer를 False로 만들어 주고 break 합니다.
    # answer가 False가 되었으면 바깥 for문도 break 해줍니다.
    for num in range(len(phone_book)):
        for num2 in range(num+1, len(phone_book)):
            if phone_book[num2][0:len(phone_book[num])] == phone_book[num]:
                answer = False
                break
        if answer == False:
            break

    # 답을 return 해줍니다.
    return answer
