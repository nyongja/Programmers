'''
2021 Kakao Build Recruitment
#5 광고 삽입
https://programmers.co.kr/learn/courses/30/lessons/72414
'''



def str_to_int(time):
    h, m, s = time.split(':')
    return int(h) * 3600 + int(m) * 60 + int(s)


def int_to_str(time):
    h = time // 3600
    h = '0' + str(h) if h < 10 else str(h)
    time = time % 3600
    m = time // 60
    m = '0' + str(m) if m < 10 else str(m)
    time = time % 60
    s = '0' + str(time) if time < 10 else str(time)
    return h + ':' + m + ':' + s


def solution(play_time, adv_time, logs):
    # 시간 -> 초로 환산
    play_time_sec = str_to_int(play_time)
    adv_time_sec = str_to_int(adv_time)

    total_time = [0 for _ in range(play_time_sec + 1)]

    for log in logs:
        start_time, end_time = log.split('-')
        total_time[str_to_int(start_time)] += 1
        total_time[str_to_int(end_time)] -= 1

    #
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i - 1]

    #
    for i in range(1, len(total_time)):
        total_time[i] += total_time[i - 1]

    #
    most_view = 0  # 가장 많이 본 횟수
    max_time = 0  # 가장 많이 본 시간 = 광고 play 할 시간
    for i in range(adv_time_sec - 1, play_time_sec):
        if i >= adv_time_sec:
            if most_view < total_time[i] - total_time[i - adv_time_sec]:
                most_view = total_time[i] - total_time[i - adv_time_sec]
                max_time = i - adv_time_sec + 1
        else:
            if most_view < total_time[i]:
                most_view = total_time[i]
                max_time = i - adv_time_sec + 1

    answer = int_to_str(max_time)
    return answer


play_time = "02:03:55"
adv_time = "00:14:15"
logs = [
    "01:20:15-01:45:14", "00:40:31-01:00:00", "00:25:50-00:48:29",
    "01:30:59-01:53:29", "01:37:44-02:02:30"
]

print(solution(play_time, adv_time, logs))
