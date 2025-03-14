from functools import reduce

nums = list(map(int, input("Enter numbers: ").split()))
result = reduce(lambda x, y: x * y, nums)
print(f"Product: {result}")
