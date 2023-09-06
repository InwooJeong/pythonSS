# number = int(input('정수 입력 : '))
# if number >= 19:
#     print('음주 가능 연령')
# else:
#     pass        #...

# number = int(input('몇 번 실행?'))
# i = 0
# while i<number:
#     i += 1
#     print(f"{i}번째 작업 실행")
#     if i >= 5:      #while 조건 탈출이 아님 -> else절 안 들어감
#         break
# else:
#     print("루프가 종료되었습니다.")

strings = "PYTHON"

for char in strings:
    print(char)
    if char == 'T':
        break
else:
    print('for loop end')
    
# score = int(input("점수 입력 : "))

# if (score >100) or (score <0):
#     print('입력 값을 확인하세요.')

# match score//10:
#     case 9 | 10:
#         print('A')
#     case 8:
#         print('B')
#     case 7:
#         print('C')
#     case _:
#         print('F')

a, b = map(int, input('두 수 입력 : ').split())
point = (a,b)

match point:
    case (10,10):
        print('정사각형')
    case (20,20):
        print('정사각형')
    case (10,20)|(20,10):
        print('직사각형')
    case _:
        print('오류')