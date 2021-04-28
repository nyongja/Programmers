'''
해시
#1 완주하지 못한 선수
https://programmers.co.kr/learn/courses/30/lessons/42576?language=python3
'''

def solution(participant, completion):
    
    participant.sort()
    completion.sort()
    
    answer = ''
    for i in range(len(completion)):
        if (participant[i] != completion[i]):
            return participant[i]
    return participant[len(participant)-1]

participant = ["leo", "kiki", "eden"]
completion = ["eden", "kiki"]
print(solution(participant, completion))