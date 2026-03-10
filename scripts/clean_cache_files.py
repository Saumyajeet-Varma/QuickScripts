import os

folder = input("Enter folder path: ")

extensions = [".log", ".tmp", ".cache"]

deleted = 0

for root, dirs, files in os.walk(folder):
    for file in files:
        if any(file.endswith(ext) for ext in extensions):
            path = os.path.join(root, file)
            os.remove(path)
            print("Deleted:", path)
            deleted += 1

print("Total deleted:", deleted)