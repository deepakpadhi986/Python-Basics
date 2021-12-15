your_name = "This is the variable of the string"
print(your_name)

your_name1 = """This the Variable of 
Multiple type
 string"""
print(your_name1)

a = "python"
b = "3"
c = a + b
print(c)

d = "this is python 3"
print("this outPut %s" % d)

x = "Hello, & Namaste World!"
# It will print the word of the mentioned number
print(x[10])
print(x[2:5])
print(x[2:])
print(x[-5:-2])

# Making loop one below another
for a in x:
    print(a)

# prints the length
print(len(x))

# It checks weather the word/number is there in the value
print("Namaste" in x)  # It gives True
print("hii" in x)  # It gives False

# It makes the value in capslock
print(x.upper())
# It makes the value in smaller
print(x.lower())
# It strips with given instruction
print(x.strip())
print(x.strip(","))
# It replaces the word/letter/number
print(x.replace("H", "Y"))

a = "Hello"
b = "World"
print(a + " " + b)

"""GOOGLE"""
# String Methods
# Escape Characters

# Escape character Example
text = "we are \"Vikings\" from the north."
print(text)
