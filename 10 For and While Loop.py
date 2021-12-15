# For Loop
numbers = [1, 2, 3, 4, 5, 67, 89, 100]
# It prints the number in loop format
for x in numbers:
    print(x)
    # It breaks the number after 67 from the list
    if x == 67:
        break
    # It skipped 4 and continued
    if x == 4:
        continue
    print(x)

# Example of for loop
x = "Fruits"
for a in x:
    print(a)

# It prints the range from accepted value
# We can also customize it like (40, 100)
for x in range(100):
    print(x)

# While Loop
i = 1
while i < 6:
    print(i)
    i += 1

# Breaking the loop
i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

# Continuing the loop
i = 1
while i < 6:
    i += 1
    if i == 3:
        continue
    print(i)

# Some Examples
fruits = ["apple", "banana", "cherry"]
for x in fruits:
    if x == "banana":
        print(x)

for x in range(6):
    print(x)
