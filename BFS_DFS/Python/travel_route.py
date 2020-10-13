from collections import deque
import copy

def setting(data):
    return data[1]

def solution(tickets):
    answer = []
    queue = deque()
    visited = [-1]
    tickets.sort(key = setting)
    tickets.append(["_", "ICN"])
    queue.append(visited)

    while queue :
        v = queue.popleft()
        p_dest = tickets[v[-1]][1]
        for index, value in enumerate(tickets) :
            if index not in v and value[0] == p_dest :
                v_copy = copy.deepcopy(v)
                v_copy.append(index)
                queue.append(v_copy)

        if len(v_copy) == len(tickets) :
            for i in v_copy:
                answer.append(tickets[i][1])
            return answer

    return answer


if __name__ == "__main__" :
    n = int(input())
    tickets = []

    for _ in range(n) :
        tickets.append(list(input().split()))
    print(solution(tickets))