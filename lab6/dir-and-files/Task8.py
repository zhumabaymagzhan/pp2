import os

path = input("Enter the file path to delete: ")
if os.path.exists(path) and os.access(path, os.W_OK):
    os.remove(path)
    print(f"The file {path} has been deleted.")
else:
    print("File does not exist or you lack permission to delete it.")
