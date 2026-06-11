# all thing in python is an object(class) and we can create our own class and object in python
# that why we called python as a object oriented programming language   

# class is a blueprint of object and object is an instance of class

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
        
student1 = Student("John", 20)
print(student1.name)  # Output: John
print(student1.age)   # Output: 20

