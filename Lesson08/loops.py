# Using a while loop

Value = 1
while Value <= 10:
    print("Value is:", Value)
    # if Value == 5: # Uncommenting this will stop the loop when Value is 5
    #     break
    Value += 1
    print("")

while Value <= 10:
    Value += 1
    if Value == 5:
        continue
    print("Value is:", Value)  # Print values from 2 to 11, skipping 5
    print("")
else:
    print("value is now equal to: " + str(Value))

# Using a for loop
names = ["Alice", "Bob", "Charlie", "Diana"]
for x in names:
    print("Name is : " + x)

print("")

for x in "mississippi":  # Iterate through each letter in the string
    print("Letter is : " + x)

print("")
for x in names:
    if x == "Charlie":
        break
    print("Name is : " + x)  # This will print names until it reaches "Charlie"
print("")
for x in names:
    if x == "Charlie":
        continue
    print("Name is : " + x)
print("")
for x in range(11):  # Iterate from 0 to 10
    print(x)
print("")
for x in range(1, 11):  # Iterate from 1 to 10
    print("Value is : " + str(x))  # str() converts integer to string for concatenation
print("")
for x in range(1, 11, 2):  # Iterate from 1 to 10 with a step of 2
    print("Value is : " + str(x))  # This will print odd numbers from 1 to 9
else:
    print("Loop is done!")
print("")
print("")

names = ["Alice", "Bob", "Charlie", "Diana"]
actions = ["running", "jumping", "swimming"]
for name in names:
    for action in actions:
        print(name + " is " + action)
        print("")
print("")
for action in actions:
    for name in names:
        print(name + " is " + action)  #
        print("")
