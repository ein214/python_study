class Calculator:
    def __init__(self, price, discount):
        self.price = price
        self.discount = discount
    
    def calc(self):
        return self.price - (self.price * self.discount / 100)
    
    def printCalc(self):
        print("최종 금액은 ", self.calc(), "입니다.")

price = int(input("원가를 입력하세요. :"))
discount = int(input("몇 퍼센트(%) 할인하나요? :"))

if discount > 100:
    print("잘못된 퍼센트입니다.")
else:
    calc = Calculator(price, discount)
    calc.printCalc()