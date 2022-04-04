string = input("가운데 글자를 찾을 단어를 입력하세요.")
sel = len(string)//2
if len(string) % 2 == 0:
    print(string[sel-1:sel+1])
else:
    print(string[len(string)//2])