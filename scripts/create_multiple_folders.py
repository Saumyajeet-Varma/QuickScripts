import os

base = input("Enter base path: ")
prefix = input("Folder name prefix: ")
count = int(input("How many folders: "))

for i in range(1, count + 1):
    folder = os.path.join(base, f"{prefix}_{i}")
    os.makedirs(folder, exist_ok=True)
    print("Created:", folder)