def func():
    print('A')
    print('B')
    print('C')

func()

def func(name,age):
    print(f"이름 : {name}, 연령 : {age}")
    
func("redStreet",20)

def printPerson(person):  # 덮어 씌워짐
    pass

def printPerson(name = '홍길동', age = 20):  # 오버로딩 대신 디폴트 파라미터 지원
    pass

printPerson()
printPerson('홍길동')
printPerson('홍길동',20)
printPerson(age = 20, name='에디슨')  # 키워드 파라미터

def func(*args):  # 가변인자 파라미터 -> 넘어온 가변인자들을 하나의 튜플로 묶어버림(패킹)
    print(args)
    print(len(args))
    print('---------------------------------------')
    
func()
func('one')
func('one','two')

a = (10,)  # 요소가 하나라면 반드시 뒤에 콤마 -> 안하면 튜플이 아닌 식을 감싸는 괄호

names = ['홍길동','이순신','심청이']
func(*names)  # 언패킹

def func(**kwargs):
    print(kwargs)
    print(len(kwargs))
    if 'name' in kwargs:
        print(kwargs['name'])
    else:
        print("name 키가 없습니다.")
    
func()
func(one=1)
func(one=1, two=2)

person = {'name':'hong','age':20}
func(**person)  # ==> 키=값

def func(*args, **kwargs):
    print(args)
    print(kwargs)

func(20,20,30,one=1,two=2,three=3)

person={'name':'gil','age':20}
func(**person)

print('작업 종료')