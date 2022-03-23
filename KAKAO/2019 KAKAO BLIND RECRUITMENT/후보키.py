from itertools import combinations

def solution(relation):
    answer = 0
    n = len(relation[0]) # attributes 수

    keys = []
    # 가능한 키 모두 구하기
    for comb in list(list(combinations(range(n),  i)) for i in range(1, n+1)) : # 가능한 feature 조합
        for case in comb : 
            tmp = ["" for _ in range(len(relation))]
            for i in case :
                for j in range(len(relation)) :
                    tmp[j] = tmp[j] + relation[j][i]
                    
            att_set = set(tmp)
            if len(att_set) == len(relation) :
                keys.append(case)
    
    # 키 중에서 후보키만 필터링
    candidates = []
    for i in keys :
        flag = True
        for j in candidates :
            if len(set(i) & set(j)) == len(set(j)) :
                flag = False
                break
        if flag :
            candidates.append(i)
    answer = len(candidates)

    return answer

print(solution([["a", "1", "aaa", "c", "ng"], ["a", "1", "bbb", "e", "g"], ["c", "1", "aaa", "d", "ng"], ["d", "2", "bbb", "d", "ng"]]))