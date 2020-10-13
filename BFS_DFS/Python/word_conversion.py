from collections import deque
import copy

def check_words(word, target) :
    if (word[:-1] == target[:-1]) or (word[1:] == target[1:]):
        return True
    cnt = 0
    for i in range(len(word)) :
        if word[i] == target[i] :
            cnt += 1
    if cnt == len(word) -1 : return True
    return False

def solution(begin, target, words):
    answer = 0
    visited = [0] * (len(words)+1)
    words.append(begin)
    visited[-1] = 1
    queue = deque()
    queue.extend([visited])

    if target not in words :
        return 0
    while queue :
        v = queue.popleft()
        p_word = words[v.index(max(v))]
        for index, value in enumerate(words) :
            if (v[index] == 0) and check_words(p_word, value):
                if value == target :
                    answer = max(v)
                    return answer
                else :
                    v_new = copy.deepcopy(v)
                    v_new[index] = max(v) + 1
                    queue.append(v_new)
    return answer

if __name__ == "__main__" :
    begin = input()
    target = input()
    words = list(input().split())
    print(solution(begin, target, words))
