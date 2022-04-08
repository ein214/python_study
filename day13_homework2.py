stock_list = {
    "물" : 5,
    "콜라" : 10,
    "사이다" : 3,
    "과일 주스" : 0
}

menu_list = {
    "물" : 700,
    "콜라" : 1000,
    "사이다" : 1000,
    "과일 주스" : 800
}

print(f"""
======음료수 목록========
물\t\t\t\t{menu_list['물']}원
콜라\t\t\t\t{menu_list['콜라']}원
사이다\t\t\t\t{menu_list['사이다']}원
과일 주스\t\t\t{menu_list['과일 주스']}원
""")

money = int(input("자판기에 넣을 금액을 입력해 주세요."))
drink = input("마시고 싶은 음료를 입력해 주세요.")

print(f"{drink}의 가격은 {menu_list[drink]}원입니다.")
if money < menu_list[drink]:
    print("돈이 부족합니다")
else:
    if stock_list[drink] >= 1:
        print("주문이 완료되었습니다.")
        print(f"잔액은 {money - menu_list[drink]}")
        stock_list[drink] -= stock_list[drink] - 1
    else:
        print("현재 해당 음료는 품절 상태입니다.")
