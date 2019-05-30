def solution(phone_book):
    answer = True

    phone_book.sort(key=len)
    search = phone_book[0]

    for match in phone_book:
        # 찾는 번호가 해당 번호에 있다면 False
        if match == search:
            # print(match)
            continue

        elif search in match[0:len(search)]:
            answer = False
            break

    return answer
