def decorate(func):
    def wrapper(cnt):
        print(func.__name__,'실행 전')
        func(cnt)
        print(func.__name__,'싱행 후')
    return wrapper

@decorate
def work(cnt):
    print(f"{cnt} Working...")

# work = decorate(work)
work(10)

def decorator(func):
    def wrapper(*args, **kwargs):
        print(func.__name__,'실행 전')
        func(*args, **kwargs)
        print(func.__name__,'싱행 후')
    return wrapper

@decorator
def work(name, age):
    print(f"이름 : {name}, 나이 : {age}")

# work = decorate(work)
work('홍길동', 20)

# import time
from time import time,sleep

def decorate(original_func):
    def wrapper(*args,**kwargs):
        start=time()
        result = original_func(*args,**kwargs)
        end=time()
        print("함수 수행시간 : %f초" % (end-start))
        return result
    return wrapper

@decorate
def add(a,b):
    sleep(2)
    return a + b

result = add(3,4)
print(result)