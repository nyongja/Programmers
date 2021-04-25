'''
2021 Kakao Build Recruitment
#3 순위 검색
https://programmers.co.kr/learn/courses/30/lessons/72412
'''
from itertools import combinations
from collections import defaultdict

def solution(infos, queries):
    answer = []
    
    info_dict = defaultdict(list)

    for info in infos :
        info = info.split()
        score = info[-1]
        info = info[:-1]

        for i in range(5) : # 가능한 정보 조합 다 구하기
            for comb in combinations(info, i) :
                comb = ''.join(comb)
                info_dict[comb].append(int(score))

    for key in info_dict.keys() : # 스코어 정렬하기
        info_dict[key].sort()

    for query in queries :
        query = query.replace('and', '')
        query = query.replace('-', '')
        query = query.split()
        target_score = int(query[-1])
        query = ''.join(query[:-1])

        if query in info_dict : # 해당 쿼리가 존재하면
            scores = info_dict[query]
            if len(scores) > 0 :
                start = 0
                end = len(scores)
                while end > start :
                    mid = (start + end) // 2
                    if scores[mid] >= target_score : 
                        end = mid
                    else :
                        start = mid + 1
                answer.append(len(scores) - start)
        else :
            answer.append(0)

    return answer


info = []
query = []

n = int(input())
for _ in range(n) :
    info.append(input())

m = int(input())
for _ in range(m) :
    query.append(input())

print(solution(info, query))
