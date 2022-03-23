from collections import defaultdict

def check_pos(x, y) :
    if 0 <= x <= 10 and 0 <= y <= 10 :
        return True
    return False

def solution(dirs):
    answer = 0
    history = defaultdict(set)
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    dir_dict = {"U" : 0, "D" : 1, "L" : 2, "R" : 3}
    
    x, y = 5, 5
    for dir in dirs.strip() :
        idx = dir_dict[dir]
        nx, ny = x + dx[idx], y + dy[idx]
        if check_pos(nx, ny) :
            history[(x, y)].add((nx, ny))
            history[(nx, ny)].add((x, y))
            x, y = nx, ny
    for value in history.values() :
        answer += len(value)
    return answer // 2


print(solution("LULLLLLLU"))