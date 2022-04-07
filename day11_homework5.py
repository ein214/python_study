months_list = [31,28,31,30,31,30,31,31,30,31,30,31]
days_list = ['금','토','일','월','화','수','목']

month = int(input("월을 입력하세요.: "))
day = int(input("일을 입력하세요.: "))

if (month in range(1, 13) and day in range(1, months_list[month-1]+1)):
    total = day
    for i in range(month-1):
        total += months_list[i]

    y = days_list[total % 7]

    print(f"2022년 {month}월 {day}일은 {y}요일입니다")
else:
    print("잘못 입력하셨습니다.")