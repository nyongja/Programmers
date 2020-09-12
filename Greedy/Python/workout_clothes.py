# https://programmers.co.kr/learn/courses/30/lessons/42862?language=python3
def solution(n, lost, reserve):
    # Sol 1
    lend = [i for i in lost if i in reserve] # 이미 빌려준 학생
    lost_st = [i for i in lost if i not in reserve] # 빌린 학생
    
    '''
    # Sol 2
    # 도난 당했지만 자기 체육복 여분이 있는 경우
    for i in lost :
        if i in reserve :
            lend.append(i)
        else :
            lost_st.append(i)
    '''

    # 자기 체육복 여분이 없는 학생 중 빌린 경우
    for i in lost_st :
        if i - 1 in reserve  and i - 1 not in lend  :
            lend.append(i-1)
        elif i + 1 in reserve  and i + 1 not in lend :
            lend.append(i+1)

    answer = n - len(lost) + len(lend)
    return answer


if __name__ == "__main__" :
    n = int(input())
    lost = list(map(int, input().split()))
    reserve = list(map(int, input().split()))
    print(solution(n, lost, reserve))