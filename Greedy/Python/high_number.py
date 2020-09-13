def solution(number, k):
    answer = ''
    num_list = list(number)
    count = len(num_list) - k
    start = 0
    end = -(count)+1

    while count > 0 :
        if end == 0 :
            if start == len(num_list) - 1 :
                answer += num_list[-1]
                break
            else :
                answer += max(num_list[start:])
                start = start + num_list[start:].index(max(num_list[start:])) + 1
        else :
            answer += max(num_list[start : end])
            start = start + num_list[start:end].index(max(num_list[start : end])) + 1
        count -= 1
        end = -(count)+1
    return answer



if __name__ == "__main__" :
    number = input()
    k = int(input())
    print(solution(number, k))