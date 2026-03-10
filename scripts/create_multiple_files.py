import os

folder = input("Enter folder path: ")
prefix = input("Enter file prefix: ")
count = int(input("How many files to create: "))
ext = input("Extension (example: .txt): ")

os.makedirs(folder, exist_ok=True)

for i in range(1, count + 1):
    filename = f"{prefix}_{i}{ext}"
    path = os.path.join(folder, filename)

    with open(path, "w") as f:
        f.write("")

    print("Created:", path)