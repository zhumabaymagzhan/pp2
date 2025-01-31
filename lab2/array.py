cars = ["Ford", "Volvo", "BMW"]

x = cars[0]

cars[0] = "Toyota"

x = len(cars)

for x in cars:
  print(x)

cars.append("Honda")


cars.pop(1)


cars.remove("Volvo")

my_list = [1, 2, 3]
my_list.append(4)
print(my_list)

my_list = [1, 2, 3, 4]
my_list.clear()
print(my_list)

my_list = [1, 2, 3, 4]
new_list = my_list.copy()
print(new_list)

my_list = [1, 2, 2, 3, 4]
count = my_list.count(2)
print(count)

my_list = [1, 2, 3]
my_list.extend([4, 5])
print(my_list)

my_list = [1, 2, 3, 4]
index = my_list.index(3)
print(index)

my_list = [1, 2, 4]
my_list.insert(2, 3)
print(my_list)

my_list = [1, 2, 3, 4]
removed_element = my_list.pop(2)
print(my_list)
print(removed_element)

my_list = [1, 2, 3, 4]
my_list.remove(2)
print(my_list)

my_list = [1, 2, 3, 4]
my_list.reverse()
print(my_list)

my_list = [4, 2, 3, 1]
my_list.sort()
print(my_list)
