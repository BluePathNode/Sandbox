import os # import teh os
import json # Import the Json
import platform # Import the platform module to identify the operating system
import webbrowser # Import the webbrowser module to open URLs in the user's default web browser

#---------------------------------------------------------------------------------------------------------------
# This file will output an html template based on whats stored in the companion JSON file HtmlTemplateDict.json
# Contains a help section 
# User can store some templates and have this script output them faster than just writing it out? idk maybe
#--------------------------------------------------------------------------------------------------------

# Define the path to the HtmlTemplateDict.json file
template_dict_path = 'HtmlTemplateDict.json'

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
/add -b     Batch add from a folder
/del        Delete a template
/view       View a template in console
/view -o    View a template in the default browser
/cls        Clears the console
/quit       Exit script
'''

def load_dict():
    """Load the dictionary from HtmlTemplateDict.json."""   
    if not os.path.isfile(template_dict_path):  # Check if the JSON file exists
        return {}  # Return an empty dictionary if the file does not exist 
    try:
        with open(template_dict_path, "r") as file: # Open the JSON file in read mode  
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
    with open(template_dict_path, "w") as file:  # Open the file in write mode
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

def add_template(template, batch_mode=False, folder_path=None):  # Define the function to add templates
    """Add templates from files to the dictionary."""  # Docstring to describe the function
    
    # Batch mode: walk through the directory and add each template
    if batch_mode:  # Check if batch_mode is enabled
        if folder_path and os.path.isdir(folder_path):  # Check if folder_path is valid and is a directory
            for root, dirs, files in os.walk(folder_path):  # Walk through the folder
                for file in files:  # Loop through each file in the directory
                    if file.endswith(".html") or file.endswith(".css"):  # Check if the file is an HTML or CSS file
                        template_name, ext = os.path.splitext(file)  # Split the file name and extension
                        full_file_path = os.path.join(root, file)  # Get the full file path

                        try:
                            with open(full_file_path, "r", encoding="utf-8") as f:  # Open the file with utf-8 encoding
                                content = f.read()  # Read the content of the file

                            # Determine whether to store HTML or CSS content
                            if ext == ".html":  # If the file is an HTML file
                                if template_name not in template:  # If template doesn't already exist
                                    template[template_name] = {"html": content, "css": None}  # Add HTML with no CSS
                                else:  # If template already exists
                                    template[template_name]["html"] = content  # Update HTML content only
                            elif ext == ".css":  # If the file is a CSS file
                                if template_name not in template:  # If template doesn't already exist
                                    template[template_name] = {"html": None, "css": content}  # Add CSS with no HTML
                                else:  # If template already exists
                                    template[template_name]["css"] = content  # Update CSS content only

                            print(f"Added {file} as {template_name}")  # Notify user the template was added
                        except FileNotFoundError:  # Catch if the file wasn't found
                            print(f"File not found: {full_file_path}")  # Print an error for missing files
                        except UnicodeDecodeError:  # Catch if there is a character encoding error
                            print(f"Error reading file: {full_file_path}")  # Print an error for reading files

            save_template(template)  # Save the updated template dictionary
            print("Batch adding complete.")  # Notify user that batch adding is done
        else:
            print(f"Invalid directory: {folder_path}")  # Print an error if the folder path is invalid
        return  # Exit the function

    # Single template mode (existing behavior)
    html_path = input("Enter the HTML file path:>")  # Get the HTML file path from the user
    css_path = input("Enter the CSS file path (leave blank if none):>")  # Get the CSS file path, if applicable
    template_name = input("Enter the template name:>")  # Get the template name from the user

    if not os.path.isfile(html_path):  # Check if the HTML file exists
        print("!" * 50)  # Print separator for emphasis
        print(f"{html_path} is not valid")  # Notify user of invalid file path
        print(path_error_text)  # Display the error message for invalid paths
        print("!" * 50)  # Print separator for emphasis
        return  # Exit the function if the file path is invalid

    try:
        with open(html_path, "r", encoding="utf-8") as html_file:  # Open the HTML file in utf-8 encoding
            html_content = html_file.read()  # Read the HTML content
            
            css_content = None  # Initialize CSS content as None
            if css_path and os.path.isfile(css_path):  # Check if CSS file path is valid and exists
                with open(css_path, "r", encoding="utf-8") as css_file:  # Open the CSS file in utf-8 encoding
                    css_content = css_file.read()  # Read the CSS content
            elif css_path:  # If the CSS path was provided but the file doesn't exist
                print(f"CSS file {css_path} not found.")  # Notify user that CSS file is missing

            # Add the HTML and CSS content to the template dictionary
            template[template_name] = {
                "html": html_content,  # Store the HTML content
                "css": css_content  # Store the CSS content or None if no CSS provided
            }
            save_template(template)  # Save the updated template dictionary
            print(f"Template named '{template_name}' has been created.")  # Notify user that the template is created
    except FileNotFoundError:  # Catch if the HTML or CSS file wasn't found
        print("File not found. Please check the file path.")  # Print error message for missing file
    except UnicodeDecodeError:  # Catch if there's an encoding issue
        print(f"Error reading file {template_name}, it may contain special characters.")  # Print error for decoding issue
        
def list_templates(template):
    """List all available templates."""
    template_list = "\n".join([key for key in template.keys()]) # Generate a list of template names
    print("-" * 30) # Print a separator
    print(template_list) # Print the list of templates
    print("-" * 30) # Print a separator

def view_template(template, open_in_browser=False):
    """View a template and optionally open in a browser."""
    
    # Ask the user for the template name they want to view
    template_name = input("Enter the name of the template to view (use /list to see available templates):> ")
    
    # Check if the template exists in the dictionary
    if template_name in template:
        # Get the HTML content from the template dictionary for the selected template
        html_content = template[template_name]["html"]
        # Get the CSS content, defaulting to "No CSS content available" if there is none
        css_content = template[template_name].get("css", "No CSS content available.")
        
        # Handle browser opening logic
        if open_in_browser:  # If open_in_browser is True, open the template in a web browser
            try:
                # Define a temporary file path for the HTML file to be opened in the browser
                temp_html_path = "temp_template.html"
                
                # Open the temporary HTML file for writing, using UTF-8 encoding
                with open(temp_html_path, "w", encoding="utf-8") as file:
                    # Write the HTML content from the template to the file
                    file.write(html_content)
                    
                # Open the newly created temporary HTML file in the default web browser
                webbrowser.open(f"file://{os.path.abspath(temp_html_path)}")
                # Notify the user that the template was opened in the browser
                print(f"Template opened in browser: {temp_html_path}")
            except IOError as e:
                # Handle any file I/O errors and notify the user if opening the file failed
                print(f"Error opening file in browser: {e}")
        else:
            # If not opening in the browser, print the template content to the console
            print("-" * 30)  # Print a divider line
            print(f"Content of {template_name}")  # Print the template name
            print("HTML Content:")  # Label for HTML content
            print(html_content)  # Output the HTML content of the template
            print("CSS Content:")  # Label for CSS content
            print(css_content)  # Output the CSS content of the template (if available)
            print("-" * 30)  # Print another divider line 
    elif template_name == "/list":
        # If the user inputs "/list", call a function to list all available templates
        list_templates(template)
    else:
        # If the template name is not found in the dictionary, notify the user
        print(f"Template '{template_name}' not found.")

def clear_screen():
    system = platform.system() # Get the name of the operating system (e.g., "Windows", "Linux", "Darwin" for macOS)
    if system == 'Windows': # Check if the OS is Windows
        os.system('cls') # Use 'cls' command to clear the console on Windows 
    else: # If the OS is not Windows 
        os.system('clear') # Use 'clear' command to clear the console on macOS/Linux
        
def main():
    # The amount of elifs in this block is too damn high 
    template = load_dict()

    while True:  # Run an infinite loop for user input
        print("Enter a template name (case sensitive) or type /help")  # Prompt the user for a command or template name
        entry = input(":>")  # Get the user's input
        
        if entry == "/list":  # Check if the user wants to list templates
            list_templates(template)
            
        elif entry == "/help":  # Check if the user wants help
            print("-" * 50)  # Print a separator
            print(help_text)  # Print the help text
            print("-" * 50)  # Print a separator
         
        elif entry == "/quit":  # Check if the user wants to quit
            print("Quitting..")  # Print a quitting message
            break  # Exit the loop

        elif entry.startswith("/add"):  # Check if the user input starts with "/add" command
            if "-b" in entry:  # Check for batch mode (-b flag)
                folder_path = input("Enter the folder path for batch adding templates:> ")  # Get folder path
                add_template(template, batch_mode=True, folder_path=folder_path)  # Call add_template in batch mode
            else:
                add_template(template)  # Call add_template in regular mode
            
        elif entry == "/del":  # Check if the user wants to delete a template
            delete_template(template)  # Call the delete_template function
            
        elif entry.startswith("/view"):  # Check if the user input starts with the "/view" command
            if "-o" in entry:  # Check for the Open in Browser flag ("-o") in the user input
                view_template(template, open_in_browser=True) # Call view_template with open_in_browser set to True to open the template in a browser
            else:
                view_template(template) # If no "-o" flag is present, call view_template to just display the template in the console
           
           
            
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
