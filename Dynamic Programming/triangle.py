def solution(triangle):
    answer = 0

    for row in range(len(triangle)) :
        for value in range(len(triangle[row])):
            if value == 0 :
                triangle[row][value] = triangle[row][value] + triangle[row-1][value]
            elif row == value :
                triangle[row][value] = triangle[row][value] + triangle[row-1][value-1]
            else :
                triangle[row][value] = max(triangle[row-1][value-1], triangle[row-1][value] + triangle[row][value])
    answer = max(triangle[-1])
    return answer
if __name__ == "__main__" :
    triangle = []
    height = int(input())

    for _ in range(height) :
        triangle.append(list(map(int, input().split())))
    
    print(solution(triangle))