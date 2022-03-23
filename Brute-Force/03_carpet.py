'''
완전 탐색
#3 카펫
https://programmers.co.kr/learn/courses/30/lessons/42842
'''
def solution(brown, yellow):
    answer = []
    if yellow == 1 :
        return [3, 3]
    for num in range(1, yellow) :
        if yellow % num == 0 :
            y_h = num
            y_w = int(yellow / num)
            width = y_w + 2
            height = y_h + 2
            if width*2+height*2-4 == brown :
                return [width, height]  


print(solution(8, 1))