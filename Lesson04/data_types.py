import math

# String data type

# Lliteral assignment

first = "Jhon"
last = "Gray"

# print(type(first))
# print(type(first) == str)
# print(isinstance(first, str))

# Constructor function
# pizza = str("Pepperoni")
# print(type(pizza))
# print(type(pizza) == str)
# print(isinstance(pizza, str))

# Concatenation
fullname = first + " " + last
print(fullname)

fullname += "!"
print(fullname)

# Casting a Number  to a String
decade = str(2002)
print(type(decade))
print(decade)

Statement = " I like pop music from the " + decade + "s."
print(Statement)

# Multiple lines

multiline = """
 Hey, how are you ?                                             
 
 
I was just checking in.   
                                    All good?
 
 
 """
print(multiline)

# Escaping special charcters
sentence = "I'm back at work!\tHey!\n\nWhere's this at \\located?"
print(sentence)

# string Methods
print(first)
print(first.lower())
print(first.upper())
print(first)
print(multiline.title())
print(multiline.replace("good", "ok"))
print(multiline)

print(len(multiline))
multiline += "                             "
multiline = "            " + multiline
print(len(multiline))


print(len(multiline.strip()))
print(len(multiline.lstrip()))
print(len(multiline.rstrip()))
print("")


# Build a menu
title = "menu".upper()
print(title.center(20, "="))
print("Coffee".ljust(16, ".") + "$1".rjust(4))
print("Muffin".ljust(16, ".") + "$2".rjust(4))
print("Cheesecake".ljust(16, ".") + "$4".rjust(4))

print("")


# String index values
print(first[1])
print(first[1:-1])
print(first[1:])
print("")

# Some methods retun boolean data
print(first.startswith("J"))
print(first.endswith("D"))

print("")

# boolean data type

myvalue = True
x = bool(False)
print(type(x))
print(isinstance(myvalue, bool))
print("")
print("")

# Numeric data types

# integer type
price = 100
best_price = int(80)
print(type(price))
print(isinstance(best_price, int))
print("")
print("")

# float type
gpa = 3.89
y = float(1.14)
print(type(gpa))
print(isinstance(y, float))
print("")
print("")

# Complex type
comp_value = 5 + 3j
print(type(comp_value))
print(comp_value.real)
print(comp_value.imag)
print("")
print("")

# Built-in function for numbers
print(abs(gpa))
print(abs(gpa * -1))
print(round(gpa))
print(round(gpa, 1))
print("")
print("")

print(math.pi)
print(math.sqrt(64))
print(math.ceil(gpa))
print(math.floor(gpa))
print("")
print("")

# Castring a string to a number
zipcode = "4000"
zipe_value = int(zipcode)
print(type(zipe_value))

# Error if you attempt to cast incorrect data
zipe_value = int("Seoul")
