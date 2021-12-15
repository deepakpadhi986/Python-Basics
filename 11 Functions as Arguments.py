def trial(x, y):
    print(x + " " + y)


trial("Hello", "There")


def my_function(fname, lname):
    print(lname + " " + fname)


my_function("Coco", "Sheth")

# Next
file = ['car', 'bus', 'bike', 'scooter']


def loop(x):
    print(x * 3)


def map_simple(crazy, crack):
    for items in crack:
        crazy(items)


map_simple(loop, file)


# Next
def my_function(food):
    for x in food:
        print(x)


fruits = ["apple", "banana", "cherry"]
my_function(fruits)


# Next
def my_function(x):
    return 5 * x


print(my_function(3))
print(my_function(5))
print(my_function(9))
