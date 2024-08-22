#  Understanding the Basics: Classes and Objects
# Class: A blueprint for creating objects. It defines a set of attributes and methods that the created objects will have.
# Object: An instance of a class. When a class is defined, no memory is allocated until an object of that class is created.
# 2. Creating a Class
# A class is defined using the class keyword

class Dog:
    # Class Attribute
    species = "Canis lupus familiaris"

    # Initializer / Instance Attributes
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    # Instance method
    def bark(self):
        return f"{self.name} says woof!"



# Class Attribute: species is a class attribute shared by all instances of the Dog class.
# Instance Attributes: name and age are instance attributes unique to each object (instance) of the class.
# Initializer (__init__): The __init__ method is a special method that initializes the instance attributes. It is called when a new object is created.
# Instance Method: bark is an instance method that acts upon an object’s data.



# Creating Objects
#You can create an object by calling the class as if it were a function:

# dog1 = Dog("Buddy", 3)
# dog2 = Dog("Milo", 5)

# print(dog1.name)  # Output: Buddy
# print(dog2.age)   # Output: 5
