'''
힙
#1 더 맵게
https://programmers.co.kr/learn/courses/30/lessons/49190
'''
import heapq

def solution(scoville, K):
    answer = 0
    heap = []
    for i in scoville :
        heapq.heappush(heap, i)
    
    while (heap[0] < K):
        heapq.heappush(heap, heapq.heappop(heap) + heapq.heappop(heap)*2)
        answer += 1
        if (len(heap) == 1 and heap[0] < K):
            return -1
        
    return answer