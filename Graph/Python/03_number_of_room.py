'''
그래프
#3 방의 개수
https://programmers.co.kr/learn/courses/30/lessons/49190
'''

move = [(-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1), (0, -1), (-1, -1)]
def solution(arrows):
    answer = 0
    arrow_dict = dict()
    
    cur_x, cur_y = 0, 0
    for arrow in arrows :
      if (cur_x, cur_y) in arrow_dict.keys() :
        arrow_dict[(cur_x, cur_y)].add(arrow)
      else :
        arrow_dict[(cur_x, cur_y)] = set()
        arrow_dict[(cur_x, cur_y)].add(arrow)

      new_x = cur_x + move[arrow][0]
      new_y = cur_y + move[arrow][1]
      
      if (new_x, new_y) in arrow_dict.keys() :
        if (arrow not in arrow_dict[(new_x, new_y)]) :
          answer += 1
      
      cur_x, cur_y = new_x, new_y
      
    return answer

arrows = [5, 2, 7, 1, 6, 3]
print(solution(arrows))