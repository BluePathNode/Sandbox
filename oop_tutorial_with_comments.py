
'''
OOP in Python - A Basic Tutorial with Comments
This file demonstrates the basic concepts of Object-Oriented Programming (OOP) in Python, including:
1. Class and Object creation
2. Instance and Class Attributes
3. Encapsulation
4. Inheritance
5. Polymorphism
6. Special Methods
'''

# 1. Defining a Class
class Dog:
    # Class attribute shared by all instances
    species = "Canis familiaris"

    # Initializer / Instance attributes
    def __init__(self, name, age):
        # Instance attributes unique to each instance
        self.name = name
        self.age = age

    # Instance method
    def bark(self):
        # Returns a string that includes the name of the dog
        return f"{self.name} says woof!"


# 2. Creating Objects (Instances)
dog1 = Dog("Buddy", 3)
dog2 = Dog("Lucy", 5)

# Access instance attributes
print(dog1.name)  # Output: Buddy
print(dog2.age)   # Output: 5

# Call instance method
print(dog1.bark())  # Output: Buddy says woof!


# 3. Instance Attributes vs. Class Attributes
print(dog1.species)  # Output: Canis familiaris
print(dog2.species)  # Output: Canis familiaris

# You can change the class attribute
Dog.species = "Canis lupus"
print(dog1.species)  # Output: Canis lupus
print(dog2.species)  # Output: Canis lupus


# 4. Encapsulation
class DogEncapsulated:
    def __init__(self, name, age):
        # Private attributes with double underscores
        self.__name = name
        self.__age = age

    # Public method to access private attributes
    def get_name(self):
        return self.__name

    # Public method to modify private attributes
    def set_name(self, name):
        self.__name = name

# Accessing private attributes using methods
dog_encapsulated = DogEncapsulated("Buddy", 3)
print(dog_encapsulated.get_name())  # Output: Buddy


# 5. Inheritance
# Bulldog inherits from Dog
class Bulldog(Dog):
    # Overriding the bark method
    def bark(self):
        return f"{self.name} says gruff!"

bulldog = Bulldog("Bully", 4)
print(bulldog.bark())  # Output: Bully says gruff!


# 6. Polymorphism
def make_dog_bark(dog):
    # Calls the bark method of any Dog object
    print(dog.bark())

make_dog_bark(dog1)    # Output: Buddy says woof!
make_dog_bark(bulldog) # Output: Bully says gruff!


# 7. Special Methods
class DogWithStr:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    # Special method to return a string representation of the object
    def __str__(self):
        return f"{self.name} is {self.age} years old."

dog_with_str = DogWithStr("Buddy", 3)
print(dog_with_str)  # Output: Buddy is 3 years old.
