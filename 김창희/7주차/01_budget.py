# 문제 링크 : https://programmers.co.kr/learn/courses/30/lessons/43237
def solution(budgets, M):
    if sum(budgets) <= M:   # 예산 요청의 합 <= 총 예산
        answer = max(budgets)
    else:   # 예산 요청의 합 > 총 예산

        # 가능한 상한액에 대하여 오름차순으로 정렬 (1 ~ 최대 예산 요청액)
        upper_limit_list = list(range(1, max(budgets) + 1))
        left = 0
        right = len(upper_limit_list) - 1

        answer = 0

        # 이분 탐색
        while left <= right:
            mid = int((left + right) / 2)
            upper_limit = upper_limit_list[mid]     # 이분탐색을 통한 상한액 찾기

            # 예산 요청 리스트에 대해 상한액을 적용
            temp_total_budget = sum(list(map(lambda budget: budget if budget <= upper_limit else upper_limit, budgets)))

            if temp_total_budget > M:   # 상한액을 적용한 예산 요청의 합 > 총 예산
                right = mid - 1         # 더 낮은 상한액 탐색

            elif temp_total_budget == M:    # 상한액을 적용한 예산 요청의 합 == 총 예산
                answer = upper_limit
                break                       # 더 이상 상한액을 탐색할 필요가 없음.

            else:                       # 상한액을 적용한 예산 요청의 합 < 총 예산
                answer = upper_limit
                left = mid + 1          # 더 높은 상한액 탐색

    return answer