
# Advanced OOP in Python - A Detailed Tutorial

This tutorial covers advanced Object-Oriented Programming (OOP) concepts in Python. Below is a description of key concepts with code examples.

## 1. Class Methods and Static Methods

- **Instance methods** operate on instances of the class.
- **Class methods** operate on the class itself, not on an instance.
- **Static methods** are utility functions that belong to the class but don't access class or instance attributes.

```python
class MyClass:
    class_variable = "I am a class variable"

    def instance_method(self):
        return f"This is an instance method. Variable: {self.class_variable}"

    @classmethod
    def class_method(cls):
        return f"This is a class method. Class variable: {cls.class_variable}"

    @staticmethod
    def static_method():
        return "This is a static method."
```

Usage:

```python
obj = MyClass()
print(obj.instance_method())   # Output: This is an instance method. Variable: I am a class variable
print(MyClass.class_method())  # Output: This is a class method. Class variable: I am a class variable
print(MyClass.static_method()) # Output: This is a static method.
```

## 2. Special Methods (Magic Methods)

Special methods (also called magic methods) allow you to define how objects of your class behave with respect to built-in operations.

```python
class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag

    def __str__(self):
        return f"{self.real} + {self.imag}i"

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

    def __eq__(self, other):
        return self.real == other.real and self.imag == other.imag
```

Usage:

```python
c1 = ComplexNumber(3, 2)
c2 = ComplexNumber(1, 7)
c3 = c1 + c2  # Calls the __add__ method
print(c3)     # Output: 4 + 9i
print(c1 == c2)  # Calls the __eq__ method; Output: False
```

## 3. Operator Overloading

Operator overloading allows you to define how operators behave with objects of your class. The above `ComplexNumber` example demonstrates overloading the `+` and `==` operators using `__add__` and `__eq__`.

## 4. Inheritance and Method Resolution Order (MRO)

Inheritance allows a class to inherit methods and attributes from a parent class. MRO determines the order in which methods are resolved when a class inherits from multiple parents.

```python
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

hybrid = Hybrid()
print(hybrid.speak())  # Output: Dog barks (MRO prioritizes Dog over Cat)
print(Hybrid.__mro__)  # Outputs the MRO for the Hybrid class
```

## 5. Abstract Base Classes (ABC)

Abstract Base Classes (ABC) are classes that cannot be instantiated and are meant to be subclassed. They enforce that certain methods must be implemented by the subclass.

```python
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
```

Usage:

```python
rect = Rectangle(4, 7)
print(f"Area: {rect.area()}")         # Output: Area: 28
print(f"Perimeter: {rect.perimeter()}") # Output: Perimeter: 22
```

This concludes the advanced tutorial on OOP in Python. Practice these concepts to deepen your understanding.
