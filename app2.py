# name = input('이름 입력 : ')
# print('Hello', name)

# a, b = input('두 숫자 입력 : ')
# print(a,b)

a = 10
b = 20
print(a,b,sep=', ',end=' ')
print(a,b)

import sys

# fp = open('data.txt','w')
# print('Hello',file=fp)
# fp.close()

# sys.stdin   : 콘솔과 연결된 표준 입력
# sys.stdout  : 콘솔과 연결된 표준 출력
# sys.stderr  : 콘솔과 연결된 에러 출력

# print('Helo',file=sys.stdout)

try:
    print(10/0)
except:
    print('에러가 발생하였습니다.',file=sys.stderr)
    
a = 1
a <<= 2
print(a)

names = "Python"
print(names[0])
print(names[len(names)-1])
print(names[-(len(names))])
print(names[:])
print(names[3:])
print(names[:3])
print(names[:-2])

name = "Inu"
age = 30
print(f'My name is {name}')

print("이름 : %s, 연령 : %d" %(name,age))
pi = 3.14195
print("원주율 : %f" %pi)
print("원주율 : %10.2f" %pi)
print("원주율 : %10.3f" %pi)
print("원주율 : %010.4f" %pi)

obj = "이름 : {}"

print(type(name))
print(type(obj))

print(obj.format(name))
print("이름 : {1}, 연령 : {0}".format(age,name))
print("이름 : {name}, 연령 : {age}".format(age=age,name=name))
print('이름 : {:<20}, 연령 : {:>10}'.format(name,age))

person = {'name':'홍길동','age':20}
print('이름 : {0[name]}, 연령 : {0[age]}'.format(person))

money = 10000000
print("{:,}".format(money))