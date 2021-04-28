'''
이분 탐색
#2 징검다리
https://programmers.co.kr/learn/courses/30/lessons/43236
'''
def solution(distance, rocks, n):
    answer = 0
    rocks.sort()
    left, right = 0, distance
    while left <= right :
        mid = (left + right) // 2
        min_distance = float('inf')
        current = 0
        remove_cnt = 0

        for rock in rocks :
            diff = rock - current
            if diff < mid :
                remove_cnt += 1
            else :
                current = rock
                min_distance = min(min_distance, diff)

        if remove_cnt > n: 
            right = mid - 1
        else: 
            answer = min_distance
            left = mid + 1
    return answer


distance = 25
rocks = [2, 14, 11, 21, 17]
n = 2
print(solution(distance, rocks, n))