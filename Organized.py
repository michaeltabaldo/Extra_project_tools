import os
import shutil

# Get the directory where the script is located
script_directory = os.path.dirname(__file__)

# Define the source folder where scattered files are located (use the script's directory)
source_folder = script_directory

# Define the destination folder where organized files will be placed
destination_folder = 'C:/Path/To/Your/Destination/Folder'

# Create the main destination folder if it doesn't exist
if not os.path.exists(destination_folder):
    os.makedirs(destination_folder)

# Function to move files to their respective folders based on file extension
def organize_files(source_folder, destination_folder):
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip if it's a directory
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Create a folder for the file extension if it doesn't exist
        extension_folder = os.path.join(destination_folder, file_extension)
        if not os.path.exists(extension_folder):
            os.makedirs(extension_folder)

        # Move the file to the appropriate folder
        destination_path = os.path.join(extension_folder, filename)
        shutil.move(source_path, destination_path)

# Organize the files
organize_files(source_folder, destination_folder)

# Rename folders based on types (file extensions)
for folder_name in os.listdir(destination_folder):
    folder_path = os.path.join(destination_folder, folder_name)
    if os.path.isdir(folder_path):
        # Get the folder's file extension (without the dot)
        extension = folder_name.lstrip('.').upper()
        
        # Rename the folder based on the extension
        new_folder_name = f"{extension} Files"
        new_folder_path = os.path.join(destination_folder, new_folder_name)
        os.rename(folder_path, new_folder_path)

print("Files have been organized and folders have been renamed.")
