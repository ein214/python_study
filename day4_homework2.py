input_time = int(input("시간(초)을 입력해 주세요. :"))
print(input_time, "초", end="= ")
sec = input_time

if sec >= 86400:
    day = sec // 86400
    sec -= day
    print(day, "일", end=" ")

if sec >= 3600:
    time = sec // 3600
    sec -= time * 3600
    print(time, "시간", end=" ")

if sec >= 60:
    minute = sec // 60
    sec -= minute * 60
    print(minute, "분", end=" ")

if sec > 0:
    print(sec, "초")
    