import os

def list_files_with_paths(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list

def write_file_paths_to_text(file_paths, output_file):
    with open(output_file, 'w') as txt_file:
        for file_path in file_paths:
            txt_file.write(f"{file_path}\n")

# Example usage:
folder_path = "/mnt/088/seeq1"
output_text_file = "file_paths.txt"

# List all files in the folder with full paths
files_with_paths = list_files_with_paths(folder_path)

# Write file paths to a text file
write_file_paths_to_text(files_with_paths, output_text_file)
