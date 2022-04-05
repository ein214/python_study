# 리스트 : 여러 개의 데이터를 묶어 하나의 변수에 저장한 것
# 리스트 응용함수
"""
1. append() : 데이터 맨 뒤에 삽입
2. insert('값을 추가할 인덱스', '데이터') : 원하는 위치에 데이터 삽입
3. del() : 인덱스로 데이터 삭제
4. remove() : 원하는 값을 찾아 삭제
5. sort() : 리스트 정렬
6. reverse() : 리스트의 인덱스를 거꾸로 만들기
"""

# code 10-3-1
a = [1,2,3,4,5,6,7,8,9,10]
print(a)
print(a[0:5])
print(a[5:10])
print(a[:5])
print(a[5:])

# code 10-4-1
a = []
a.append(0)
print(a)
a.append(1)
print(a)

# code 10-4-2
a = [1,2,3,4,5]
print(a)

a.insert(3, 6)
print(a)

del a[1]
print(a)

# 10-5 2차원 리스트
# code 10-5-1
array_2d = [["이", "차", "원"], ["리","스","트"]]
for array in array_2d:
    print(array)

for array in array_2d:
    for a in array:
        print(a, end=" ")
    print()

# code 10-5-3
print(array_2d[0])
print(array_2d[0][0])
print(array_2d[1][0:2])

# 11-1 튜플 - 리스트처럼 여러 데이터를 저장할 수 있는 자료형, 값을 소괄호로 감싸 사용
"""
리스트와 튜플
- 리스트는 가변적, 튜플은 불변적 튜플은 변경 불가
"""
# code 11-1-1
a = (1,2)
b = [1,2]
print(a)
print(b)

# code 11-2-4
blue = (0, 0, 255)
print("파란색의 RGB값은 ", blue, "입니다.")

# code 11-3-1
a = 10
b = 20
c, d  = a, b
print(a,b,c,d)

# code 11-3-2
def minmax(ex_lst):
    return min(ex_lst), max(ex_lst)

a = [1,2,3,4,5]
result = minmax(a)
print(result)
print(type(result))