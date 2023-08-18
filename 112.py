import os
import shutil

from_dir = "/path/to/Downloads"
to_dir = "/path/to/Document_Files"
extensions_list = ['.txt', '.doc', '.docx', '.pdf']

list_of_files = os.listdir(from_dir)

for file_name in list_of_files:
    name, extension = os.path.splitext(file_name)
    
    if extension == '':
        continue
    
    if extension in extensions_list:
        path1 = os.path.join(from_dir, file_name)
        path2 = os.path.join(to_dir, extension[1:])  # Remove the dot from extension
        path3 = os.path.join(path2, file_name)
        
        if not os.path.exists(path2):
            os.makedirs(path2)
        
        print(f"Moving '{file_name}' to '{path3}'")
        shutil.move(path1, path3)

print("Sucessfully moved!")
