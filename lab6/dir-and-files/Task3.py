import os

path = input("Enter the path: ")
if os.path.exists(path):
    print(f"Directory portion: {os.path.dirname(path)}")
    print(f"File portion: {os.path.basename(path)}")
else:
    print("The path does not exist.")
