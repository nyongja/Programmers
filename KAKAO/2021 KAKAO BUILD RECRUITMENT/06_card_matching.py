'''
2021 Kakao Build Recruitment
#6 카드 짝 맞추기
https://programmers.co.kr/learn/courses/30/lessons/72415
'''

from itertools import permutations
from collections import deque

d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

def check_boundary(x, y):
    if x < 0 or x >= 4 or y < 0 or y >= 4 :
        return False
    return True

def end_game(b) :
    if b.count("0") == 16 :
        return True
    return False

def remove_element(b, e) :
    b = b.replace(e, "0")
    return b

def move(b, y, x, dy, dx):
    ny, nx = y+dy, x+dx
    if check_boundary(nx, ny) and b[ny * 4 + nx] == "0":
        return move(b, ny, nx, dy, dx)
    else :
        if check_boundary(nx, ny) :
            return (ny, nx)
        else :
            return (y, x)

def solution(board, r, c):
    answer = 0
    
    # 보드 -> 문자열로 변환
    b = ""
    for i in range(4) :
        for j in range(4) :
            b += str(board[i][j])
    q = deque([])

    cnt = 0
    enter = -1 # enter 클릭 위치 
    q.append((r, c, b, cnt, enter))
    s = set()

    while q :
        y, x, b, c, e = q.popleft()
        pos = 4 * y + x

        if (y, x, b, e) in s :
            continue
        s.add((y, x, b, e))

        if end_game(b) :
            return c
        
        # 방향 이동
        for (dy, dx) in d :
            ny, nx = y + dy, x + dx
            if check_boundary(ny, nx) :
                q.append((ny, nx, b, c+1, e))
        # ctrl + 방향이동
        for (dy, dx) in d :
            ny, nx = move(b, y, x, dy, dx)
            if ny == y and nx == x :
                continue
            q.append((ny, nx, b, c+1, e))
        
        # enter 하는 경우
        if b[pos] != 0 :
            if e == -1 :
                n_e = pos
                q.append((y, x, b, c+1, n_e))
            else :
                if e != pos and b[e] == b[pos] :
                    b = remove_element(b, b[e])
                    q.append((y, x, b, c +1, -1))

    return answer


board = [[1,0,0,3],[2,0,0,0],[0,0,0,2],[3,0,1,0]]
r = 1
c = 0
print(solution(board, r, c))