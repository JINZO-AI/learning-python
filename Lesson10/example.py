value = "yes"
count = 0
# while value:  # also means while value == True
#     print(value)
#     value = False  # 0 also means False, so we can also write value = 0

while value:  # also means while value == True
    count += 1
    print(count)
    if count == 5:
        break
    else:
        value = 0
        continue  # yes it going to check the while value part  to evaluate whether the loop should execute or not
