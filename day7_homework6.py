print("1. 10초\t2. 30초\t3. 1분\t4. 10분\t5. 시작")


total_time = 0

while(1):
    number = int(input("원하는 버튼의 숫자를 입력해 주세요."))
    if number == 5:
        print("전자레인지를 작동합니다.")
        break
    elif number == 1:
        total_time += 10
    elif number == 2:
        total_time += 30
    elif number == 3:
        total_time += 60
    elif number == 4:
        total_time += 600
    else:
        print("잘못된 입력입니다.")
        break

    
    print("%d : %02d" % (total_time // 60, total_time % 60))
    