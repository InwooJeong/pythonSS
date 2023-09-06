# List
lst = [1,2,3,['Python','Programming']]
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[3][0])
print(lst[3][0][2])
print(lst[-1][-1][-1])

lst[0] = 100
lst[-1] = ('Python','Script')
print(lst[0])
print(lst[1])
print(lst[2])
print(lst[3])
print(lst[3][0])
print(lst[3][0][2])
print(lst[-1][-1][-1])

lst = [1,2,3,['Python','Programming']]
print(lst[:])
print(lst[0:-1])

lst = [1,2,3]
lst[2] = 10
lst.append(100)
print(lst)

numbers = [1,2,3,4,5,6,7,8,9,10]
# del numbers[:5]
del numbers[-5:]
print(numbers)

numbers = [1,6,7,5,10,9,3,8,4,2]
numbers2 = [1,6,7,5,10,9,3,8,4,2]

numbers.sort(key=lambda x:10-x,reverse=True)         # 함수 제일 앞 * : 뭐가오건 다 버림 -> 이름 없어서 안 받겠다.
print(numbers)

numbers2.reverse()
print(numbers2)

# Tuple
t1=()
t2=(1,)
t3=(1,2,3)
t4=1,2,3
t5=(1,2,3,(1,2,3))

# Dictiionary
# 키는 중복 불가(immutable key)
# Association array(<-> Scalar), Hash
com = {'cpu':'i7-8550u','ram':16,'ssd':256}
print(com)
print(com['cpu'])

com['name'] = 'compu'    # 없으면 추가 있으면 value가 변경 
print(com)

for item in com:
    print(item)
    
for item in com.keys():
    print(item)
    
for item in com.values():
    print(item)
    
for item in com.items():
    print(item)
    
for key,value in com.items():
    print(f"{key} 의 값 : {value}")
    
keys = com.keys()
print(keys)
values = com.values()
print(values)
values = tuple(com.values())
print(values)
items = com.items()
print(items)

print('cpu' in com)
print(16 in com.values())

# Set
# 중복 허용 x
# 내부적으로 정렬 X -> 인덱싱, 슬라이싱 불가
A = {1,2,3,4,5}
B = {3,4,5,6,7}

# 교집한
# A & B

# 합집합
# A | B

# 차집합
# A - B
# B - A

setA = {1,2,3,4}
print(dir(setA))
listA = [1,2,3,4,]
print(dir(listA))

print(dir())            # 전역 객체
if __name__ == '__main__':
    print(__file__)
    print("메인 입니다.")