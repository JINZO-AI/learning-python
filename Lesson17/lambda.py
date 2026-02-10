def squared(num):
    return num * num


print(squared(2))

addTwo = lambda num: num + 2
print(addTwo(12))

sum = lambda a, b: a + b
print(sum(5, 3))


#########################
def func_builder(x):
    return lambda num: num + x


add_ten = func_builder(10)
add_twenty = func_builder(20)

print(add_ten(7))
print(add_twenty(7))

#########################

numbers = [1, 2, 3, 22, 44, 7]
squared_nums = map(lambda num: num * num, numbers)
print(list(squared_nums))
