# 계산기
price = 3420
thousand_units = price // 1000
hundred_units = (price % 1000) // 100
won_units = (price % 100) // 10

print(price, "원을 계산하려면")
print("1000원 지폐", thousand_units, "장")
print("100원 동전 ", hundred_units, "개")
print("10원 동전", won_units, "개가 필요합니다.")