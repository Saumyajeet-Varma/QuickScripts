import os

folder = input("Enter folder path: ")
ext = input("Extension to count (example: .txt): ")

count = 0

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(ext):
            count += 1

print(f"Total {ext} files:", count)