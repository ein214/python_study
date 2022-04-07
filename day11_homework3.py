hour24 = input("24시 시준의 시간을 입력해 주세요. :").split(":")

hour = int(hour24[0])
convert_hour = hour
type = ""

if hour < 0 or hour > 24:
    print("잘못된 숫자를 입력했습니다.")
else :
    if hour >= 12:
        type = "PM"
        convert_hour = hour - 12
    else:
        type = "AM"

    print(f"변환 시간 : {convert_hour}:{hour24[1]} {type}")
