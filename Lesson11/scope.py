# Global scope
name = "John"
count = 1


# def greeting(first_name):  # function has its own local scope
#     color = "blue"  # this variable is only accessible within the greeting function
#     print(first_name)
#     print(name)  # this will work because name is defined in the global scope
#     print(color)  # this will work because color is defined within the greeting function


# greeting("dave")  # calling the function with an argument


def another_function():
    color = "blue"
    # count = 2 # it  does not change the global variable count, it creates a new local variable count within the scope of another_function
    global count  # this tells Python that we want to use the global variable count instead of creating a new local variable
    count += 1  # this will change the value of the global variable count
    print(count)

    def greeting(name):  # function has its own local scope
        print(name)
        nonlocal color  # this tells Python that we want to use the color variable from the nearest enclosing scope (another_function) instead of creating a new local variable
        color = "red"  # this will change the value of the color variable in the another_function scope
        print(color)

    greeting("Alice")


another_function()  # calling another function that calls greeting
