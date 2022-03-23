def solution(A,B):
    answer = 0

    A.sort()
    B.sort()
    n = len(A)
    for i in range(n) : 
        answer += A[i] * B[n-i-1]
        
    return answer