height = int(input("삼각형의 높이를 입력해 주세요.:"))

for i in range(1, height+1):
    print(' ' * (height - i) + '*' * i)


"""
for i in range(0, number):
    for j in range(0, number-i-1):
        print(" ", end = "")
    
    for k in range(number-i-1, number):
        print("*", end = "")
    print()
"""