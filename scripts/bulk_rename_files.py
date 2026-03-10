import os

folder = input("Enter folder path: ")
prefix = input("New file prefix: ")

files = os.listdir(folder)

for i, file in enumerate(files, start=1):
    old_path = os.path.join(folder, file)

    if os.path.isfile(old_path):
        ext = os.path.splitext(file)[1]
        new_name = f"{prefix}_{i}{ext}"
        new_path = os.path.join(folder, new_name)

        os.rename(old_path, new_path)
        print(f"{file} -> {new_name}")