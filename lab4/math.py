import math

#Task1
degree = int(input("Input degree: "))
radian = degree * math.pi / 180
print(f"Output radian: {radian:.6f}")

#Task2
height =  int(input("Height: "))
first_val = int(input("Base, first value: "))
second_val = int(input("Base, second value: "))

s = 1/2 * (first_val + second_val) * height

print(f"Expected Output: {s}")

#Task3
n = int(input("Input number of sides: "))
len = int(input("Input the length of a side: "))

polygon = (len**2 * n) / 4 * math.tan(math.pi/n)

print(f"The area of the polygon is: {polygon:.2f}")

#Task4 
len = int(input("Length of base: "))
hei = int(input("Height of parallelogram: "))

area = len * hei

print(f"Expected Output: {area:.1f}")