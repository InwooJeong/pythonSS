def func():
    return 10, 20

a, b = func()
print(a,b)

count = 10

# documentation strings
def docs(string):
    """
    함수명 : func
    전달인자 : string 문자열 타입으로 문자열 출력에 사용된다.
    반환값 : 없음
    func()함수에 대한 설명
    """
    print('Hello %s' %string)

print(__name__)

if __name__ == '__main__':    
    print(docs.__doc__)
    
g_count = 10

# global 영역

def outer():
    # none local 영역
    a = 100
    def func(count):  # 함수 실행 영역 / 환경
        # local 영역
        global g_count
        g_count += count
        nonlocal a
        return g_count
    return func

x = 100

def outer(y):
    def inner():
        global x
        print(x)
        nonlocal y
        print(y)  #-> nonlocal
        y += 10
        x += y
    return inner()
    
outer(100)
print(x)