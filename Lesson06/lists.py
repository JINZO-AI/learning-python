users = ["John ", "Sara", "Dave"]
data = ["Dave", 33, True]
emptylist = []
# print("Dave" in users)
# print("Dave" in data)
# print("Dave" in emptylist)

print(users[0])
print(users[-1])
print(users[-2])
print(users.index("Sara"))
print(users[0:1])
print(users[0:2])
print(users[0:])
print(users[1:])
print(users[0:3])
print(users[-3:-1])
print(len(data))

users.append("Elsa")
print(users[3])
users += ["Mark"]
print(users)
users.extend(["Robert", "Jimmy"])
print(users)
# users.extend(data)
# print(users)

users.insert(0, "Bob")
print(users)
users[2:2] = ["Max", "Alex"]
print(users)

users[1:3] = ["Aspas", "Demon1"]
print(users)

users.remove("Demon1")
print(users)

print(users.pop())
print(users)
del users[0]
print(users)

# del data
data.clear()
print(data)

print("")
print("")

users[1:2] = ["kelly"]  # lowercase
# Sorts alphabetically, but checks Capitals (A-Z) BEFORE lowercase (a-z)
users.sort()
print(users)
print("")

users.sort(key=str.lower)
print(users)

print("")
print("")
print("")
print("")

Num = [4, 3, 66, 7, 9, 0, 11, 42]
print(Num)
print("")
Num.reverse()
print(Num)
print("")
Num.sort(reverse=True)
print(Num)
print("")
Num.sort(reverse=False)
print(Num)
print("")

print(sorted(Num, reverse=False))
print(Num)
print("")
print("")
# Create a copy using the built-in method (Clear and readable)
num_Copy = Num.copy()
# Create a copy by casting the data into a new list object
My_Num = list(Num)
# Create a copy using the slice technique (everything from start to end)
My_Copy = Num[:]
print(num_Copy)
print(My_Num)
My_Copy.sort()
print(My_Copy)
print(Num)

print("")
print("")

print(type(Num))
print("")
print("")
My_List = list([1, "Jinzo", True])
print(My_List)


# Tuples
# Tuples are "Immutable" — This means they CANNOT be changed once created.
# Think of it like a "Locked List" that protects your data.
# 1. Faster: Python handles Tuples quicker than Lists.
# 2. Safer: No one can accidentally .append() or .sort() your data.
# 3. Use for: Data that stays together (like Name/Age or Latitude/Longitude).
My_Tuple = tuple(("Dave", 33, False))
Another_Tuple = (1, 2, 3, 4, 5, 4, 4)
print(My_Tuple)
print(Another_Tuple)
print(type(My_Tuple))
print(type(Another_Tuple))

New_List = list(My_Tuple)
New_List.append("Max")
New_Tuple = tuple(New_List)
print(New_Tuple)
# Unpack the tuple
(one, tow, *hey) = Another_Tuple
print(one)
print(tow)
print(hey)
print("")
(one, *tow, hey) = Another_Tuple
print(one)
print(tow)
print(hey)
print("")
print(Another_Tuple.count(4))
