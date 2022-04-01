def calculate(n):
    area = 0
    if n == 1:
        radius = int(input("반지름을 입력하세요. :"))
        area = radius * radius * 3.1415
        print("반지름이 %d인 원의 넓이는 약 %.2f입니다." % (radius, area))

    elif n == 2:
        base = int(input("삼각형의 밑변을 입력하세요.:"))
        height = int(input("삼각형의 높이를 입력하세요.:"))
        area = base * height / 2
        print("밑변의 길이가 %d 이고 높이가 %d인 삼각형의 넓이는 %d 입니다." % (base, height, area))

    elif n == 3:
        width = int(input("가로 길이를 입력하세요."))
        height = int(input("세로 길이를 입력하세요."))
        area = width * height
        print("가로가 %d이고 세로가 %d인 직사각형의 넓이는 %d입니다." % (width, height, area))
    
    elif n == 4:
        base = int(input("한 변의 길이를 입력하세요. :"))
        area = base ** 2
        print("한변의 길이가 %d인 정사각형의 넓이는 %d입니다" % (base, area))
    
    else:
        print("잘못된 숫자를 선택하셨습니다.")

print("""
========도형을 선택하세요===========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
""")

shapes = int(input("도형을 선택하세요.:"))
calculate(shapes)