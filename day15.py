import gugudan

gugudan.gugu2()

# 15-5-3
def isEven(num):
    return num % 2 ==0
filtered = list(filter(isEven, [1,3,4,2,5,3]))
print(filtered)