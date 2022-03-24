def solution(n):
    answer = ''
    while n :
        if n % 3 != 0 : # 3으로 안나누어떨어지면
            answer += str(n % 3)
            n //= 3
        else :
            answer += "4"
            n = n // 3 - 1
    return answer[::-1]

print(solution(12))
