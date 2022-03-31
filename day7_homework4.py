number = int(input("숫자를 입력해 주세요:"))

x = 2
while x <= number :
    if number % x == 0:
        number = number / x
        print(x, end = " ")
    else:
        x = x + 1
         