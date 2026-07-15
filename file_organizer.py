import os
import shutil

path = input("Enter folder path: ")

# Create folders
folders = {
    ".txt": "Text Files",
    ".pdf": "PDF Files",
    ".py": "Python Files"
}

for folder in folders.values():
    os.makedirs(os.path.join(path, folder), exist_ok=True)

# Organize files
for file in os.listdir(path):

    file_path = os.path.join(path, file)

    # Skip folders
    if not os.path.isfile(file_path):
        continue

    # Move files based on extension
    for extension, folder in folders.items():
        if file.endswith(extension):
            shutil.move(file_path, os.path.join(path, folder, file))
            print(f"Moved: {file} -> {folder}")
            break

print("Done!")
