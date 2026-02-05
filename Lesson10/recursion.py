def add_one(num):

    if num >= 9:
        return num + 1 
    total = num + 1
    print(total)

    return add_one(total)


my_new_total = add_one(0)# Output: 1, 2, 3, 4, 5, 6, 7, 8, 9
print(my_new_total)# Output: 10
