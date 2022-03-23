'''
2021 Kakao Build Recruitment
#7 매출 하락 최소화
https://programmers.co.kr/learn/courses/30/lessons/72416
'''


def dfs(sales, graph, count, v):
    # 현재 노드를 방문 처리
    if len(graph[v]) == 0 : # 리프노드면
        count[v][1] = sales[v-1]
        count[v][0] = 0
    elif len(graph[v]) != 0 : # 리프노드가 아니면 서브트리 방문
        sum_child = 0
        min_child = []
        check = False
        for i in graph[v]:
            count, min_v = dfs(sales, graph, count, i)
            sum_child += min_v
            min_child.append(count[i][1] - count[i][0])
            if count[i][0] > count[i][1] :
              check = True
        count[v][1] = sales[v-1] + sum_child
        if check:
            count[v][0] = sum_child
        else :
            count[v][0] = sum_child + min(min_child)
    min_v = min(count[v][1], count[v][0])
    return count, min_v

def solution(sales, links):
    answer = 0
    graph = [[] for _ in range(len(sales) + 1)]
    for link in links :
      graph[link[0]].append(link[1])

    count = [[0, 0] for _ in range(len(sales) +1)]
    count, _ = dfs(sales, graph, count, 1)
    answer = min(count[1][0], count[1][1])
    return answer


sales = [14, 17, 15, 18, 19, 14, 13, 16, 28, 17]
links = [[10, 8], [1, 9], [9, 7], [5, 4], [1, 5], [5, 10], [10, 6], [1, 3], [10, 2]]
print(solution(sales, links))