sentence = input("문장을 입력해 주세요. :").split(" ")

sort_list = list(set(sentence))
sort_list.sort()
print(" ".join(sort_list))