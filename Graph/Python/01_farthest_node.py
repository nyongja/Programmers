'''
그래프
#1 가장 먼 노드
https://programmers.co.kr/learn/courses/30/lessons/49189
'''
from collections import deque

INF = int(1e9) # 무한을 의미하는 값으로 10억을 설정


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]
    visited = [-1] * (n+1)

    for e in edge :
        a, b = map(int, e)
        graph[a].append(b)
        graph[b].append(a)

    # bfs
    queue = deque([1])
    visited[1] = 0
    while queue :
        cur = queue.popleft()
        for next in graph[cur] :
            if visited[next] == -1 :
                visited[next] = visited[cur] + 1
                queue.append(next)
    max_val = max(visited)
    answer = visited.count(max_val)
    return answer

n = 6
edge = [[3, 6], [4, 3], [3, 2], [1, 3], [1, 2], [2, 4], [5, 2]]
print(solution(n, edge))