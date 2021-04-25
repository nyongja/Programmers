'''
2021 Kakao Build Recruitment
#4 합승 택시 요금
https://programmers.co.kr/learn/courses/30/lessons/72413
'''
INF = int(1e9)

def solution(n, s, a, b, fares):
    graph = [[INF] * (n + 1) for _ in range(n+1)]

    # 자기 자신으로 가는 비용은 0으로 초기화
    for i in range(1, n + 1) :
        graph[i][i] = 0

    # 각 간선에 대한 정보를 입력받아, 그 값으로 초기화
    for f in fares :
        x, y, z = f
        graph[x][y] = z
        graph[y][x] = z

    # 플로이드 워셜 알고리즘
    for k in range(1, n + 1) :
        for i in range(1, n + 1) :
            for j in range(1, n + 1) :
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

    # 택시 요금 최소값 찾기
    answer = graph[s][a] + graph[s][b]
    for i in range(1, n + 1) :
        answer = min(answer, graph[s][i] + graph[i][a] + graph[i][b])
    return answer

n, s, a, b = map(int, input().split())
f = int(input())
fares = []
for _ in range(f) :
    fares.append(list(map(int, input().split())))
