import os

folder = input("Enter folder path: ")
size_mb = int(input("Minimum file size (MB): "))

limit = size_mb * 1024 * 1024

for root, dirs, files in os.walk(folder):
    for file in files:
        path = os.path.join(root, file)
        size = os.path.getsize(path)

        if size > limit:
            print(f"{path} - {size / (1024*1024):.2f} MB")