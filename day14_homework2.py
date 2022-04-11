class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calcRound(self):
        return (self.width + self.height) * 2
    
    def calcArea(self):
        return self.width * self.height

width = int(input("가로 : "))
height = int(input("세로 : "))

rect = Rectangle(width, height)
print("직사각형의 둘레는", rect.calcRound(), "이고, 넓이는 ", rect.calcArea(), "입니다.")