answer = input("퀴즈 결과를 입력해 주세요.(예 : OOXOXXO) : ").split("X")

total = 0
for i in answer:
    for j in range(0, len(i)+1):
        total = total+j
print("퀴즈 점수 : ", total)