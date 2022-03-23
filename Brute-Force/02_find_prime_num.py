'''
완전 탐색
#2 소수찾기
https://programmers.co.kr/learn/courses/30/lessons/42839
'''

from itertools import permutations

def is_prime(num) :
    if num == 1 or num == 0:
        return False
    elif num ==2 :
        return True
    for i in range(2, num) :
        if num % i == 0 :
            return False
    return True

def solution(numbers):
    answer = set()
    numbers = list(numbers)
    for i in range(1, len(numbers)+1) :
        for num in list(map(''.join, permutations(numbers, i))) :
            if is_prime(int(num)) :
                answer.add(int(num))
    return len(answer)

numbers = "011"
print(solution(numbers))