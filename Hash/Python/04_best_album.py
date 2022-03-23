'''
해시
#4 베스트 앨범
https://programmers.co.kr/learn/courses/30/lessons/42579
'''
from collections import defaultdict

def sort_album() :
    return 
def solution(genres, plays):
    answer = []
    
    genre_count = defaultdict(lambda : 0)
    genre_num = defaultdict(list)

    for idx, genre in enumerate(genres) :
        genre_count[genre] += plays[idx] # 장르 별 총 재생 수
        genre_num[genre].append((plays[idx], idx)) # 장르 내 곡 각각 재생횟수
    genre_sort = sorted(genre_count.items(), key = lambda x : (-x[1])) # 인기 장르 찾기
    for i in genre_sort :
        genre = i[0]
        songs = genre_num[genre]
        songs = sorted(songs, key = lambda x : (-x[0], x[1])) # 장르 내 인기 곡 찾기
        if len(songs) == 1 : # 한 곡 만 있을때는 한 곡만 수록
            answer.append(songs[0][1])
        else : # 두 곡 이상이면 두 곡까지만 수록
            for j in songs[:2] :
                answer.append(j[1])
    return answer

genres = ["classic", "pop", "classic", "classic", "pop"]
plays = [500, 600, 150, 800, 600]
print(solution(genres, plays))