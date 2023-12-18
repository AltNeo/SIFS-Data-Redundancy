import os
import shutil
import zipfile
import filecmp

def extract_zip(zip_file, extract_to):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall(extract_to)

def delete_file(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
        print(f"Deleted: {file_path}")

def move_folder(source, destination):
    shutil.move(source, destination)
    print(f"Moved: {source} to {destination}")

def compare_folders(folder1, folder2):
    dcmp = filecmp.dircmp(folder1, folder2)
    return dcmp.diff_files

def list_files_in_folder(folder):
    file_list = []
    for root, dirs, files in os.walk(folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_list.append(file_path)
    return file_list


zip_file_path = 'path/to/your/archive.zip'
extract_folder_path = 'path/to/extract/folder'
destination_folder = 'path/to/move/folder'


extract_zip(zip_file_path, extract_folder_path)

delete_file(zip_file_path)

if os.path.exists(extract_folder_path) and os.path.exists(destination_folder):
    move_folder(extract_folder_path, destination_folder)

extract_zip(zip_file_path, extract_folder_path)

files_list = list_files_in_folder(extract_folder_path)


with open('file_list.txt', 'w') as txt_file:
    for file_path in files_list:
        txt_file.write(f"{file_path}\n")


different_files = compare_folders(destination_folder, extract_folder_path)
print("Different Files:")
for file in different_files:
    print(file)


def find_duplicates(source_folder, destination_folder):
    duplicate_files = set()

    for root, dirs, files in os.walk(source_folder):
        for file in files:
            source_file_path = os.path.join(root, file)
            dest_file_path = os.path.join(destination_folder, os.path.relpath(source_file_path, source_folder))

            if os.path.exists(dest_file_path) and filecmp.cmp(source_file_path, dest_file_path):
                duplicate_files.add(file)

    return duplicate_files

def browse_button(entry_var):
    folder_selected = filedialog.askdirectory()
    entry_var.set(folder_selected)

def compare_folders_and_display_result():
    source_folder = source_folder_entry.get()
    destination_folder = destination_folder_entry.get()

    if not source_folder or not destination_folder:
        result_text.delete(1.0, tk.END)
        result_text.insert(tk.END, "Please select both source and destination folders.")
        return

    duplicates = find_duplicates(source_folder, destination_folder)

    result_text.delete(1.0, tk.END)
    if duplicates:
        result_text.insert(tk.END, "Duplicate Files:\n")
        for file in duplicates:
            result_text.insert(tk.END, f"{file}\n")
    else:
        result_text.insert(tk.END, "No duplicate files found.")


root = tk.Tk()
root.title("Duplicate File Finder")


source_folder_label = tk.Label(root, text="Source Folder:")
source_folder_label.grid(row=0, column=0, sticky=tk.E)
source_folder_var = tk.StringVar()
source_folder_entry = tk.Entry(root, textvariable=source_folder_var, width=50)
source_folder_entry.grid(row=0, column=1)
source_folder_button = tk.Button(root, text="Browse", command=lambda: browse_button(source_folder_var))
source_folder_button.grid(row=0, column=2)


destination_folder_label = tk.Label(root, text="Destination Folder:")
destination_folder_label.grid(row=1, column=0, sticky=tk.E)
destination_folder_var = tk.StringVar()
destination_folder_entry = tk.Entry(root, textvariable=destination_folder_var, width=50)
destination_folder_entry.grid(row=1, column=1)
destination_folder_button = tk.Button(root, text="Browse", command=lambda: browse_button(destination_folder_var))
destination_folder_button.grid(row=1, column=2)
compare_button = tk.Button(root, text="Compare Folders", command=compare_folders_and_display_result)
compare_button.grid(row=2, column=0, columnspan=3)
result_text = tk.Text(root, height=10, width=60)
result_text.grid(row=3, column=0, columnspan=3)
root.mainloop()
