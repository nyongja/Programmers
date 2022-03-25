def solution(number, k):
    remove_idx = 0
    while k > 0 :
        idx1 = max(0, remove_idx)
        for idx2 in range(idx1+1, len(number)) : # 비교할 인덱스
            if int(number[idx1]) < int(number[idx2]) :
                number = number[:idx1] + number[idx2:]
                remove_idx = idx1-1
                break
            idx1 = idx2
        else : 
            return number[:len(number)-k]
        k -= 1
    return number

print(solution("999", 2))