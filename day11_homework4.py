# sort를 사용하지 말것 
# 출력값은 리스트 자료형으로 출력
# 숫자는 총 5개를 입력받되 한번에 하나씩만 입력받음

numbers = []

for n in range(5):
    number = int(input("숫자를 입력하세요. :"))
    numbers.append(number)

tmp = 0
for i in range(5):
    for j in range(i, 5):
        if numbers[i] > numbers[j]:
            tmp = numbers[i]
            numbers[i] = numbers[j]
            numbers[j] = tmp

print("오름차순 정렬 : ", numbers)
        
    