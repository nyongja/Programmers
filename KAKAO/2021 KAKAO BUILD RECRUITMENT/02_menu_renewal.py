'''
2021 Kakao Build Recruitment
#2 메뉴 리뉴얼
https://programmers.co.kr/learn/courses/30/lessons/72411
'''
from itertools import combinations

def solution(orders, course):
    answer = []
    candidates = [{} for _ in range(len(course))]
    
    for order in orders :
        order = list(order)
        order.sort()
        for idx, val in enumerate(course) :
            menu_comb = list(map(''.join, combinations(order, val))) # 가능한 경우의 조합 만들어보기
            for menu in menu_comb : # 각 경우의 조합 등장횟수 count
                if menu not in candidates[idx] :
                    candidates[idx][menu] = 1
                else :
                    candidates[idx][menu] += 1

    for cand in candidates :
        if cand : 
            max_count = max(cand.values()) # 조합 중 인기 메뉴 고르기
            if max_count >= 2 :
                for k, v in cand.items() :
                    if v == max_count :
                        answer.append(k)
    answer.sort()
    return answer


num = int(input())
orders = []
for _ in range(num) :
    orders.append(input())
course = list(map(int, input().split()))

print(solution(orders, course))