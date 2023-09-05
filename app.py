name = 'python'
age = 20
print(name)
print(age,id(age))

def func():
  pass

func()

name = None
age = 3.14
#name: str

print(name,type(name))
print(age,type(age),id(age))

age = 0x10
print(age,type(age))

age = 0o10
print(age,type(age))

age = 0b10
print(age,type(age))

number = -0b1
print(number)

# 데이터 단위
# 데이터 최소 단위 -> byte -> 8 bit로 구성 1024 byte = Kbyte
# 메모리 주소는 바이트 단위로 부여
# bit는 의미적으로 무엇인가 담을 수 있다

# 00000000 - 경우의 수 2의 8승(256)
# 11111111 - 값으로 본다면 0을 포함해야 함으로 255
# 음수도 표현 - 256을 절반으로 나눠 반은 음수 반은 양수
# 0은 영수에 속하므로 -128 ~ 127 -2의 8-1승 부터 2의 8-1승 -1까지

# 2진수 변환
# 몫이 0이 될 때 까지 2로 나누며 나머지를 떨군다. 떨굴때는 뒤에서 부터
# 10/2		5		0
# 5/2			2		1
# 2/2			1		0
#	1/2			0		1
#	00001010

# print(0b1010)

# signed 부호가 있는 정수, unsigned 부호가 없는 정수

# 첫 비트는 부호 비트(MSB : most signiture bit)
# 양수면 첫 비트는 0
# 음수면 첫 비트는 1

# -10
# 1. 부호비트를 구한다.
# 2. 절대값을 이진수로 변환한다.
# 00001010
# 3. 1의 보수를 취한다.
# (6의 10의 보수는? 4)
# 11110101 <- 1의 보수
# 4. +1을 한다.
# 11110110
# 11111111 11111111 11111111 11110110
# -1?
# 00000001
# 11111110 1의 보수
# 11111111 1을 더함 2의 보수를 취한다.

# 10000001 -1이라면 +1을 했을 때 0
# 10000010

# 11111111
# 00000001
# 00000000

print(-0b1)

# 부동소수점(float) : 부호1 지수8 유효자리수23 (4바이트 실수형)

print(u"\u00dcnic\u00f6de")
print(r"This is\nRaw String")
print("This is\nRaw String")

mylist = ['one','two','three']
mylist = []
print(bool(mylist))

var = None

try:
  var = 10
  
except:
  print('에러 발생')
finally:
  print(var)
  
nums = [1,2,3,4,5,6,7,8,9,10]  
nums[1] = 20
print(nums[1])

nums = (1,2,3,4,5,6,7,8,9,10)
# nums[0] = 10 TypeError: 'tuple' object does not support item assignment
print(nums[0])

dict = {'name': '홍길동', 'age': 20}
print(dict['name'], dict['age'])
dict['major'] = '전산'
print(dict['major'])

set = {1,2,3,4,5,5,5}
print(set)

A = {1,2,3}
B = {2,3,4}
print(A&B)
print(A-B)
print(A|B)
print(B-A)

str = 'ABCDE'
print(str[2:])

r = range(10)
print(r)
for i in r:
  print(i)
  
for i in range(10,20,2):
  print(i)
  
for i in range(30,20,-2):
  print(i)