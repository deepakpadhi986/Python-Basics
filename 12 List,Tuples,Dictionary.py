# List
"""It is used to store multiple items in single variables"""
# ordered,changeable, Square Brackets and allow duplicates
print("list")

list = ["car", 'Bike', 30, 40, 3.0, True, 'Bike']

print(list)

print(len(list))

print(type(list))

print(list[0])

print(list[5])

print(list[2:5])

print(list[2:])

print(list[:5])

# Change

list[2] = "Scooters"

print(list)

list[1:3] = ["Scooters", "Watermelons"]

print(list)

# Insert

list.insert(3, "Jeep")

print(list)

# Add

list.append("Oranges")

print(list)

""" Tuples """
# ordered, unchangeable, Circle brackets and allow duplicates
print("Tuples")

tuple = ("car", 'Jeep', 30, 40, 3.0, True, 'Bike')

print(tuple)

print(len(tuple))

print(type(tuple))

print(tuple[0])

print(tuple[2:5])

print(tuple[2:])

print(tuple[:5])

print(tuple[-1])

""" Dictionaries """
# Unordered, changeable, curly brackets, and Do not allow Duplicate Values
print("Dictionaries")
dictt = {
    "name": "Raj",
    "age": 26,
    "Phone": 1231233211,
    "Role": "Student",
    "vehicle": "Ford Endeavour",
    "DOB": "12-12-12",
    "Fruits": ["Apples", "Oranges", "Pineapples", "Blueberries"]
}

print(dictt)

print(len(dictt))

print(type(dictt))

x = dictt["vehicle"]
print(x)

# another way
x = dictt.get("name")
print(x)

# Change the value of the key
dictt["vehicle"] = "Bike"
print(dictt)

# Update
dictt.update({"name": "prakash"})
print(dictt)

# Add
dictt["colour"] = "Blue"
print(dictt)

# Remove
dictt.pop("Fruits")
print(dictt)


""" Example """
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": "1964"
}

# another to get the value
print(car.get("model"))

car["year"] = 2020
print(car)
