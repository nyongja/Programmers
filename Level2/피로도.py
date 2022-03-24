'''
https://programmers.co.kr/learn/courses/30/lessons/87946
'''

from itertools import permutations

def solution(k, dungeons):
    answer = -1
    n = len(dungeons) # 던전 갯수
    
    for perm in list(permutations(range(0, n), n)) :
        cnt = 0
        now_k = k
        for i in perm :
            if now_k >= dungeons[i][0] :
                now_k -= dungeons[i][1]
                cnt += 1
        answer = max(answer, cnt)
    return answer