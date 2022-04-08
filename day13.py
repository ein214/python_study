# 13-1 딕셔너리 : key와 value가 있는 자료형
# key와 value에 넣을 수 있는 자료형이 다름. key에 넣을 수 있는 자료형은 제한적 변하지 않는 값인 숫자(정수,실수), 문자열, 튜플만 넣을 수 있음 
# 13-1-2
dic = {'python':'파이썬', 'c':'C언어', 'java':'자바'}
print(dic['python'])

# 13-1-1
dic = {'int':1, 'str':'문자', 'list':[1,2], 'tuple':(1,2), 'dict':{'python':'파이썬'}}
print(dic['int'])
print(dic['str'])
print(dic['list'])
print(dic['tuple'])
print(dic['dict'])

# 13-2 딕셔너리 수정
# 리스트처럼 추가, 삭제, 수정 가능하지만 key, value를 함께 쌍으로 추가하거나 삭제해야함. key는 수정 불가 value만 수정

# 13-3 for문과 딕셔너리
# 1. 딕셔너리 key값으로 반복하기 : 딕셔너리명.keys()
# 13-3-1
dic = {'a':'apple', 'b':'banana', 'c':'cool'}
print(dic.keys())

# 2. 딕셔너리 value값으로 반복하기 : 딕셔너리명.values()
# 13-3-3
print(dic.values())

# 3. 딕셔너리의 key, value 쌍으로 반복하기 : 딕셔너리명.items()
# 13-3-5
print(dic.items())
