import math
def binary_search(max_time, n):
    start = 0
    end = max_time
    answer = end
    while start <= end :
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 반환
        possible_person = 0
        for i in times :
            possible_person += mid // i
        if possible_person >= n :
            end = mid - 1
            if answer >= mid :
                answer = mid
        else :
            start = mid + 1
    return answer



def solution(n, times):
    answer = 0
    max_time = min(times) * n
    
    answer = binary_search(max_time, n)
    return answer


if __name__ == "__main__" :
    n = int(input())
    times = list(map(int, input().split()))
    
    print(solution(n, times)) 