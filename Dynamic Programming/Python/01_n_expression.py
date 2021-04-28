'''
다이나믹 프로그래밍(동적 계획법)
#1 n으로 표현
https://programmers.co.kr/learn/courses/30/lessons/42895
'''
def solution(N, number):
    number_set = [set() for _ in range(8)]
    for index, n_set in enumerate(number_set, start=1):
        n_set.add(int(str(N) * index))  # 5, 55, 555, ..., N 이어붙이기 한 경우를 각 n_set에 넣어주기

    if number in number_set[0] : # N 하나로 타겟 값 만들 수 있는 경우
        answer = 1
        return answer

    for i in range(1,8):
        for j in range(i):
            for op1 in number_set[j]:
                for op2 in number_set[i-j-1]:
                    number_set[i].add(op1+op2)
                    number_set[i].add(op1-op2)
                    number_set[i].add(op2-op1)
                    number_set[i].add(op1 * op2)
                    if op2 != 0:
                        number_set[i].add(int(op1/op2))
                    if op1 != 0 :
                        number_set[i].add(int(op2//op1))

        if number in number_set[i] :
            print(number_set)
            answer = i+1
            break
    else:
        answer = -1
    return answer

print(solution(5, 5))