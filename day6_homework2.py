height = int(input("키를 입력하세요:"))
weight = int(input("몸무게를 입력하세요.:"))

bmi = weight / ((height * 0.01) ** 2)

print("BMI 지수가", end=" ")
if bmi >= 25:
    print(bmi, " 이므로 비만입니다.")
elif bmi >= 23 and bmi < 25:
    print(bmi, " 이므로 과체중입니다.")
elif bmi >= 18.5 and bmi < 23:
    print(bmi, " 이므로 정상 체중입니다.")
else:
    print(bmi, " 이므로 저체중입니다.")