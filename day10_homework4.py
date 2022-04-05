"""
첫번째 단어는 제약이 없다.
두번째 단어부터는 앞 단어의 마지막 글자와 동일한 글자로 시작되어야한다
앞에서 입력했던 단어를 다시 입력하는 경우에도 게임을 종료
5의 배수 번째 단어를 입력하고 나면 누적된 단어가 몇개인지 알려준다
"""
words = []
index = 0
while(1):
    word = input()
    
    if index > 1 and (words[index-1][-1] != word[0]):        
        print("틀린 단어를 입력하셨습니다. 게임을 종료합니다.")
        break
    elif word in words:
        print("앞에서 사용한 단어와 동일한 단어를 입력하셨습니다. 게임을 종료합니다.")
        break

    words.append(word)
    
    if (index+1) % 5 == 0:
        print(f"(중간 점검) 현재 {index+1}개의 단어를 입력하셨습니다.")

    index += 1
