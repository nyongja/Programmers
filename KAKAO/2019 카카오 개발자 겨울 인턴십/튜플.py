def solution(s):
    answer = []
    s = s[1:-1] # 대괄호 제거
    s = ''.join(s.split('{')).split('}')[:-1] # 집합 분리
    
    set_dict = dict() # 길이 별 집합 저장
    for i in s : 
        if i[0] == "," : i = i[1:] # 맨 앞 쉼표 제거
        nums = set(i.split(','))
        set_dict[len(nums)] = nums
    
    answer_set = set()
    for i in sorted(set_dict.keys()) : # 길이 짧은 순서대로 집합 업데이트
        diff = set_dict[i]-answer_set
        for num in diff : 
            answer_set.add(num)
            if num != "" :
                answer.append(int(num))
    return answer

print(solution("{{1,2,3},{2,1},{1,2,4,3},{2}}"))