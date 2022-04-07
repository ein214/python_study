word = input("영어 단어를 입력하세요. : ")
word = list(set(word))
word.sort()
print("정렬결과 : ", word)

print("한큐에 끝내는 버전 : ", sorted(set(word)))