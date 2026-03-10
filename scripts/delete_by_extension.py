import os

folder = input("Enter folder path: ")
ext = input("Enter file extension (example: .txt): ")

deleted = 0

for root, dirs, files in os.walk(folder):
    for file in files:
        if file.endswith(ext):
            path = os.path.join(root, file)
            os.remove(path)
            print("Deleted:", path)
            deleted += 1

print(f"\nTotal files deleted: {deleted}")