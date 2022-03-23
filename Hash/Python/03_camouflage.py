'''
해시
#3 위장
https://programmers.co.kr/learn/courses/30/lessons/42578?language=python3
'''
from collections import defaultdict

def solution(clothes):
    answer = 1
    clothes_dict = defaultdict(list)

    for c_type in clothes :
        clothes_dict[c_type[1]].append(c_type[0])
    
    for key in clothes_dict : # 옷이 선택되는 경우의 수
        answer *= len(clothes_dict[key])+1
    answer -= 1 # 전부다 선택하지 않은 케이스 제외하기
    return answer


clothes = [["yellowhat", "headgear"], ["bluesunglasses", "eyewear"], ["green_turban", "headgear"]]
print(solution(clothes))