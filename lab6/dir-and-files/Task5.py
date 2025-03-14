filename = input("Enter the filename to write to: ")
items = input("Enter list items separated by spaces: ").split()
with open(filename, 'w') as file:
    for item in items:
        file.write(item + "\n")
print("List has been written to the file.")
