class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

numbers = [5, 2 ,4, 7 ,3]
print(all(number >= 1 for number in numbers))

persons = [Person('홍길동',20),Person('심청이',16),Person('에디슨',55)]
#Persons 리스트의 모든 Person 객체 연령이 19세 이상?
print(all(p.age >= 19 for p in persons))
print(any(p.age >= 30 for p in persons))
print('Hello'.encode().decode())