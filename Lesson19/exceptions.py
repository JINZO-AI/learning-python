# try:
#     print(x)
# except NameError:
#     print("NameError means something is probably undefined.")


class JustNotCollError(Exception):
    pass


x = 2
try:
    raise JustNotCollError("this just isn't cool,man.")
    # raise Exception("im a custom exception!")
    # print(x / 0)
    # if not type(x) is str:
    #     raise TypeError("only strings are allowed")
except NameError:
    print("NameError means something is probably undefined.")
except ZeroDivisionError:
    print("pls do not divide by zero.")
except Exception as error:
    print(error)
else:
    print("no Errors!")
finally:
    print("im going to print with or without an error.")
