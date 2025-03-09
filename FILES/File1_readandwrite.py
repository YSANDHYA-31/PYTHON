# file read and write permissions

import os

# Function to check file permissions
def check_permissions(file_path):
    if os.path.exists(file_path):  # Check if file exists
        print(f"Checking permissions for: {file_path}")
        
        # Check read permission
        if os.access(file_path, os.R_OK):
            print("File has READ permission.")
        else:
            print("File does NOT have READ permission.")
        
        # Check write permission
        if os.access(file_path, os.W_OK):
            print("File has WRITE permission.")
        else:
            print("File does NOT have WRITE permission.")
    else:
        print("File does not exist.")

# Provide the file path here
file_path = "test.txt"  # Change this to the file you want to check
check_permissions(file_path)
