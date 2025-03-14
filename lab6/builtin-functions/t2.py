text = input("Enter string: ")
upper_count = sum(1 for c in text if c.isupper())
lower_count = sum(1 for c in text if c.islower())

print(f"Uppercase: {upper_count}")
print(f"Lowercase: {lower_count}")
