import os # import teh os
import json # Import the Json
import platform # Import the platform module to identify the operating system

#---------------------------------------------------------------------------------------------------------------
# This file will output an html template based on whats stored in the companion JSON file HtmlTemplateDict.json
# Contains a help section 
# User can store some templates and have this script output them faster than just writing it out? idk maybe
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
/add        Add a template from file
/del        Delete a template
/view       View a template in console
/cls        Clears the console
/quit       Exit script
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
    """Add a template from files to the dictionary."""
    html_path = input("Enter the HTML file path:>")  # Get the HTML file path from the user
    css_path = input("Enter the CSS file path (leave blank if none):>")  # Get the CSS file path from the user, optional
    template_name = input("Enter the template name:>")  # Get the template name from the user   
    
    if not os.path.isfile(html_path):  # Check if the HTML file exists
        print("!" * 50)  # Print a separator
        print(f"{html_path} is not valid")  # Print the invalid file path message
        print(path_error_text)  # Print the path error text
        print("!" * 50)  # Print a separator
        return  # Exit the function       

    try:
        with open(html_path, "r", encoding="utf-8") as html_file:  # Open the HTML file in read mode with UTF-8 encoding
            html_content = html_file.read()  # Read the content of the HTML file
            
            css_content = None
            if css_path and os.path.isfile(css_path):  # Check if a CSS file path was provided and if it exists
                with open(css_path, "r", encoding="utf-8") as css_file:  # Open the CSS file
                    css_content = css_file.read()  # Read the content of the CSS file
            elif css_path:
                print(f"CSS file {css_path} not found.")  # Inform the user if the CSS file was not found
            
            template[template_name] = {
                "html": html_content,
                "css": css_content
            }  # Add the new template to the dictionary
            save_template(template)  # Save the updated dictionary to the file
            print(f"Template named '{template_name}' has been created.")  # Print confirmation message                  
    except FileNotFoundError:
        print("File not found. Please check the file path.")  # Print an error message if the file is not found
    except UnicodeDecodeError:
        print(f"Error reading file {template_name} may contain special characters")  # Print error message if file contains unsupported characters

def list_templates(template):
    """List all available templates."""
    template_list = "\n".join([key for key in template.keys()]) # Generate a list of template names
    print("-" * 30) # Print a separator
    print(template_list) # Print the list of templates
    print("-" * 30) # Print a separator

def view_template(template):
    """View a template."""
    template_name = input("Enter the name of the template to view (use /list) \n :>")  # Input the template name, might need to use /list first 
    if template_name in template:
        print("-" * 30)  # Print a separator
        print(f"Content of {template_name}")  # Print the template name
        print("HTML Content:")
        print(template[template_name]["html"])  # Print the content of the HTML template
        print("CSS Content:")
        print(template[template_name].get("css", "No CSS content available."))  # Print the content of the CSS template if available
        print("-" * 30)  # Print a separator
    elif template_name == "/list":
        list_templates(template)  # Call list_templates function to show available templates
    else:
        print(f"Template '{template_name}' not found.")  # Inform the user if the template was not found
        
def clear_screen():
    
    system = platform.system() # Get the name of the operating system (e.g., "Windows", "Linux", "Darwin" for macOS)
    if system == 'Windows': # Check if the OS is Windows
        os.system('cls') # Use 'cls' command to clear the console on Windows 
    else: # If the OS is not Windows 
        os.system('clear') # Use 'clear' command to clear the console on macOS/Linux
        
def main():
    """Main function to interact with user."""
    template = load_dict()  # Load the dictionary from the file

    while True:
        print("Enter a template name (case sensitive) or type /help")  # Prompt the user for input
        
        entry = input(":>")  # Get user input
        
        if entry == "/list":  # Check if the user wants to list templates
            list_templates(template)
            
        elif entry == "/help":  # Check if the user wants help
            print("-" * 50)  # Print a separator
            print(help_text)  # Print the help text
            print("-" * 50)  # Print a separator
         
        elif entry == "/quit":  # Check if the user wants to quit
            print("Quitting..")  # Print a quitting message
            break  # Exit the loop

        elif entry == "/add":  # Check if the user wants to add a template
            add_template(template)  # Call the add_template function
            template = load_dict()  # Reload the dictionary after adding the new template
            
        elif entry == "/del":  # Check if the user wants to delete a template
            delete_template(template)  # Call the delete_template function
            
        elif entry == "/view":  # Check if the user wants to view a template
            view_template(template)  # Call the view_template function
            
        elif entry == "/cls":
            clear_screen()

        elif entry in template:  # Check if the user input matches a template name
            html_filename = input("Enter the name of the HTML file (Example: filename.html)\n:>")  # Name the HTML output file
            css_filename = input("Enter the name of the CSS file (Example: filename.css) or leave blank\n:>")  # Name the CSS output file, if any
            
            if isinstance(template[entry], dict):  # Ensure entry is a dictionary
                html_content = template[entry].get("html")  # Get the content of the HTML template
                css_content = template[entry].get("css")  # Get the content of the CSS template, if available
                
                if html_content:
                    with open(html_filename, "w") as html_file:  # Open the HTML file in write mode
                        html_file.write(html_content)  # Write the HTML content to the file
                        print(f"HTML template '{entry}' has been written to {html_filename}.")  # Print confirmation message
                
                if css_content and css_filename:
                    with open(css_filename, "w") as css_file:  # Open the CSS file in write mode
                        css_file.write(css_content)  # Write the CSS content to the file
                        print(f"CSS for template '{entry}' has been written to {css_filename}.")  # Print confirmation message
                elif not css_filename:
                    print("No CSS file specified, skipping CSS output.")
            else:
                print(f"Template '{entry}' does not have valid content.")  # Inform the user if the template content is not valid
        else:
            print("Please enter a valid template or command")  # Print an error message for invalid input

if __name__ == "__main__":
    main()  # Call the main function if the script is run directly
