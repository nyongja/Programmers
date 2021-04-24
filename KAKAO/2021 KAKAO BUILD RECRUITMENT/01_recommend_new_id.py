'''
2021 Kakao Build Recruitment
#1 신규 아이디 추천
https://programmers.co.kr/learn/courses/30/lessons/72410
'''
import re

def solution(new_id):
    # step1 : Upper -> Lower
    new_id = new_id.lower()
    #print("step 1 : ", new_id)

    # step2 : alphabet, num, -, _, .
    new_id = "".join(re.findall("[a-z0-9_.\-]+", new_id))
    #print("step 2 : ", new_id)

    # step3 : .. -> .
    new_id = re.sub('[.]{2,}', '.', new_id)
    #print("step 3 : ", new_id)

    # step4 : eliminte . at first or last
    new_id = new_id.strip('.')
    #print("step4 : ", new_id)

    # step5 : empty string -> add 'a'
    if len(new_id) == 0 :
        new_id = "a"
    #print("step5 : ", new_id)

    # step6 : len(id) < 16
    if len(new_id) >= 16 :
        new_id = new_id[:15]
        new_id = new_id.rstrip('.')
    #print("step6 : ", new_id)
    
    # step7 : repeat last word 
    while len(new_id) <= 2 :
        new_id += new_id[-1]
    #print("step7 : ", new_id)

    return new_id

    
new_id = input()
print(solution(new_id))