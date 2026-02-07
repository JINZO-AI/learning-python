person = "Dave"
coins = 3
print("\n" + person + " has " + str(coins) + " coins left")

message = "\n%s has %s coins left" % (person, coins)  # old way of doing it
print(message)

# format method approach
message = "\n{} has {} coins left".format(person, coins)
# new way of doing it before f-strings
print(message)


message = "\n{1} has {0} coins left".format(person, coins)
# you can also specify the order of the variables in the format method
print(message)


message = "\n{person} has {coins} coins left".format(coins=coins, person=person)
# you can also specify the variable names in the format method
print(message)

player = {"person": "Dave", "coins": 3}

message = "\n{person} has {coins} coins left".format(**player)
# you can also unpack a dictionary in the format method
print(message)


# f-strings approach this is the way to do it in python
message = f"\n{person} has {coins} coins left"
# f-strings are faster than the format method and are more readable. you can also use expressions inside f-strings
print(message)


message = f"\n{person} has {2 * 3} coins left"
# you can also use expressions inside f-strings
print(message)

message = f"\n{person.lower()} has {2 * 3} coins left"
# you can also use methods inside f-strings
print(message)


message = f"\n{player['person']} has {2 * 3} coins left"
# you can also use dictionary keys inside f-strings
print(message)

###################
# You can pass formatting options inside f-strings as well

num = 10
print(f"\n2.25 times {num} is {2.25 * num:.2}\n")
# the :.2f formats the number to 2 decimal places

for num in range(1, 11):
    print(f"2.25 times {num} is {2.25 * num:.2f}")


for num in range(1, 11):
    print(f"{num} divided by 4.52 is  {num / 4.52:.2%}")
    # the :.2% formats the number as a percentage with 2 decimal places
