import os
import hashlib

folder = input("Enter folder path: ")

hashes = {}

for root, dirs, files in os.walk(folder):
    for file in files:
        path = os.path.join(root, file)

        with open(path, "rb") as f:
            file_hash = hashlib.md5(f.read()).hexdigest()

        if file_hash in hashes:
            os.remove(path)
            print("Deleted duplicate:", path)
        else:
            hashes[file_hash] = path