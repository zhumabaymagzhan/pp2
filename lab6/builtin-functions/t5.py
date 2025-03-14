data = tuple(map(bool, map(int, input("Enter 0 and/or 1 separated by spaces: ").split())))
print(f"Are all elements true? {all(data)}")
