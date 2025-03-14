filename = input("Enter the filename: ")
with open(filename, 'r') as file:
    lines = file.readlines()
print(f"Number of lines: {len(lines)}")
