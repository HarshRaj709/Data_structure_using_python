'''
1. Class
2.Attributes ----> Data
3.Objects
4.Class Object
5. __init__() method
6. Types of method
7. Types of variables
'''

#Encapsulation :- An act of combining properties and methods related to same object is known as Encapsulation.
# Class is a way to implement Encapsulation.

#Function is also called attribute in python


# 1 class has exactly 1 class Object but can have any number of instance objects.
#    Test ---> class Object
#    Test() ---> instance object


# class Person:

#     x= 10                           #class Object variable

#     def __init__(self,name='harsh',age=0):        
#         self.name = name           #attribute name  Here name is a local variable whereas self.a is instance variable
#         self.age = age

#     def show(self):
#         print(f'Age is {self.age} and name is {self.name}')

# t1 = Person('harsh',30)         #here t1 will be pass in place of self 
# t1.show()
# t2 = Person()
# t2.show()


# Types of methods in class

# Instance Methods: Operate on instances of the class, taking self as their first argument.

# Class Methods: Operate on the class itself, taking cls as their first argument. They can modify class state that applies across all 
# instances.

# Static Methods: Operate without reference to either the instance (self) or the class (cls). They are used as utility functions that 
# don't depend on class or instance state.


# class Person:

#     classobject = 100

#     def __init__(self,value):           #instance method        Instance methods are primarily used to read or modify the object's state.
#         self.value = value
#         print(f'this is instance method and have value {self.value}')

#     @staticmethod       #dont take any arguments either self,cls        No need to create instance for them
#     def add(x,y):
#         print(f'Addition is {x+y}')
#         # return x+y
    
#     @classmethod
#     def class_method(cls):      #take cls as first argument             No need to create instance for them
#         print(f'the class had class object {cls.classobject}')
    

# t1 = Person(45)             #this is instance method
# t2 = Person.add(4,5)             # no need to create instance
# t3 = Person.class_method()       # no need to create instance




# #       Example and use cases of each Method type

# ### Instance Methods

# #1.Manipulating Instance Data:Instance methods are primarily used to read or modify the object's state.
# class BankAccount:
#        def __init__(self, balance):
#            self.balance = balance

#        def deposit(self, amount):
#            self.balance += amount

#        def withdraw(self, amount):
#            if amount <= self.balance:
#                self.balance -= amount
#            else:
#                print("Insufficient funds")

#        def get_balance(self):
#            return self.balance

# account = BankAccount(100)
# account.deposit(50)
# print(account.get_balance())  # Output: 150

# #2.Interacting with Other Instances:Instance methods can interact with other instances of the same class.
# class Person:
#        def __init__(self, name):
#            self.name = name

#        def greet(self, other_person):
#            return f"Hello, {other_person.name}! My name is {self.name}."

# alice = Person("Alice")
# bob = Person("Bob")
# print(alice.greet(bob))  # Output: Hello, Bob! My name is Alice.

# ### Class Methods

# #1.Factory Methods:Class methods can be used to create alternative constructors.
# class Date:
#        def __init__(self, year, month, day):
#            self.year = year
#            self.month = month
#            self.day = day

#        @classmethod
#        def from_string(cls, date_string):
#            year, month, day = map(int, date_string.split('-'))
#            return cls(year, month, day)

# date = Date.from_string("2023-07-08")
# print(date.year, date.month, date.day)  # Output: 2023 7 8

# #2.Modifying Class State:Class methods can modify the state that is shared across all instances.
   
# class Employee:
#        raise_amount = 1.05

#        def __init__(self, name, salary):
#            self.name = name
#            self.salary = salary

#        @classmethod
#        def set_raise_amount(cls, amount):
#            cls.raise_amount = amount

#        def apply_raise(self):
#            self.salary *= self.raise_amount

# Employee.set_raise_amount(1.10)
# emp = Employee("John", 50000)
# emp.apply_raise()
# print(emp.salary)  # Output: 55000.0


# ### Static Methods

# #1.Utility Functions:Static methods can be used as utility functions that don't need access to class or instance data.
# class MathUtils:
#        @staticmethod
#        def add(x, y):
#            return x + y

#        @staticmethod
#        def subtract(x, y):
#            return x - y

# print(MathUtils.add(5, 3))       # Output: 8
# print(MathUtils.subtract(5, 3))  # Output: 2

# #2.Encapsulating Helper Functions:Static methods can encapsulate helper functions that are logically related to the class but don't operate on class or instance data.
# class StringUtils:
#        @staticmethod
#        def is_palindrome(s):
#            return s == s[::-1]

#        @staticmethod
#        def reverse_string(s):
#            return s[::-1]

# print(StringUtils.is_palindrome("radar"))  # Output: True
# print(StringUtils.reverse_string("hello"))  # Output: "olleh"



class Employee:

    def __init__(self,emp_id=None,name=None,salary=None):
        self.emp_id = emp_id
        self.name = name
        self.salary = salary
    def setEmpid(self,emp_id):
        self.emp_id = emp_id
    def setName(self,name):
        self.name = name
    def setSalary(self,salary):
        self.salary = salary
    def getEmpid(self):
        return self.emp_id
    def getName(self):
        return self.name
    def getsalary(self):
        return self.salary
    
t1 = Employee()
print(t1.getsalary())
t1.setSalary(777777)
t1.setName('Rza')
print(t1.getsalary())
print(t1.getName())
t2 = Employee(101,"harsh",72000)
print(t2.getsalary())
    