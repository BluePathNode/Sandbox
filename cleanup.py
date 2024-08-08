import os
import shutil

# Define the file type categories and their corresponding extensions
file_categories = {
    "pdf": ["pdf"],
    "image": ["jpg", "jpeg", "png", "gif", "bmp", "tiff", "svg"],
    "exe": ["exe", "bat", "bin", "msi"],
    "video": ["mp4", "mkv", "flv", "avi", "mov", "wmv"],
    "audio": ["mp3", "wav", "aac", "flac", "ogg", "wma"],
    "compressed": ["zip", "rar", "7z", "tar", "gz"],
    "text": ["txt", "doc", "docx", "odt", "rtf", "tex", "md"],
    "misc": []
}

def sanitize_path(path):
    """Encode the path to handle special characters and long paths."""
    if not path.startswith('\\\\?\\'):
        return f'\\\\?\\{os.path.normpath(path)}'
    return path

def gather_files(target_directory):
    # Ensure the target directory exists
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)
    
    # Walk through the directory tree starting from the script's location
    script_directory = os.path.dirname(os.path.abspath(__file__))
    print(f"Script directory: {script_directory}")
    
    for root, dirs, files in os.walk(script_directory, topdown=False):
        for file in files:
            # Skip the script itself
            if file == os.path.basename(__file__):
                continue
            
            # Get the file extension
            file_extension = file.split('.')[-1].lower() if '.' in file else 'no_extension'
            
            # Determine the category for the file extension
            category = "misc"
            for cat, extensions in file_categories.items():
                if file_extension in extensions:
                    category = cat
                    break
            
            # Create a directory for the category if it doesn't exist
            category_dir = os.path.join(target_directory, category)
            if not os.path.exists(category_dir):
                os.makedirs(category_dir)
            
            # Move the file to the directory for its category
            src_path = os.path.join(root, file)
            dest_path = os.path.join(category_dir, file)
            try:
                src_path_sanitized = sanitize_path(src_path)
                dest_path_sanitized = sanitize_path(dest_path)
                if not os.path.exists(src_path_sanitized):
                    print(f"File not found: {src_path_sanitized}")
                    continue
                shutil.move(src_path_sanitized, dest_path_sanitized)
                print(f"Moved: {src_path_sanitized} -> {dest_path_sanitized}")
            except FileNotFoundError:
                print(f"FileNotFoundError: The system cannot find the file specified: {src_path}")
            except PermissionError:
                print(f"PermissionError: Permission denied for {src_path} or {dest_path}")
            except Exception as e:
                print(f"Error moving {src_path} -> {dest_path}: {e}")
        
        # Remove empty directories
        for dir in dirs:
            dir_path = os.path.join(root, dir)
            try:
                os.rmdir(dir_path)
                print(f"Removed empty directory: {dir_path}")
            except OSError:
                pass

if __name__ == "__main__":
    # Ask the user for the target directory
    target_directory = input("Please enter the full path to the target directory: ")
    target_directory_sanitized = sanitize_path(target_directory)
    
    gather_files(target_directory_sanitized)
