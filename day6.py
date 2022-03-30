# code 6-4-1
money = 3000
if money >= 5000:
    print('결제가 가능합니다.')
else:
    print("결제가 불가능합니다.")

# code 6-5-1
button = int(input("1~3 중에서 입력하세요. :"))
if button == 1:
    print("한식")
elif button == 2:
    print("중식")
elif button == 3:
    print("일식")
else:
    print("잘못된 번호 입력!")
print("맛있게 드세요!")