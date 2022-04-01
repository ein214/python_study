def printMultiple(n):
    for item in range(1, 10):
        print("%d X %d = %d" % (n, item, (n * item)))

while(1):
    n = int(input("2부터 9 사이 숫자를 입력해 주세요. (1을 누르면 프로그램이 종료됩니다."))
    if n == 1:
        print("프로그램을 종료합니다.")
        break
    elif n > 9:
        print("범위 외의 숫자입니다. 다시 시도하세요.")
    else:
        printMultiple(n)
