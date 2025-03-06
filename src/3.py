class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

student1 = Student("John", 25)
student2 = Student("Jane", 30)

print(student1.greet()) # Output: Hello, my name is John
print(student2.greet()) # Output: Hello, my name is Jane
