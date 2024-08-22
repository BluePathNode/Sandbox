
'''
Advanced OOP in Python - A Detailed Tutorial with Comments
This file demonstrates advanced concepts of Object-Oriented Programming (OOP) in Python, including:
1. Class Methods and Static Methods
2. Special Methods (Magic Methods)
3. Operator Overloading
4. Inheritance and Method Resolution Order (MRO)
5. Abstract Base Classes (ABC)
'''

# 1. Class Methods and Static Methods
class MyClass:
    # Class attribute
    class_variable = "I am a class variable"

    # Instance method
    def instance_method(self):
        return f"This is an instance method. Variable: {self.class_variable}"

    # Class method (using @classmethod decorator)
    @classmethod
    def class_method(cls):
        return f"This is a class method. Class variable: {cls.class_variable}"

    # Static method (using @staticmethod decorator)
    @staticmethod
    def static_method():
        return "This is a static method."

# Creating an instance
obj = MyClass()

# Calling methods
print(obj.instance_method())  # Output: This is an instance method. Variable: I am a class variable
print(MyClass.class_method())  # Output: This is a class method. Class variable: I am a class variable
print(MyClass.static_method())  # Output: This is a static method.

# 2. Special Methods (Magic Methods)
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    # Overriding the __str__ method to define the string representation
    def __str__(self):
        return f"{self.real} + {self.imag}i"

    # Overriding the __add__ method to add two complex numbers
    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    # Overriding the __eq__ method to compare two complex numbers
    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag

# Creating complex numbers
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)

# Using the overridden methods
print(c1)  # Output: 3 + 2i
print(c2)  # Output: 1 + 7i

c3 = c1 + c2  # Calls the __add__ method
print(c3)  # Output: 4 + 9i

print(c1 == c2)  # Calls the __eq__ method; Output: False

# 3. Operator Overloading
# The above example of ComplexNumber already demonstrates operator overloading.
# You can override other operators like __sub__ (for -), __mul__ (for *), __truediv__ (for /), etc.

# 4. Inheritance and Method Resolution Order (MRO)
class Animal:
    def speak(self):
        return "Animal speaks"

class Dog(Animal):
    def speak(self):
        return "Dog barks"

class Cat(Animal):
    def speak(self):
        return "Cat meows"

class Hybrid(Dog, Cat):
    pass

# Creating an instance of Hybrid
hybrid = Hybrid()
print(hybrid.speak())  # Output: Dog barks (Method Resolution Order prioritizes Dog over Cat)

# Checking the MRO
print(Hybrid.__mro__)  # Output: (<class '__main__.Hybrid'>, <class '__main__.Dog'>, <class '__main__.Cat'>, <class '__main__.Animal'>, <class 'object'>)

# 5. Abstract Base Classes (ABC)
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)

# Cannot instantiate Shape because it's an abstract class
# shape = Shape()  # This would raise an error

# Creating an instance of Rectangle
rect = Rectangle(4, 7)
print(f"Area: {rect.area()}")  # Output: Area: 28
print(f"Perimeter: {rect.perimeter()}")  # Output: Perimeter: 22
