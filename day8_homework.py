def getSum(inputNumber):
    sum = 0
    for item in range(0, inputNumber+1):
        sum += item
    return sum

number = int(input("정수를 입력하세요:"))
print("0부터 %d까지의 합계는 %d입니다" % (number, getSum(number)))