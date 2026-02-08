# import math
from math import sqrt, pi  # importing specific functions from a module

# import sys
# from enum import Enum
import random as rdm  # importing a module and giving it an alias using 'as'
import kansas  # importing a custom module named 'kansas'
from rps7 import rock_paper_scissor  # importing the rps function from the rps7 module
# sys.exit()
# random.choice([1, 2, 3, 4, 5])

print(sqrt(16))  # don't need to use math.sqrt() because we imported sqrt directly
print(pi)  # don't need to use math.pi() because we imported pi directly


print(rdm.choice([1, 2, 3, 4, 5]))
# using the alias 'rdm' to access the choice function from the random module

# print(dir(rdm))  # prints all the attributes and methods of the random module
print("--------------------------")
# print(dir(math))  # prints all the attributes and methods of the math module

# for item in dir(rdm):
#     print(item)

# -----------------------------------
print(kansas.capital)
kansas.random_fun_fact()

# print the name of the module we are currently running
print(__name__)
# print the name of the module we are currently running (this will be "__main__" if we are running this file directly)
print(kansas.__name__)  # print the name of the module we imported (kansas)

print("--------------------------")

print(rock_paper_scissor.__name__)
# print the name of the function we imported from rps7
rock_paper_scissor()  # calling the function we imported from rps7
