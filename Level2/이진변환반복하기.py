def solution(s):
    answer = []
    cnt = 0 # 제거한 0의 개수
    step = 0 # 회차
    
    while s != "1" :
        step += 1
        new_s = len(''.join(s.split("0")))
        cnt += len(s) - new_s
        
        s = ""
        while new_s != 1 and new_s != 0 :
            s = str(new_s % 2) + s
            new_s //= 2
        s = str(new_s)  + s
        
    answer = [step, cnt]
    
    return answer

print(solution("110010101001"))