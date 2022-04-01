def circle_a(x):
    area = x * x * 3.1415
    return area
def tri_a(x, y):
    area = x * y / 2
    return area
def rect_a(x, y):
    area = x * y
    return area
def squ_a(x):
    area = x * x
    return area

print("""
========도형을 선택하세요===========
1. 원
2. 삼각형
3. 직사각형
4. 정사각형
""")

menu = int(input("도형을 선택하세요.:"))
if menu == 1:
    radius = int(input("반지름을 입력하세요. :"))
    print("반지름이 %d인 원의 넓이는 약 %.2f입니다." % (radius, circle_a(radius)))
elif menu == 2:
    base = int(input("삼각형의 밑변을 입력하세요.:"))
    height = int(input("삼각형의 높이를 입력하세요.:"))
    print("밑변의 길이가 %d 이고 높이가 %d인 삼각형의 넓이는 %d 입니다." % (base, height, tri_a(base, height)))
elif menu == 3:
    width = int(input("가로 길이를 입력하세요."))
    height = int(input("세로 길이를 입력하세요."))
    print("가로가 %d이고 세로가 %d인 직사각형의 넓이는 %d입니다." % (width, height, rect_a(width, height)))
elif menu == 4:
    base = int(input("한 변의 길이를 입력하세요. :"))
    print("한변의 길이가 %d인 정사각형의 넓이는 %d입니다" % (base, squ_a(base)))
else:
    print("잘못된 숫자를 선택하셨습니다.")