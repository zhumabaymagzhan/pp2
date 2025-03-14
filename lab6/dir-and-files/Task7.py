src = input("Enter the source filename: ")
dest = input("Enter the destination filename: ")
with open(src, 'r') as source_file:
    content = source_file.read()
with open(dest, 'w') as dest_file:
    dest_file.write(content)
print(f"Contents have been copied from {src} to {dest}.")
