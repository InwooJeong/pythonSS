def func():
    return 10

func = lambda : 10

def func(x):
    return x*x

func = lambda x : x*x
print(func(10))

def max(a,b):
    if a>b:
        return a
    else:
        return b
    
value = (lambda a, b : a if a > b else b)(10,20)  # 재사용 목적이 아님

print(value)

def func(callback, a, b):
    return callback(a, b)

value = func(lambda x, y: x if x > y else y,30,40)
value2 = func(lambda x, y: x if x < y else y,30,40)
print(value)
print(value2)