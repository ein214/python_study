letter = []
word = input("단어를 입력해 주세요: ")

for item in word:
    letter.append(item)

rv_letter = list(reversed(letter))

if letter == rv_letter:
    print(f"{word}는 회문입니다.")
else:
    print(f"{word}는 회문이 아닙니다.")
