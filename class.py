class Person:
    
    __slots__ = ['__name','__age','major']
    
    def __init__(self, name='홍길동',age=20):
        self.__name = name
        self.__age = age
        
    def show(self):
        print(f"이름 : {self.__name}, 연령 : {self.__age}")
        
    def showInfo():
        pass
        
    def __str__(self):
        return f"이름 : {self.__name}, 연령 : {self.__age}"
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value
        
    @property   
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value >= 19:
            self.__age = value          # 직접 접근 시 못 했던 평가가 가능
        else:
            print("나이는 19 이상") 

class MyClass:
    pass     
        
# person = Person('심청이',16)
# person.show()

myClass = MyClass()         # 생성자 기술하지 않으면 디폴트 생성자
print(myClass)

# p = Person('홍길동',20)
# p.major = '도둑'
# p1 = Person('심청이',16)
# p1.age = -1                       # 들어가서는 안되는 값 - 직접 접근의 문제점 __ -> private
# print(p.name, p.age, p.major)     # private 이후 접근 불가 - person 클래스를 활용한 캡슐화
# print(p1.name, p1.age, p1.major)          # 객체 통일성 X

# 접근 불가 - 멤버가 무의미 -> 외부에서 name, age에 접근이 가능 해야함 -> 접근 이유 data get/set

p = Person('홍길동',20)
p.name = '심청이'       # p의 name setter를 찾음
p.age = 20
print(p)
print(p.name)

# p.major 문제
p.major = '도둑'
print(p)

# p.show()
# print(p.__str__())
# print(isinstance(p, Person))
# print(isinstance(p, object))

# 파이썬 최초 객체는 멤버가 없음 -> 객체 생성
# 객체 생성 후 멤버 공간을 할당하고 값을 넣는다. -> 초기화