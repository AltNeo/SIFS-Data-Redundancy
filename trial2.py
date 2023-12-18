import os
import zipfile

def extract_zip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def list_files_in_folder(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def extract_files_from_zip(zip_file_path, extract_folder_path):
    extract_zip(zip_file_path, extract_folder_path)

def print_files_in_folder(folder_path):
    files_list = list_files_in_folder(folder_path)
    for file_path in files_list:
        print(file_path)

# Customize the file and folder names
zip_file_name = 'salesAnalysisReport.zip'
extract_folder_name = 'shakti'

# Get user input for the zip file path
zip_file_path = input("Enter the path to the zip file: ")

# Get user input for the extract folder path
extract_folder_path = input("Enter the path to the extract folder: ")

# Extract files from the zip archive
extract_files_from_zip(zip_file_path, extract_folder_path)

# List all files in the extracted folder recursively
print_files_in_folder(extract_folder_path)