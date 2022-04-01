def findMax(list):
    temp_max = 0
    for item in range(len(list)):
        if list[item] > list[temp_max]:
            temp_max = item
    return temp_max

list = [2, 10, 5, 6, 20000, 50, 50, 78, 3400]
print(findMax(list))