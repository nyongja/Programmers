def solution(triangle):
    answer = 0

    for i in range(1, len(triangle)) :
        triangle[i][0] = triangle[i-1][0] + triangle[i][0]
        triangle[i][-1] = triangle[i-1][-1] + triangle[i][-1]
        for j in range(1, len(triangle[i])-1) :
            triangle[i][j] = max(triangle[i][j] + triangle[i-1][j-1], triangle[i][j] + triangle[i-1][j])

    answer = max(triangle[-1])

    return answer


if __name__ == "__main__" :
    triangle = []
    height = int(input())

    for _ in range(height) :
        triangle.append(list(map(int, input().split())))
    
    print(solution(triangle))