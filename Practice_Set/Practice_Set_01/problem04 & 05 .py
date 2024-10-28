#4.write a python program to print the contents of a directory using the os module . Search online for the function which does that 
import os

def list_directory_contents(directory):
    try:
        # Get the list of files and directories in the specified directory
        contents = os.listdir(directory)
        print(f"Contents of '{directory}':")
        for item in contents:
            print(item)
    except FileNotFoundError:
        print(f"The directory '{directory}' does not exist.")
    except PermissionError:
        print(f"You do not have permission to access '{directory}'.")

# Specify the directory you want to list
directory_path = input("Enter the directory path: ")
list_directory_contents(directory_path)

#5.Label the program using the comments 