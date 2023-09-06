names = ('홍길동','이순신','강감찬')
print(type(names))

namesIter = iter(names)     #생성자 iterrator 타입 객체를 생성
print(type(namesIter))

# print(namesIter.__next__())
# print(namesIter.__next__())
# print(namesIter.__next__())      # print(next(namesIter)) -> 인자로 전달된 namesIter의 __next__()를 호출하고 그 반환값을 반환
# print(namesIter.__next__()) -> StopIteration 예외

# 시퀀스 타입이면 모두 __iter__() 를 가지고 있어서 iterrator 타입 생성 가능

for name in namesIter:          # names를 주면 __iter__()를 호출, iterrator 객체 반환
    print(name)         # 다 돌아서 에러가 발생하는 순간 for문 종료

namesIter = iter(names)         # iterrator는 1회성

for name in namesIter:
    print(name)
    
# iterrable type -> list, str, range, tuple, dictionary
class MyIter:
    def __iter__(self):
        return self
# for로 돌릴 수 있음