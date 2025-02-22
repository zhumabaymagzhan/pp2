#Task1
def generate_squares(n):
    for i in range(n):
        yield i ** 2
n = int(input())
for square in generate_squares(n):
    print(square)

#Task2
def even_nums(n):
    for i in range(n):
        if i % 2 == 0 :
            yield i

n = int(input())
even_numbers = list(even_nums(n))
print(", ".join(map(str, even_numbers)))

#Task3
def divisible_by_3_and_4(n):
    for num in range(n + 1):
        if num % 3 == 0 and num % 4 == 0:
            yield num

n = int(input("Enter a number: "))

result = list(divisible_by_3_and_4(n))
print(result)

#Task4
def squares(a, b):
    for num in range(a, b + 1):
        yield num ** 2

a = int(input("Enter the starting number (a): "))
b = int(input("Enter the ending number (b): "))

print("The squares of numbers from", a, "to", b, "are:")
for square in squares(a, b):
    print(square)

#Task5
def countdown(n):
    while n >= 0:
        yield n
        n -= 1

n = int(input("Enter a number: "))

print("Counting down from", n, "to 0:")
for number in countdown(n):
    print(number)
