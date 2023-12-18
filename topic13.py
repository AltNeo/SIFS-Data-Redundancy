import os
import zipfile
import tarfile

def extract_zip(zip_file, extract_to):
  """
  Extracts files from a ZIP archive, skipping encrypted files.

  Args:
      zip_file: Path to the ZIP archive file.
      extract_to: Path to the directory where extracted files will be saved.
  """
  with zipfile.ZipFile(zip_file, 'r') as zip_ref:
    for file_info in zip_ref.infolist():
      if file_info.flag_bits & 0x01:  # Check if file is encrypted
        print(f"Skipping encrypted file: {file_info.filename}")
      else:
        zip_ref.extract(file_info, extract_to)

def extract_tar_gz(tar_gz_file, extract_to):
  """
  Extracts files from a tar.gz archive and saves a list of files to a text file.

  Args:
      tar_gz_file: Path to the tar.gz archive file.
      extract_to: Path to the directory where extracted files will be saved.
  """
  with tarfile.open(tar_gz_file, 'r:gz') as tar_ref:
    tar_ref.extractall(extract_to)

    # List extracted files and save to a text file
    tar_gz_file_list = list_files_in_folder(extract_to)
    with open(os.path.join(extract_to, 'tar_gz_file_list.txt'), 'w') as txt_file:
      txt_file.write(f"Total files: {len(tar_gz_file_list)}\n")
      for file in tar_gz_file_list:
        txt_file.write(f"{file}\n")

def list_files_in_folder(folder):
  """
  Lists all files recursively within a directory.

  Args:
      folder: Path to the directory to be scanned.

  Returns:
      A list of file paths within the directory and its subdirectories.
  """
  file_list = []
  for root, dirs, files in os.walk(folder):
    for file in files:
      file_path = os.path.join(root, file)
      file_list.append(file_path)
  return file_list

def extract_recursive(zip_file_path, extract_folder_path):
  """
  Extracts files recursively from nested ZIP archives within a main ZIP archive.

  Args:
      zip_file_path: Path to the ZIP archive file.
      extract_folder_path: Path to the directory where extracted files will be saved.
  """
  extract_zip(r'C:\Users\Jasmine\Downloads\topic12.zip'
,r'C:\Users\Jasmine\Downloads\ABC')

  # List extracted files and check for nested ZIP files
  files_list = list_files_in_folder(r'C:\Users\Jasmine\Downloads\ABC')
  for file_path in files_list:
    _, extension = os.path.splitext(file_path.lower())

    # Extract nested ZIP archives recursively
    if extension == ".zip":
      extract_recursive(file_path, os.path.join(r'C:\Users\Jasmine\Downloads\ABC', os.path.splitext(os.path.basename(file_path))[0]))

    # Handle other archive formats if needed (add separate functions)

# Replace the placeholder paths in the "Example usage" section!
main_zip_file_path = r'C:\Users\Jasmine\Downloads\topic12.zip'

main_extract_folder_path = "path/to/extract/folder"

if __name__ == "__main__":
  extract_recursive(r'C:\Users\Jasmine\Downloads\topic12.zip'
, r'C:\Users\Jasmine\Downloads\ABC')
