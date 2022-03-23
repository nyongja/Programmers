def solution(land):
    answer = 0
    
    N = len(land)
    for row in range(N-2, -1, -1) :
        for col in range(4) :
            candidates = land[row+1][:col] + land[row+1][col+1:]
            land[row][col] += max(candidates)
    answer = max(land[0])
    return answer