class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def setX(self, x):
        self.x = x
    
    def setY(self, y):
        self.y = y
    
    def get(self):
        return (self.x, self.y)
    
    def move(self, x, y):
        self.x += x
        self.y += y


x = int(input("x좌표를 입력해 주세요. :"))
y = int(input("y좌표를 입력해 주세요. :"))

point = Point(x, y)
print("현재 좌표: ", point.get())
print("x좌표 설정을 원한다면 x를, \ny 좌표 설정을 원한다면 y를 \n좌표 이동을 원한다면 m을 \n좌표 설정을 종료하려면 0을 입력해 주세요.")
while(True):
    key = input("입력 :")
    if key == "x":
        point_x = int(input("x 좌표를 입력해 주세요. :"))
        point.setX(point_x)
    elif key == "y":
        point_y = int(input("y 좌표를 입력해 주세요. :"))
        point.setY(point_y)
    elif key == "m":
        move_x = int(input("x 좌표를 얼마만큼 이동할지 입력해 주세요. : "))
        move_y = int(input("y 좌표를 얼마만큼 이동할지 입력해 주세요. : "))
        point.move(move_x, move_y)
    elif key == "0":
        print("현재 좌표", point.get())
        break
    else:
        print("잘못된 키 입력입니다.")
