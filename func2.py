def func():
    return 10, 20

a, b = func()
print(a,b)

count = 10

# documentation strings
def func(string):
    """
    함수명 : func
    전달인자 : string 문자열 타입으로 문자열 출력에 사용된다.
    반환값 : 없음
    func()함수에 대한 설명
    """
    print('Hello %s' %string)

if __name__ == '___main__':    
    print(func.__doc__)