number = int(input("숫자를 입력해 주세요.:"))

fact = 1
for i in range(1, number+1):
    fact = fact * i
print(str(number) + "!은 " + str(fact) + "입니다.")
