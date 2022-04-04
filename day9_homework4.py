numbers = input("숫자 두 개를 입력해 주세요. :")
x = int(input("배수를 알고 싶은 숫자를 입력해 주세요:"))
numsList = numbers.split(" ")

number1 = int(numsList[0])
number2 = int(numsList[1])

if number1 > number2:
    print("잘못된 입력입니다.")
else :
    for i in range(number1, number2+1):
        if i % x == 0:
            print(i, end=" ")