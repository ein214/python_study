"""
def digitSum(x):
    sum = 0
    for j in range(len(temp[item])):
        sum += int(temp[item][j])
    
    return sum

numbers = input("각 숫자를 공백으로 구분하여 입력해주세요.")

temp = numbers.split(" ")
max_sum = 0
max_index = 0
for item in range(len(temp)):
    digit_sum = digitSum(temp[item])
    if max_sum < digit_sum:
        max_sum = digit_sum
        max_index = item

print(temp[max_index])
"""

# 추천
numList, sumList = [], []
nums = input("각 숫자를 공백으로 구분하여 입력해 주세요.")
numList = nums.split(' ')
for i in numList:
    partial_sum = 0
    for n in i:
        partial_sum += int(n)
    sumList.append(partial_sum)
maxNum = max(sumList)
result = numList[sumList.index(maxNum)]
print(result)