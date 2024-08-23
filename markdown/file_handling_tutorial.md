
# File Handling in Python - A Basic Tutorial

This tutorial covers the fundamental concepts of file handling in Python. Below is a description of the key concepts with code examples.

## 1. Opening and Closing Files

You can open a file using the `open()` function. It’s important to close the file after you are done with it to free up system resources.

```python
file = open('example.txt', 'r')  # Open for reading
file.close()                     # Close the file
```

## 2. Reading Files

You can read the content of a file using various methods like `read()` and `readlines()`.

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

To read a file line by line:

```python
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())
```

## 3. Writing to Files

You can write to a file using the `write()` method. This will overwrite the existing content of the file.

```python
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.")
```

## 4. Appending to Files

To append content to an existing file without overwriting it, use the `'a'` mode.

```python
with open('example.txt', 'a') as file:
    file.write("\nAppending this line.")
```

## 5. Using 'with' for File Handling

Using the `with` statement is the recommended way to handle files, as it ensures that files are properly closed even if an error occurs.

```python
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)
```

## 6. Working with File Paths

Python's `os` module provides utilities to interact with the file system, such as working with file paths.

```python
import os

# Get the current working directory
current_directory = os.getcwd()
print(f"Current Directory: {current_directory}")

# Join paths in a platform-independent way
file_path = os.path.join(current_directory, 'example.txt')
print(f"File Path: {file_path}")

# Check if a file exists
if os.path.exists(file_path):
    print(f"The file {file_path} exists.")
else:
    print(f"The file {file_path} does not exist.")
```

This concludes the basic tutorial on file handling in Python. Practice these concepts to solidify your understanding.
