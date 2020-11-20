def solution(money):
    answer = 0
    
    table = [0 for _ in range(len(money))]
    # 첫 번째 집을 털 경우
    table[0] = money[0]
    table[1] = max(money[0], money[1])
    for i in range(2, len(money)-1) :
        table[i] = max(table[i-1], money[i] + table[i-2])
    # 첫 번재 집을 털지 않는 경우
    table2 = [0 for _ in range(len(money))]
    table2[0] = 0
    table2[1] = money[1]
    for i in range(2, len(money)) :
        table2[i] = max(table2[i-1], money[i] + table2[i-2])
    
    answer = max(max(table), max(table2))
    return answer


if __name__ == "__main__" :
    money = list(map(int, input().split()))
    print(solution(money))