'''
완전 탐색
#1 모의고사
https://programmers.co.kr/learn/courses/30/lessons/42840
'''

def solution(answers):
    answer = []
    
    student_1 = [1, 2, 3, 4, 5]
    student_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    student_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    score = [0, 0, 0]
    for idx, a in enumerate(answers) :
        if a == student_1[idx%5] :
            score[0] += 1
        if a == student_2[idx%8] :
            score[1] += 1
        if a == student_3[idx%10] :
            score[2] += 1
    max_score = max(score)
    for s in range(len(score)) :
        if score[s] == max_score :
            answer.append(s+1)

    return answer

answers = [1,2,3,4,5]
print(solution(answers))