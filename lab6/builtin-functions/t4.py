import time
import math

number = float(input("Enter a number: "))
delay = int(input("Enter delay in milliseconds: "))
time.sleep(delay / 1000)
result = math.sqrt(number)
print(f"Square root of {number} after {delay} milliseconds is {result}")
