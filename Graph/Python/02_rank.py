'''
그래프
#2 순위
https://programmers.co.kr/learn/courses/30/lessons/49191
'''
def solution(n, results):
    answer = 0

    graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
    
    for result in results :
        a, b = map(int, result)
        graph[a][b] = 1
        graph[b][a] = -1
    # 플로이드 워샬 알고리즘으로 전체 대소비교 가능한 노드들 찾기
    for k in range(1, n+1) :
        for a in range(1, n+1) :
            for b in range(1, n+1) :
                if graph[a][b] == 0 :
                    if graph[a][k] == 1 and graph[k][b] == 1 :
                        graph[a][b] = 1
                    elif graph[a][k] == -1 and graph[k][b] == -1 :
                        graph[a][b] = -1
    for i in range(1, n+1) :
        if graph[i].count(0) == 2 :
            answer += 1
    return answer


n = 5
results = [[4, 3], [4, 2], [3, 2], [1, 2], [2, 5]]
print(solution(n, results))