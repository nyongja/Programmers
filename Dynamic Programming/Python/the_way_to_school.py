def solution(m, n, puddles):
    answer = 0
    
    map = []
    for i in range(n) :
        map.append([])
        for j in range(m) :
            if i == 0 and j == 0 : # 시작 위치
                map[i].append(1)
            elif [j+1, i+1] in puddles : # 물에 잠긴 지역인 경우
                map[i].append(0)
            elif i == 0 : # 첫 번째 행은 왼쪽만 고려
                map[i].append(map[i][j-1])
            elif j == 0 : # 첫 번재 열은 위쪽만 고려
                map[i].append(map[i-1][j])
            else : # 그 외는 왼쪽, 위쪽 다 다 고려
                map[i].append(map[i-1][j] + map[i][j-1])
       
    answer = map[-1][-1] % 1000000007
    
    return answer


if __name__ == "__main__" :
    m = int(input())
    n = int(input())

    p = int(input()) # puddles 개수
    puddles = []
    for _ in range(p) :
        puddles.append(list(map(int, input().split())))

    print(solution(m, n, puddles))