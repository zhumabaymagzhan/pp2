import json

txt_file = "C:\\Users\\jumab\\Downloads\\row.txt"

with open(txt_file, "r", encoding="utf-8") as file:
    lines = file.readlines()

products = []
i = 0
while i < len(lines):
    line = lines[i].strip()

if line.isdigit() or line.endswith("."):
    item_number = line.replace(".", "")
    name = lines[i + 1].strip()  
    quantity_price = lines[i + 2].strip()  
    total_price = lines[i + 3].strip()  

    if i + 4 < len(lines) and "Стоимость" in lines[i + 4]:
        i += 1 

    parts = quantity_price.split(" x ")
    if len(parts) == 2:
        quantity, price_per_unit = parts
    else:
        quantity, price_per_unit = "N/A", "N/A"

    price_per_unit = price_per_unit.replace(" ", "")
    total_price = total_price.replace(" ", "")

    products.append({
        "№": item_number,
        "Название": name,
        "Кол-во": quantity,
        "Цена за шт": price_per_unit,
        "Стоимость": total_price
    })


    i += 1

print("{:<5} {:<100} {:<10} {:<15} {:<10}".format("№", "Название", "Кол-во", "Цена за шт", "Стоимость"))
print("=" * 100)

for item in products:
    print("{:<5} {:<100} {:<10} {:<15} {:<10}".format(item["№"], item["Название"], item["Кол-во"], item["Цена за шт"], item["Стоимость"]))
