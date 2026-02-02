# Dictionaries in Python
# A dictionary is a collection of key-value pairs. Each key is unique and is used to access the corresponding value.
# Creating a dictionary
Band = {
    "Vocals": "Plant",
    "Guitar": "Page",
}
Band2 = dict(Vocals="Plant", Guitar="Page")
print(Band)
print(Band2)
print(type(Band))
print(len(Band))
print(type(Band2))
print(len(Band2))


# Access items
print(Band["Vocals"])
print(Band.get("Guitar"))

# list all keys
print(Band.keys())

# list all values
print(Band.values())

# list of key/value pairs as tuples
print(Band.items())

# verify if key exists
print("Vocals" in Band)
print("triangle" in Band)

# changing values
Band["Guitar"] = "Clapton"
Band.update({"bass": "JPj"})
print(Band)

# Removing items
print(Band.pop("bass"))
print(Band)

Band["drums"] = "Bonham"
print(Band)
print("")

print(Band.popitem())  # removes last inserted item will return a tuple
print(Band)
print("")

# Delete and clear dictionary

Band["drums"] = "Bonham"
del Band["drums"]
print(Band)

Band2.clear()
print(Band2)
del Band2
print("")
print("")
print("")

# Copying dictionaries

# Band2 = Band  # this creates a reference, not a copy
# print("bad copy")
# print(Band2)
# print(Band) # both are the same
# Band2["Vocals"] = "Mercury" # this will also change Band
# print(Band) # shows "Mercury" instead of "Plant"

Band3 = Band.copy()
Band3["drums"] = "Moon"
print("good copy")
print(Band3)  # new copy with changes
print(Band)  # original remains unchanged

# or use the dict()  constructor function
Band4 = dict(Band)
print("another good copy")
print(Band4)
print("")
print("")
print("")

# Nested dictionaries
Member1 = {"name": "plant", "instrument": "vocals"}
Member2 = {"name": "page", "instrument": "guitar"}
bandMembers = {"member1": Member1, "member2": Member2}
print(bandMembers)
print("")
print(bandMembers["member1"])
print("")
print(bandMembers["member1"]["name"])
print("")
print("")
print("")


# Sets
# A set is an unordered collection of unique items.
# Creating a set
nums = {1, 2, 3, 4, 5}
nums2 = set([1, 2, 3, 4, 5])
print(nums)
print(nums2)
print(type(nums))
print(len(nums))
print(type(nums2))
print(len(nums2))

# Note: sets do not support indexing or slicing because they are unordered
# No duplicates allowed
nums = {1, 2, 2, 3, 4, 4, 5}  # duplicates will be removed
print(nums)  # Output: {1, 2, 3, 4, 5}
print("")

# True is a duplicate of 1, and False is a duplicate of 0

bool_set = {0, 1, True, False}  # duplicates will be removed
print(bool_set)  # Output: {0, 1}
print("")

# Create a set with mixed integers and booleans
# Note: 1 is treated as True, and 0 is treated as False.
# The set only keeps the first one it sees and removes the rest.

nums = {1, True, 2, False, 3, 4, 0}

# Output will be {False, 1, 2, 3, 4} (or a different order)
# - True was removed because 1 was already there.
# - 0 was removed because False was already there.
print(nums)

# Check if a value exists in a set
print(2 in nums)
# but u cannot do indexing like nums[0]or a key like nums["key"] because sets are unordered
print("")
print("")

# Adding a new element to a set
nums.add(5)
nums.add(99)
print(nums)
print("")


# Add elements from one set to another
more_nums = {6, 7, 8}
nums.update(more_nums)
print(nums)
# you can also use update with lists or tuples and  dictionaries.

print("")
print("")
print("")

# Merge two sets to cerate a new set
set_a = {1, 2, 3}
set_b = {3, 4, 5}
set_c = set_a.union(set_b)
print(set_c)  # Output: {1, 2, 3, 4, 5}
print("")

# Keep only the duplicates
set_a = {1, 2, 3}
set_b = {3, 2, 5}
set_c = set_a.intersection(set_b)  # creates a new set with duplicates
print(set_c)  # Output: {2, 3}
print("")
set_a.intersection_update(set_b)  # modifies set_a to keep only duplicates
print(set_a)  # Output: {2, 3}
print("")

# Keep EVERYTHING EXCEPT the duplicates.
set_a = {1, 2, 3}
set_b = {3, 2, 5}
set_c = set_a.symmetric_difference(set_b)  # creates a new set without duplicates
print(set_c)  # Output: {1, 5}
print("")
set_a.symmetric_difference_update(set_b)  # modifies set_a to remove duplicates
print(set_a)  # Output: {1, 5}
