def reverse_number(n):
    number = list(str(n))
    number.reverse()

    return int("".join(number))

def is_prime(n):
    count = 0
    for i in range(2, n+1):
        if n % i == 0:
            count += 1
    
    if count == 1:
        return True
    else:
        return False


count = int(input("입력받을 숫자의 개수를 입력해 주세요.: "))
lst = []
for i in range(count):
    number = input(f"{i+1}번째 숫자를 입력해 주세요.: ")
    lst.append(number)
    
for j in lst:
    reverse = reverse_number(j)

    if is_prime(reverse):
        print(reverse_number(reverse), end=" ")
