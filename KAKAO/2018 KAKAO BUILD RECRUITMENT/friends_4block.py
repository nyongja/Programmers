"""
아이디어 설명
왼쪽 위 블록부터 순서대로 오른쪽, 아래쪽, 대각선 블록 모두가 같은 블록이면 소문자로 바꿈 -> 삭제될 블록을 의미
한바퀴 다 돈 후 열을 기준으로 소문자가 아닌 블록들만 정리(남아있는 블록) -> 즉, 아래에서 남아있는 블록들 차례대로 쌓기 (빈 칸은 .으로 채움) 
.인 블록을 제외하고 다시 처음부터 끝까지 돌면서 같은 블록이 있는지 count 
"""

dx = [0, 1, 1] # 오른쪽, 아래쪽, 대각선
dy = [1, 0, 1]

def search(x, y, board, m, n) :
    for i in range(3) :
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= m or ny >= n :
            return False
        if (board[x][y].upper() != board[nx][ny].upper()) :
            return False
    return True

def solution(m, n, board):
    answer = 0
    # m : 판의 높이
    # n : 판의 폭
    # board : 배치 정보
    count = 0
    for i in range(m) :
        board[i] = list(board[i])

    while True :
        for i in range(m) : 
            for j in range(n) :
                if board[i][j] == "." : # 비어있는 블록인지 확인
                    continue
                if search(i, j, board, m, n) : # 4개 붙어있는 블록인지 체크
                    lower = board[i][j].lower() # 4개 붙어있는 블록이면 소문자로 바꾸기
                    if board[i][j] != lower : # 이미 소문자로 바껴있는 경우(중복이므로) count안함
                        count += 1
                        board[i][j] = board[i][j].lower() 
                    for k in range(3) :
                        if board[i+dx[k]][j+dy[k]] != lower :
                            board[i+dx[k]][j+dy[k]] = lower
                            count += 1
        if count == 0 :
            break
            
        #블록 정렬
        for y in range(n) :
            col = ""
            for x in range(m-1, -1, -1) : # 아래블록부터 순서대로 대문자인 블록들 체크 (남아있는 블록들)
                if board[x][y].isupper() :
                    col += board[x][y]
            col = col + "."*(m-len(col)) # 지워진 수 만큼 + "." 
            for x in range(m-1, -1, -1) : # 블록들 재정렬
                board[x][y] = col[m-1-x]
        answer += count
        count = 0
    return answer


if __name__ == "__main__" :
    m, n = map(int, input().split())
    board = []

    for i in range(m) :
        b = input()
        board.append(b)

    print(solution(m, n, board))