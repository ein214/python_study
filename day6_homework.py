score1 = int(input("첫 번째 과목의 점수를 입력하세요:"))
score2 = int(input("두 번째 과목의 점수를 입력하세요:"))
score3 = int(input("세 번째 과목의 점수를 입력하세요:"))

average = (score1 + score2 + score3) / 3

if average >= 50:
    print("평균 점수는 " + str(average) + "점으로 합격입니다.")
else:
    print("평균 점수는 " + str(average) + "점으로 불합격입니다.")