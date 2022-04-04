# hi. nicE to MEEt yOU. i'M hAPPY. tHen, gOOD Bye.
# THe wEaTHer iS vERy CleaR TOdAy. i nEEd To go FoR a waLK.
strings = input("문장을 입력해 주세요.")

sentence = strings.split(".")
for item in range(len(sentence) - 1):
    convert = sentence[item].strip().capitalize()
    sentence[item] = convert
print('. '.join(sentence))
