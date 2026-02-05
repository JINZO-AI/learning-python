def hello():
    print("Hello, world!")


hello()


def hello_words():
    print("Hello, world!")


hello_words()


def sum(num1, num2):
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


total = sum(3, 10)
print(total)


def sum(num1=0, num2=0):  # num1 and num2 will be 0 by default if not provided
    if type(num1) is not int or type(num2) is not int:
        return
    return num1 + num2


total = sum()  # num1 and num2 will be 0 by default
print(total)

print("------------------")


def multiple_items(
    *args,
):  # *args allows for an arbitrary number of arguments to be passed to the function
    print(
        args
    )  # args will be a tuple containing all the arguments passed to the function
    print(type(args))  # args will be of type tuple


multiple_items("dog", "cat", "mouse")
multiple_items(1, 2, 3, 4, 5)

print("------------------")

def multiple_named_items(**kwargs):# **kwargs allows for an arbitrary number of keyword arguments to be passed to the function
    print(kwargs)  # kwargs will be a dictionary containing all the keyword arguments passed to the function
    print(type(kwargs))  # kwargs will be of type dict

multiple_named_items(name="Alice", age=30, city="New York")# multiple_named_items can accept any number of keyword arguments, and they will be stored in the kwargs dictionary. In this example, we are passing three keyword arguments: name, age, and city. The function will print the kwargs dictionary and its type.
multiple_named_items(country="USA", language="English", population=331000000)