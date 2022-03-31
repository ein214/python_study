# code 7-2-1
for item in range(1, 11):
    print(item)

# code 7-2-2
for item in range(0, 11, 2):
    print(item)

# code 7-3-1
for i in range(2, 10):
    for j in range(1, 10):
        print(i * j, end = " ")
    print()

# code 7-4-1
for x in range(1,4):
    print(x)

# code 7-4-2
x = 1
while x <= 3:
    print(x)
    x = x + 1

# code 7-5-1
hit = 0
while hit < 5:
    hit = hit+1
    print("나무를", hit, "번 찍었습니다.")
    if hit == 5:
        print("쓰러집니다.")

# code 7-5-2
number = 0
while True:
    number = int(input("문을 여시겠습니까? (1: Yes, 2 : No)"))
    if number == 1:
        print("문이 열렸습니다.")
        break
    elif number == 2:
        print("문을 열 수 없습니다.")
