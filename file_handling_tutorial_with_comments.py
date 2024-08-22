
'''
File Handling in Python - A Basic Tutorial with Comments
This file demonstrates the basic concepts of file handling in Python, including:
1. Opening and Closing Files
2. Reading Files
3. Writing to Files
4. Appending to Files
5. Using 'with' for File Handling
6. Working with File Paths
'''

# 1. Opening and Closing Files
# Open a file for reading (default mode)
file = open('example.txt', 'r')
# Perform file operations
# Close the file
file.close()

# 2. Reading Files
# Reading the entire file content
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# Reading line by line
with open('example.txt', 'r') as file:
    for line in file:
        print(line.strip())

# 3. Writing to Files
# Writing to a file (overwrites if the file exists)
with open('example.txt', 'w') as file:
    file.write("Hello, World!\n")
    file.write("This is a new file.")

# 4. Appending to Files
# Appending to a file (adds content to the end of the file)
with open('example.txt', 'a') as file:
    file.write("\nAppending this line.")

# 5. Using 'with' for File Handling
# The 'with' statement ensures that the file is properly closed after its suite finishes, even if an exception is raised.
with open('example.txt', 'r') as file:
    content = file.read()
    print(content)

# 6. Working with File Paths
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
