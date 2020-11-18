from collections import deque

def solution(numbers, target):
    answer = 0

    queue = deque()
    queue.append(numbers[0])
    queue.append(-numbers[0])

    for n in numbers[1:] :
        num_list = []
        while queue :
            num = queue.popleft()
            num_list.append(num + n)
            num_list.append(num - n)
        for _ in range(len(num_list)) : queue.append(num_list.pop())
    answer = queue.count(target)
    return answer

if __name__ == "__main__" :
    numbers = list(map(int, input().split()))
    target = int(input())
    print(solution(numbers, target))
