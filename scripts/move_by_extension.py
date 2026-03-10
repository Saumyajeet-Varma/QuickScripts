import os
import shutil

source = input("Enter source folder: ")
destination = input("Enter destination folder: ")
ext = input("Enter extension (example: .jpg): ")

os.makedirs(destination, exist_ok=True)

for root, dirs, files in os.walk(source):
    for file in files:
        if file.endswith(ext):
            src_path = os.path.join(root, file)
            dst_path = os.path.join(destination, file)
            shutil.move(src_path, dst_path)
            print("Moved:", src_path)

print("Done moving files.")