# OOP Exercise: Building a Simple Library System

**Objective**: Create a simple library system that manages books and their authors.

## Requirements

1. **Create Classes**:
   - **Book**: Represents a book in the library.
     - Attributes: `title`, `author`, `year_published`
     - Methods: `get_info()` that returns a string with book details.

   - **Author**: Represents an author.
     - Attributes: `name`, `birth_year`
     - Methods: `get_bio()` that returns a string with author details.

2. **Encapsulation**:
   - Ensure that the attributes of the classes are private (use double underscores for private attributes).
   - Provide public methods to access and modify these attributes.

3. **Inheritance**:
   - Create a class **EBook** that inherits from **Book**.
     - Additional Attribute: `file_size` (in MB)
     - Override the `get_info()` method to include the file size.

4. **Polymorphism**:
   - Define a method **print_book_info()** that takes a **Book** object (or its subclass) and prints its information. It should work for both **Book** and **EBook** instances.

5. **Abstraction**:
   - Create an abstract class **LibraryItem** that defines an abstract method `get_details()`. Both **Book** and **EBook** should inherit from **LibraryItem** and implement this method.

## Implementation Steps

1. **Define the Classes**:

   ```python
   from abc import ABC, abstractmethod

   class LibraryItem(ABC):
       @abstractmethod
       def get_details(self):
           pass

   class Author:
       def __init__(self, name, birth_year):
           self.__name = name
           self.__birth_year = birth_year

       def get_bio(self):
           return f"Author: {self.__name}, Born: {self.__birth_year}"

   class Book(LibraryItem):
       def __init__(self, title, author, year_published):
           self.__title = title
           self.__author = author
           self.__year_published = year_published

       def get_info(self):
           return f"Title: {self.__title}, Author: {self.__author.get_bio()}, Year: {self.__year_published}"

       def get_details(self):
           return self.get_info()

   class EBook(Book):
       def __init__(self, title, author, year_published, file_size):
           super().__init__(title, author, year_published)
           self.__file_size = file_size

       def get_info(self):
           return f"Title: {self.__title}, Author: {self.__author.get_bio()}, Year: {self.__year_published}, File Size: {self.__file_size} MB"
    ```



