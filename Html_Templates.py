import os # import teh os
import json # Import the Json
#---------------------------------------------------------------------------------------------------------------
# This file will output an html template based on whats stored in the companion JSON file HtmlTemplateDict.json
# Contains a help section 
# User can store some templates and have this script output them faster than just writing it out? idk maybe
# Css support Soon™️
#--------------------------------------------------------------------------------------------------------

# Define the path to the HtmlTemplateDict.json file
dict_path = 'HtmlTemplateDict.json'

# Define error message for invalid file paths
path_error_text = '''
Please check the file path.
A correct file path will include the file name. 
Example: C:\\Users\\User\\Documents\\your_file_name.html
'''

# Define help text for user commands
help_text = '''
/list       List of available templates
/quit       Exit script
/add        Add a template from file
/del        Delete a template
/view       View a template in console
'''

def load_dict():
    """Load the dictionary from HtmlTemplateDict.json."""   
    if not os.path.isfile(dict_path):  # Check if the JSON file exists
        return {}  # Return an empty dictionary if the file does not exist 
    try:
        with open(dict_path, "r") as file: # Open the JSON file in read mode  
            return json.load(file) # Try to load the content of the file as a dictionary
    except json.JSONDecodeError as e: # Catch any JSON decoding errors
        print(f"Error loading JSON data: {e}") # Print the error message with details of the exception
        save_template({}) # Save an empty dictionary to create a new file
        return {} # Return an empty dictionary if a decoding error occurs
    except Exception as e: # Catch the unknown
        print(f"Error loading JSON data: {e}") # Print the error message
        save_template({}) # Save an empty dictionary to create a new file
        return {} # Return an empty dictionary

def save_template(template_dict):
    """Save the dictionary to HtmlTemplateDict.json."""
    with open(dict_path, "w") as file:  # Open the file in write mode
        json.dump(template_dict, file, indent=4) # Write the dictionary to the file in a JSON format

def delete_template(template):
    """Delete an existing template."""
    template_name = input("Enter the name of the template to delete:>") # Prompt user for the template name to delete
    if template_name in template: # Check if the template exists in the dictionary
        del template[template_name] # Remove the template from the dictionary
        print(f"{template_name} has been deleted.") # Inform the user that the template has been deleted
        save_template(template) # Save the updated dictionary back to the file       
    else:
        print(f"{template_name} not found.") # Inform the user if the template was not found

def add_template(template):
    """Add a template from a file to the dictionary."""
    filepath = input("Enter the file path:>")  # Get the file path from the user
    template_name = input("Enter the template name:>")  # Get the template name from the user   
    if not os.path.isfile(filepath): # Check if the file exists
        print("!" * 50) # Print a separator
        print(f"{filepath} is not valid") # Print the invalid file path message
        print(path_error_text) # Print the path error text
        print("!" * 50) # Print a separator
        return # Exit the function       
    try:
        with open(filepath, "r", encoding="utf-8") as file: # Open the file in read mode with UTF-8 encoding
            file_content = file.read() # Read the content of the file
            print(f"Content read from file:\n{file_content}") # Print the file content
            template[template_name] = file_content # Add the new template to the dictionary
            save_template(template) # Save the updated dictionary to the file
            print(f"Template named '{template_name}' has been created.") # Print confirmation message                  
    except FileNotFoundError:
        print("File not found. Please check the file path.") # Print an error message if the file is not found
    except UnicodeDecodeError:
        print(f"Error reading file {template_name} may contain special characters") # Print error message if file contains unsupported characters

def view_template(template):
    """View a template."""
    template_name = input("Enter the name of the template to view (use /list) \n :>") # Input the template name, might need to use /list first 
    if template_name in template:
        print("-" * 30) # Print a separator
        print(f"Content of {template_name}") # Print the template name
        print(template[template_name]) # Print the content of the specified template
        print("-" * 30) # Print a separator
    elif template_name == "/list":
        list_templates(template) # Call list_templates function to show available templates
    else:
        print(f"Template '{template_name}' not found.") # Inform the user if the template was not found

def list_templates(template):
    """List all available templates."""
    template_list = "\n".join([key for key in template.keys()]) # Generate a list of template names
    print("-" * 30) # Print a separator
    print(template_list) # Print the list of templates
    print("-" * 30) # Print a separator

def main():
    """Main function to interact with user."""
    # The 'template' variable holds the dictionary of templates loaded from the JSON file.
    # It is passed as a parameter to functions that need to access or modify the template data.
    template = load_dict() # Load the dictionary from the file

    while True:
        print("Enter a template name (case sensitive) or type /help") # Prompt the user for input
        
        entry = input(":>") # Get user input
        filename = entry + ".html" # Construct the filename
        
        if entry == "/list": # Check if the user wants to list templates
            list_templates(template)
            
        elif entry == "/help": # Check if the user wants help
            print("-" * 50) # Print a separator
            print(help_text) # Print the help text
            print("-" * 50) # Print a separator
         
        elif entry == "/quit": # Check if the user wants to quit
            print("Quitting..") # Print a quitting message
            break # Exit the loop

        elif entry == "/add": # Check if the user wants to add a template
            add_template(template) # Call the add_template function
            template = load_dict() # Reload the dictionary after adding the new template
            
        elif entry == "/del": # Check if the user wants to delete a template
            delete_template(template) # Call the delete_template function
            
        elif entry == "/view": # Check if the user wants to view a template
            view_template(template) # Call the view_template function

        elif entry in template: # Check if the user input matches a template name
            html_content = template[entry] # Get the content of the selected template
            
            with open(filename, "w") as file: # Open the file in write mode
                file.write(html_content) # Write the template content to the file
                print(f"Template '{entry}' has been written to {filename}.") # Print confirmation message
            
        else:
            print("Please enter a valid template or command") # Print an error message for invalid input

if __name__ == "__main__":
    main() # Call the main function if the script is run directly
