def dfs(computers, v, visited, answer):
    # 현재 노드를 방문 처리
    visited[v] = True

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for index, value in enumerate(computers[v]):
        if (not visited[index]) and value == 1:
            dfs(computers, index, visited, answer)


def solution(n, computers):
    answer = 0
    visited = [False] * n
    for v in range(n) :
        for index, value in enumerate(computers[v]):
            if (not visited[index]) and value == 1:
                dfs(computers, index, visited, answer)
                answer += 1
    return answer


if __name__ == "__main__" :
    n = int(input())
    computers = []
    for i in range(n) :
        computers.append(list(map(int, input().split())))
    print(solution(n, computers))
