# this script will write a set of html templates from a dictionary HtmlTemplateDict
# comes with a help section just run 

# css support soon™️ 
import os
import json
from HtmlTemplateDict import template  # Import the existing template dictionary

# Define the path to the HtmlTemplateDict.py file
dict_path = 'HtmlTemplateDict.py'

# Define error message for invalid file paths
path_error_text = '''
Please check the file path.
A correct file path will include the file name. 
Example: C:\\Users\\User\\Documents\\your_file_name.html
'''

# Define help text for user commands
help = '''
/list       List of available templates
/quit       Exit script
/add        Add a template from file
'''

def load_dict():
    """Load the dictionary from HtmlTemplateDict.py."""
    # Check if the HtmlTemplateDict.py file exists
    if not os.path.isfile(dict_path):
        return {}  # Return an empty dictionary if the file does not exist
    
    with open(dict_path, "r") as file:  # Open the file in read mode
        content = file.read()  # Read the entire content of the file
    
    try:
        # Extract the dictionary content from the file content
        # Assuming that the file contains a line of the format `template = {...}`
        start = content.find('{')  # Find the starting index of the dictionary
        end = content.rfind('}') + 1  # Find the ending index of the dictionary
        if start == -1 or end == -1:
            return {}  # Return an empty dictionary if indices are not found
        dict_content = content[start:end]  # Extract the dictionary content
        return json.loads(dict_content.replace("'", '"'))  # Convert single quotes to double quotes and parse the JSON
    except (json.JSONDecodeError, ValueError) as e:
        # Print an error message if there's an issue with JSON decoding
        print(f"Error loading dictionary from file: {e}")
        return {}  # Return an empty dictionary on error

def save_template(template_dict):
    """Save the dictionary to HtmlTemplateDict.py."""
    with open(dict_path, "w") as file:  # Open the file in write mode
        # Write the dictionary to the file in a JSON format
        file.write(f"template = {json.dumps(template_dict, indent=4)}")

def add_template():
    """Add a template from a file to the dictionary."""
    filepath = input("Enter the file path:>")  # Get the file path from the user
    template_name = input("Enter the template name:>")  # Get the template name from the user
    
    if not os.path.isfile(filepath):  # Check if the file exists
        print("!" * 50)  # Print a separator
        print(f"{filepath} is not valid")  # Print the invalid file path message
        print(path_error_text)  # Print the path error text
        print("!" * 50)  # Print a separator
        return  # Exit the function
        
    try:
        with open(filepath, "r") as file:  # Open the file in read mode
            file_content = file.read()  # Read the content of the file
            print(f"Content read from file:\n{file_content}")  # Print the file content
            template_dict = load_dict()  # Load the existing dictionary
            template_dict[template_name] = file_content  # Add the new template to the dictionary
            save_template(template_dict)  # Save the updated dictionary to the file
            print(f"{template_name} has been added.")  # Print confirmation message
            
    except FileNotFoundError:
        # Print an error message if the file is not found
        print("File not found. Please check the file path.")

def main():
    """Main function to interact with user."""
    global template  # Use the global template variable
    template = load_dict()  # Load the dictionary from the file
    template_list = "\n".join([key.capitalize() for key in template.keys()])  # Create a list of template names
    
    while True:
        print("Enter a template name or type /help")  # Prompt the user for input
        
        entry = input(":>")  # Get user input
        filename = entry + ".html"  # Construct the filename
        
        if entry == "/list":  # Check if the user wants to list templates
            print("-" * 30)  # Print a separator
            print(template_list)  # Print the list of templates
            print("-" * 30)  # Print a separator
            
        elif entry == "/help":  # Check if the user wants help
            print("-" * 50)  # Print a separator
            print(help)  # Print the help text
            print("-" * 50)  # Print a separator
         
        elif entry == "/quit":  # Check if the user wants to quit
            print("Quitting..")  # Print a quitting message
            break  # Exit the loop

        elif entry == "/add":  # Check if the user wants to add a template
            add_template()  # Call the add_template function
            template = load_dict()  # Reload the dictionary after adding the new template
            template_list = "\n".join([key.capitalize() for key in template.keys()])  # Update the template list

        elif entry in template:  # Check if the user input matches a template name
            html_content = template[entry]  # Get the content of the selected template
            
            with open(filename, "w") as file:  # Open the file in write mode
                file.write(html_content)  # Write the template content to the file
                print(f"Template '{entry}' has been written to {filename}.")  # Print confirmation message
            
        else:
            print("Please enter a valid template or command")  # Print an error message for invalid input
                
if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
