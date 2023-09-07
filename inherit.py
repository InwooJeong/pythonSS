from abc import ABCMeta,abstractmethod

class Person(metaclass=ABCMeta):
    def __init__(self,name,age):
        self._name = name               #protected _
        self._age = age         
        print("Call Person()")
        
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self,value):
        self._name = value
        
    @property
    def age(self):
        return self._age
    
    @age.setter
    def age(self,value):
        self._age = value
    
    @abstractmethod    
    def showinfo(self):
        pass    
        
class Student(Person):
    def __init__(self,name,age,major):
        super().__init__(name,age)
        self.__major = major
        print("Call student()")
        
    @property
    def major(self):
        return self.__major
    
    @major.setter
    def major(self,value):
        self.__major = value    
        
    def show(self):
        print(f"{self._name,self._age,self.__major}")
    
    @staticmethod    
    def staticshow(obj):
        #print("call static method")
        return Student(obj._name,obj._age,obj.__major)
    
    @classmethod    
    def clone(cls,obj):
        return cls(obj._name,obj._age,obj.__major)
    
    def showinfo(self):
        self.show()             # delegating
    
class Employee(Person):
    def __init__(self):
        print("Call Employee()")
    
    def showinfo(self):
        return super().showinfo()   
        
# p = Person('심청이', 16)
s = Student('홍길동', 20, '전산')
e = Employee()

# s.show()
s.showinfo()
# print(s._name)

# Student.staticshow()
s2 = Student.clone(s)
s3 = Student.staticshow(s)
# print(id(s),type(s))
# print(id(s2),type(s2))
# print(id(s3),type(s3))

# print(isinstance(p,Person))
# print(isinstance(p,object))
# print(isinstance(s,Student))
# print(isinstance(s,Person))
# print(isinstance(s,object))
# print(isinstance(e,Employee))
# print(isinstance(e,Person))
# print(isinstance(e,object))