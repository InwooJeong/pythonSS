def gen():
    yield 'A'
    yield 'B'
    yield 'C'

for i in gen():
    print(i)
    
# 코루틴?