import os

path = input("Enter folder path: ")

for root, dirs, files in os.walk(path, topdown=False):
    for d in dirs:
        folder = os.path.join(root, d)
        if not os.listdir(folder):
            os.rmdir(folder)
            print("Deleted empty folder:", folder)