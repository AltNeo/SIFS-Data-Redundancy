# Project 12 Data Redundancy Remover
Team CodeFlipper's Submission for SIF Hackathon 

The problem statement requires that we develop a program (with GUI) where user can quickly compare a new folder against a database of existing folders. The GUI has to provide the user a comprehensive list of files that are found to be duplicates and give the user an option to delete the files (from new or old files) or the entire folder if needed.

Our solution hashes (CRC32 and SHA256, depending on number of files) every file in the directory and subdirectory and stores it in a dictionary (and also exports it into a csv to build a database). It then checks it against another dictionary to find same hash in other directory. 
It then forwards this data to the GUI for an easier interpretation giving user an option to delete the file or keep it and/or delete the entire folder if necessary

### How to use
Install necessary libraries 
Just run the notebook and enter the two folder paths.

### GUI Representation
https://www.figma.com/file/w1rHRhFSKlhnCANLpo4PaW/SIFS?type=design&node-id=0%3A1&mode=design&t=jpEOtCU5USDCNIW2-1

### Working Features: 
Scanning files and subdirectories
Creating lists and dictionaries for comparisons.
Exporting dictionaries for later reference
Currently, our code compares only two folders, scanning against a complete database will be implemented soon.
Hashing functions: Both CRC32 and SHA256 are working.
Exporting filename-hash dictionary
Comparing hashes and listing duplicate files. (GUI integration pending)

### Features Yet to be implemented: 
Scanning against a complete database.
GUI Integration

### Explaination
The solution comprises of following steps: 
1. Taking in input from user about two folders. (This can be changed later so that only one folder is compared to all existing folders, or just to compare two folders). This will be done through GUI.
2. The program will then make a list of all files and subdirectories and store it in a list.
3. The program will then look for any .tar.gz and .zip files or any other compressed files and then extract them in their own folders.
4. We again repeat Step 2 and 3 until there are no more compressed archives left in the folder. (When comparing two folders, we repeat the same process again for the second folder)
5. We then create a checksum hash, can find duplicates even when file names aren’t same (can be CRC32 or SHA256 chosen by user based on required level of accuracy and speed). 
i)CRC32 is good for faster hashing, but can lead to duplicate hashes after 2^32 files.
ii)SHA256 is good for larger number of files but can take longer to create hashes.
6.These hashes are then saved in  a dictionary, corresponding to their respective filenames.
7. For permanent storage, these dictionaries can be exported as CSV files and later read when necessary. 
8. We then create functions for fetching file details if a match is found.
9. We create a comparing function that looks through the hash dictionaries (can be optimised in later stages) to find a duplicate.
10. The duplicates found are then sent to the GUI for interpretation and evaluation.
11. The admin can then decide on which file to keep and it will be updated in the respective dictionary.
12. Once satisfied, the admin can click submit and the changes will be applied.



