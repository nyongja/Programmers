def solution(name):
    answer = 0

    # 알파벳 조정 횟수 계산
    for i in name :
        ch_ascii = ord(i) - 64
        if ch_ascii <= 14 :
            answer += ch_ascii - 1
        else :
            answer += 27 - ch_ascii

    # 커서 이동 횟수 계산

    name_ = "A" * len(name)
    # 1) 그냥 직진
    idx = 0
    min_cnt = -1
    while name_ != name :
        name_ = name_[:idx] + name[idx] + name_[idx+1:]
        min_cnt +=1
        idx += 1
    # 2) 중간에 A만나면 되돌아가기
    cnt = 0
    for idx, alph in enumerate(name) :
        if alph != "A" :
            cnt += 1
        elif alph == "A" :
            cnt = 0
            tmp_idx = idx+1
            if tmp_idx < len(name):
                while name[tmp_idx] == "A" :
                    tmp_idx += 1
                    if tmp_idx >= len(name):
                        break
            if idx == 0 :
                cnt = len(name) - tmp_idx
            else:
                cnt = (idx - 1) * 2 + len(name) - tmp_idx
            break

    min_cnt = min(min_cnt, cnt)
    if min_cnt < 0 :
        min_cnt = 0
    answer += min_cnt
    return answer


if __name__ == "__main__" :
    name = input()
    print(solution(name))