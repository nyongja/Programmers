from collections import deque

def solution(numbers, target):
    def bfs(start) :
        answer = 0
        q = deque([])
        q.append((numbers[start], start))
        q.append((-numbers[start], start))
        while q :
            result, index = q.popleft()
            if index == len(numbers)-1 :
                if result == target :
                    answer += 1
            else :
                index += 1
                q.append((result + numbers[index], index))
                q.append((result - numbers[index], index))
        return answer
    
    answer = bfs(0)

    
    def dfs(result, idx) :
        answer = 0
        if idx == len(numbers)-1 :
            if result == target :
                answer += 1
        else :
            idx += 1
            answer += dfs(result+numbers[idx], idx)
            answer += dfs(result-numbers[idx], idx)
        return answer
    
    #answer = dfs(0, -1)
    
    return answer

# def solution(numbers, target):
#     answer = 0

#     queue = deque()
#     queue.append(numbers[0])
#     queue.append(-numbers[0])

#     for n in numbers[1:] :
#         num_list = []
#         while queue :
#             num = queue.popleft()
#             num_list.append(num + n)
#             num_list.append(num - n)
#         for _ in range(len(num_list)) : queue.append(num_list.pop())
#     answer = queue.count(target)
#     return answer

if __name__ == "__main__" :
    numbers = list(map(int, input().split()))
    target = int(input())
    print(solution(numbers, target))
