import json

file_path = "C:\\Users\\jumab\\Downloads\\sample-data.json"

with open(file_path, "r", encoding="utf-8") as file:
    data = json.load(file)

print("Interface Status")
print("=" * 80)
print("{:<50} {:<15} {:<10} {:<10}".format("DN", "Description", "Speed", "MTU"))
print("-" * 80)

for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes["dn"]
    descr = attributes["descr"] if attributes["descr"] else "N/A"
    speed = attributes["speed"]
    mtu = attributes["mtu"]

    print("{:<50} {:<15} {:<10} {:<10}".format(dn, descr, speed, mtu))
