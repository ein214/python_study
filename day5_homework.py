# 생년월일로 연도, 월, 일 출력하기

birth = int(input("생년월일을 입력해주세요: "))
year = birth // 10000
month = birth % 10000 // 100
day = birth % 100

print(year, "년", month, "월", day, "일 생이네요!")