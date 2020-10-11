from collections import deque
import copy

def check_words(word, target) :
    if (word[:-1] == target[:-1]) or (word[1:] == target[1:]):
        return True
    if (word[0] == target[0] and word[-1] == target[-1]) :
        for i in range(1, len(target)-1):
            if word[:i-1] == target[:i-1] and word[i] != target[i] and word[i+1:] == target[i+1:]:
                return True
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
        v_new = copy.deepcopy(v)

        for index, value in enumerate(words) :
            p_word = words[v.index(max(v))]
            if (v[index] == 0) and check_words(p_word, value):
                if value == target :
                    return max(v)
                else :
                    v_new[index] = max(v) + 1
                    queue.append(v_new)
    return answer

if __name__ == "__main__" :
    begin = input()
    target = input()
    words = list(input().split())
    print(solution(begin, target, words))
