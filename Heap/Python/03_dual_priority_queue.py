'''
힙
#3 이중우선순위큐
https://programmers.co.kr/learn/courses/30/lessons/42628
'''
import heapq

def solution(operations):
    heap = []
    for op in operations :
        if op[0] == "I" :
            heapq.heappush(heap, int(op[2:]))
        elif heap :
            if op == "D 1" : # max 값 삭제
                heap = heapq.nlargest(len(heap), heap)[1:]
                heapq.heapify(heap)
            else :
                heapq.heappop(heap)

    if heap :
        min_value = heapq.heappop(heap)
        if heap :
            max_value = heapq.nlargest(1, heap)[0]
        else :
            max_value = min_value
        return [max_value, min_value]
    else :
        return [0, 0]


operations =["I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1", "I 1", "I 2", "I 3", "I 4", "I 5", "I 6", "I 7", "I 8", "I 9", "I 10", "D 1", "D -1", "D 1", "D -1"]


print(solution(operations))