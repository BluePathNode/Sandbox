
# OOP in Python - A Basic Tutorial

This tutorial covers the fundamental concepts of Object-Oriented Programming (OOP) in Python. Below is a description of the key concepts with code examples.

## 1. Class and Object Creation

A **class** is a blueprint for creating objects. Objects are instances of classes.

```python
class Dog:
    species = "Canis familiaris"  # Class attribute

    def __init__(self, name, age):
        self.name = name            # Instance attribute
        self.age = age              # Instance attribute

    def bark(self):
        return f"{self.name} says woof!"
```

You create an object (instance) of a class like this:

```python
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)
```

## 2. Instance and Class Attributes

- **Instance attributes** are unique to each object.
- **Class attributes** are shared by all objects of the class.

Example:

```python
print(dog1.name)  # Output: Buddy
print(dog2.species)  # Output: Canis familiaris
```

## 3. Encapsulation

Encapsulation involves hiding the internal state of an object and requiring all interaction to be performed through methods.

```python
class DogEncapsulated:
    def __init__(self, name, age):
        self.__name = name  # Private attribute
        self.__age = age    # Private attribute

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name
```

## 4. Inheritance

Inheritance allows a new class to inherit attributes and methods from an existing class.

```python
class Bulldog(Dog):
    def bark(self):
        return f"{self.name} says gruff!"
```

## 5. Polymorphism

Polymorphism allows methods to behave differently based on the object calling them.

```python
def make_dog_bark(dog):
    print(dog.bark())

make_dog_bark(dog1)    # Output: Buddy says woof!
make_dog_bark(bulldog) # Output: Bully says gruff!
```

## 6. Special Methods

Special methods in Python begin and end with double underscores (e.g., `__init__`, `__str__`). They allow you to define how objects of your class behave in specific situations.

```python
class DogWithStr:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} is {self.age} years old."

dog_with_str = DogWithStr("Buddy", 3)
print(dog_with_str)  # Output: Buddy is 3 years old.
```

This concludes the basic tutorial on OOP in Python. Practice these concepts to solidify your understanding.
