def solution(number, k):
    answer = ''
    stack = [number[0]]
    for num in number[1:] :
        while len(stack) > 0 and stack[-1] < num and k > 0 :
            stack.pop()
            k -= 1
        stack.append(num)
    if k != 0 :
        stack = stack[:-k]
    
    answer = answer.join(stack)
    return answer



if __name__ == "__main__" :
    number = input()
    k = int(input())
    print(solution(number, k))