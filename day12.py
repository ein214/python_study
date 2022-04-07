# 12-1 집합 : 파이썬에서만 사용되는 자료형
"""
다른 자료형들과 달리 중복을 허용하지 않고, 순서가 없음
리스트나 튜플처럼 인덱스를 이용해 접근하는 것이 불가능
파이썬 내장 함수인 set()을 이용하거나 중괄호를 이용해 만들 수 있음. 단 중괄호 이용시에는 데이터 1개 이상 필수
"""

# code 12-1-1
a = set([5, 2, 3, 2, 1, 4])
b = set("apple")
c = {3, 6, 4, 7, 1, 7}
print(a, type(a))
print(b, type(b))
print(c, type(c))

# 12-2 합집합, 교집합, 차집합

#합집합 : union() or |
# code 12-2-1
a = set([1, 2, 3])
b = set([2, 3, 4])
print(a | b)
print(a.union(b))
print(b.union(a))

# code 12-2-2 교집합 & 또는 intersection()
print(a & b)
print(a.intersection(b))
print(b.intersection(a))

# code 12-2-3 차집합 - 또는 difference()
print(a - b)
print(b - a)
print(a.difference(b))
print(b.difference(a))