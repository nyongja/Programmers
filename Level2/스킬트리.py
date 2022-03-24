def solution(skill, skill_trees):
    answer = 0
    
    # 각 스킬 레벨 정리
    skill_dict = dict() # CBD
    for idx, value in enumerate(skill) :
        skill_dict[value] = idx
    
    for skill_tree in skill_trees :
        skill_level = 0
        flag = True
        for sk in skill_tree : # 스킬 하나씩 살펴보기
            if sk in skill_dict.keys() : # 선행 스킬이 있는 스킬이면
                if skill_dict[sk] == skill_level : # 현재 내가 배울 수 있는 스킬이면
                    skill_level += 1
                else :
                    flag = False
                    break
        if flag :
            answer += 1
      
    return answer

print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))