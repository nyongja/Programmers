'''
해시
#2 전화번호
https://programmers.co.kr/learn/courses/30/lessons/42577?language=python3
'''

def solution(phone_book):
    phone_book.sort()
    for idx, num in enumerate(phone_book[:-1]) :
        if num == phone_book[idx+1][:len(num)] :
              return False
    return True


phone_book = ["123","12345","789"]
print(solution(phone_book))